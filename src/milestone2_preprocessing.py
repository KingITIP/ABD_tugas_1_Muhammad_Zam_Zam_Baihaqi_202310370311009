# C:\\project_1\\data analysis\\tugas 1\\src\\milestone2_preprocessing.py
from pathlib import Path
import sys

import duckdb
import polars as pl

ROOT = Path(r"C:\project_1\data analysis\tugas 1")
DATASET_DIR = ROOT / "dataset"
RAW_XLSX = DATASET_DIR / "01_Data-Ch-Jabar-2020-2025.xlsx"
META_XLSX = DATASET_DIR / "02_West_Java_Rainfall_Station_Metadata_Lengkap.xlsx"
OUT_DIR = ROOT / "prosessed_data"
OUT_PARQUET = OUT_DIR / "west_java_rainfall_long_clean.parquet"
OUT_CSV_SAMPLE = OUT_DIR / "west_java_rainfall_long_clean_sample_10000.csv"

OUT_DIR.mkdir(parents=True, exist_ok=True)

def main():
    print("="*60)
    print("MILESTONE 2 - DATA CLEANING & PREPROCESSING")
    print("Dataset: West Java Daily Rainfall 2020-2025 (BMKG)")
    print("="*60)

    print("\n[1/8] Loading wide matrix from Excel...")
    df_wide = pl.read_excel(RAW_XLSX, sheet_name="DATA")
    print(f"Wide shape: {df_wide.shape[0]:,} rows x {df_wide.shape[1]:,} cols")

    date_col = df_wide.columns[0]
    station_cols = [c for c in df_wide.columns if c != date_col]
    print(f"Date col: {date_col} | Jumlah stasiun: {len(station_cols)}")

    print("\n[2/8] Melting wide -> long format...")
    df_long = df_wide.unpivot(
        index=[date_col],
        on=station_cols,
        variable_name="station_id",
        value_name="rainfall_mm"
    ).rename({date_col: "tanggal"})
    
    df_long = df_long.with_columns([
        pl.col("tanggal").cast(pl.Date),
        pl.col("rainfall_mm").cast(pl.Utf8).str.strip_chars().alias("rainfall_mm_str")
    ])
    
    # Handle trace/symbolic values from BMKG (R, TR, T, -, empty)
    df_long = df_long.with_columns([
        pl.when(
            pl.col("rainfall_mm_str").is_null() |
            (pl.col("rainfall_mm_str") == "") |
            pl.col("rainfall_mm_str").str.to_lowercase().is_in(["nan", "none", "-", "na"])
        )
        .then(None)
        .when(pl.col("rainfall_mm_str").str.to_lowercase().is_in(["r", "tr", "t", "trace"]))
        .then(0.0)
        .otherwise(pl.col("rainfall_mm_str").str.replace_all(r"[^0-9\.\-]", ""))
        .alias("rainfall_mm_clean_str")
    ]).with_columns([
        pl.when(pl.col("rainfall_mm_clean_str") == "")
        .then(None)
        .otherwise(pl.col("rainfall_mm_clean_str").cast(pl.Float64, strict=False))
        .alias("rainfall_mm")
    ]).drop(["rainfall_mm_str", "rainfall_mm_clean_str"])
    
    print(f"Long shape (raw melt): {df_long.shape[0]:,} rows x {df_long.shape[1]:,} cols")
    print(f"Expected ~ {len(df_wide)*len(station_cols):,} rows")

    print("\n[3/8] Loading station metadata & joining...")
    try:
        df_meta = pl.read_excel(META_XLSX, sheet_name="metadata")
        df_meta = df_meta.rename({c: c.strip().lower().replace(" ", "_").replace("/", "_") for c in df_meta.columns})
        if "station_id" not in df_meta.columns:
            for cand in ["id_stasiun", "kode_stasiun", "stationid", "id"]:
                if cand in df_meta.columns:
                    df_meta = df_meta.rename({cand: "station_id"})
                    break
        df_long = df_long.join(df_meta, on="station_id", how="left")
        print("Metadata joined. Columns now:", len(df_long.columns))
    except Exception as e:
        print(f"[WARN] Gagal join metadata: {e}")

    print("\n[4/8] Profiling with DuckDB SUMMARIZE...")
    con = duckdb.connect()
    con.register("df_long", df_long.to_pandas())
    try:
        summ = con.execute("SUMMARIZE SELECT * FROM df_long").df()
        print(summ[["column_name","column_type","min","max","approx_unique","avg","count","null_percentage"]].head(15).to_string())
    except Exception as e:
        print(f"[WARN] SUMMARIZE error: {e}")
    con.close()

    print("\n[5/8] Detecting missing values...")
    before_null = df_long.null_count().sum_horizontal().item()
    print(f"Total null before: {before_null:,}")
    df_mv = df_long
    after_null = df_mv.null_count().sum_horizontal().item()
    print(f"Total null after: {after_null:,}")
    print("[INFO] rainfall_mm NaN = missing observation (dipertahankan). Nilai 'R/TR/T' dikonversi ke 0.0 (trace).")

    print("\n[6/8] Outlier handling with IQR + winsorization (clip)...")
    q = df_mv.filter(pl.col("rainfall_mm").is_not_null() & (pl.col("rainfall_mm") >= 0)) \
             .select([
                 pl.col("rainfall_mm").quantile(0.25).alias("q1"),
                 pl.col("rainfall_mm").quantile(0.75).alias("q3")
             ]).row(0)
    q1,q3 = q[0], q[1]
    iqr = q3-q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    print(f"Q1={q1:.2f} | Q3={q3:.2f} | IQR={iqr:.2f}")
    print(f"IQR bounds: [{lower:.2f}, {upper:.2f}]")
    
    df_out = df_mv.with_columns([
        pl.when(pl.col("rainfall_mm").is_null())
          .then(None)
          .when(pl.col("rainfall_mm").is_between(lower, upper, closed="both"))
          .then(pl.col("rainfall_mm"))
          .when(pl.col("rainfall_mm") > upper).then(upper)
          .when(pl.col("rainfall_mm") < lower).then(lower)
          .otherwise(pl.col("rainfall_mm"))
          .alias("rainfall_mm_clipped")
    ])

    print("\n[7/8] Deduplication & validation...")
    key = ["tanggal", "station_id"]
    before_dedup = df_out.height
    df_dedup = df_out.unique(subset=key, keep="first")
    after_dedup = df_dedup.height
    print(f"Rows before dedup by {key}: {before_dedup:,}")
    print(f"Rows after dedup: {after_dedup:,} | Removed: {before_dedup-after_dedup:,}")
    
    valid = df_dedup.select([
        pl.len().alias("total_rows"),
        pl.col("rainfall_mm").is_null().sum().alias("null_rainfall"),
        pl.col("rainfall_mm_clipped").is_null().sum().alias("null_rainfall_clipped"),
        ((pl.col("rainfall_mm") < 0) & pl.col("rainfall_mm").is_not_null()).sum().alias("neg_rainfall"),
        pl.col("tanggal").is_null().sum().alias("null_tanggal"),
        pl.col("station_id").is_null().sum().alias("null_station_id"),
    ])
    print(valid)

    print("\n[8/8] Saving processed data...")
    priority_cols = ["tanggal", "station_id", "rainfall_mm", "rainfall_mm_clipped"]
    other_cols = [c for c in df_dedup.columns if c not in priority_cols]
    df_save = df_dedup.select(priority_cols + other_cols)
    
    df_save.write_parquet(OUT_PARQUET)
    print(f"SAVED: {OUT_PARQUET}")
    print(f"Shape: {df_save.shape[0]:,} rows x {df_save.shape[1]:,} cols")
    df_save.head(10000).write_csv(OUT_CSV_SAMPLE)
    print(f"SAMPLE: {OUT_CSV_SAMPLE}")
    print(f"File size: {OUT_PARQUET.stat().st_size / (1024**2):.2f} MB")
    
    print("\n" + "="*60)
    print("MILESTONE 2 SELESAI")
    print("="*60)
    print(f"Total rows: {df_save.shape[0]:,} (> 1,000,000: {'YES' if df_save.shape[0] > 1000000 else 'NO'})")
    print("Output tersimpan di: prosessed_data/")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)
