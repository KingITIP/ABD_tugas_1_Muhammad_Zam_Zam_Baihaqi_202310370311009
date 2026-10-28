# Data Tugas 1

## Dataset yang Dipilih

| Item | Isi |
|---|---|
| Nama dataset | Daily Rainfall Observations from 460 Stations and Flood Event Records across West Java, Indonesia (2020-2025) |
| Sumber | [Mendeley Data - DOI: 10.17632/d7j3s64vvr.3](https://data.mendeley.com/datasets/d7j3s64vvr/3) (BMKG dataonline.bmkg.go.id, DIBI-BNPB, BPBD Jawa Barat) |
| Lisensi/ketentuan pakai | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| Ukuran | Total file < 10 MB (raw). Saat di-unpivot ke format long (`tanggal`, `station_id`, `rainfall_mm`) menghasilkan **~1.008.320 baris** (> 1.000.000 baris) sehingga memenuhi syarat tugas |
| Periode data | 1 Januari 2020 – 31 Desember 2025 (2.192 hari) |
| Unit analisis | Observasi curah hujan harian per stasiun BMKG (07:00–07:00 WIB, UTC+7) |

## File yang Digunakan (data/raw/)

| File | Keterangan |
|---|---|
| `01_Data-Ch-Jabar-2020-2025.xlsx` (Sheet `DATA`) | Matriks harian wide-format (Date x 460 stasiun). File utama. |
| `02_West_Java_Rainfall_Station_Metadata_Lengkap.xlsx` (Sheet `metadata`) | Metadata 460 stasiun (nama stasiun, kabupaten/kota, koordinat, elevasi). |
| `03_Data-Event_Banjir-2020-2025.xlsx` | Rekam kejadian banjir 2020–2025. |
| `04_consensus_rainfall_flood.csv` | Linking kejadian banjir dengan stasiun terdekat (±25 km, ±1 hari). |
| `05_missing_data_summary.csv` | Ringkasan missing per stasiun per bulan. |
| `06_spatial_layers.gpkg` | Layer spasial (stasiun, kejadian banjir, batas wilayah). |
| `07_Figures/` | Gambar pendukung dari sumber dataset. |
| `08_README.md`, `09_CHANGELOG.md` | Dokumentasi asli dari Mendeley Data. |

## Cara Memperoleh Data

1. Dataset diperoleh dari Mendeley Data (DOI: 10.17632/d7j3s64vvr.3)
2. Seluruh file telah ditempatkan di folder `data/raw/`
3. Untuk analisis, `01_Data-Ch-Jabar-2020-2025.xlsx` di-transform menjadi bentuk *long format* (unpivot/melt) agar jumlah baris > 1.000.000 baris
4. Data bersih hasil preprocessing disimpan di `data/processed/dataset_bersih.parquet`

## Aturan Penyimpanan

- `data/raw/` berisi data mentah dan tidak diubah.
- `data/processed/` berisi hasil cleaning yang siap dipakai untuk Milestone 3.
- Jangan commit file mentah berukuran besar ke Git jika tidak diperlukan; pada repo ini data mentah sudah didokumentasikan sesuai struktur tugas.
