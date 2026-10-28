# Rangkuman Tugas 1: Eksplorasi & Analisis Dataset Besar Indonesia

> Sumber: `tugas1-abd-2026/` | Target: `tugas 1/knowledge/tugas_1.md`

## 1. Tujuan Tugas
Menganalisis dataset besar bertema Indonesia (minimal **500 MB** atau **> 1 juta baris**) dengan pendekatan *big data* menggunakan **Polars** (manipulasi/transformasi efisien) dan **DuckDB** (analitik SQL & profiling). Output harus ter-reproduksi lewat `Dockerfile`, `requirements.txt`, dan notebook yang bisa dieksekusi berurutan.

## 2. Timeline Milestone

| Milestone | Target Pertemuan | Yang Wajib Dikerjakan | Bukti |
|---|---|---|---|
| **Milestone 1** | Pertemuan 3 | Pilih & dokumentasikan dataset Indonesia, pastikan ukuran memenuhi syarat | `data/README.md` terisi + `notebooks/01_data_profiling.ipynb` |
| **Milestone 2** | Pertemuan 5 | Profiling dengan `DuckDB SUMMARIZE`, *data cleaning* (missing, duplikasi, outlier), validasi | `notebooks/02_data_cleaning.ipynb` + `data/processed/dataset_bersih.parquet` |
| **Milestone 3** | Pertemuan 8 | Analisis temporal/spasial, minimal 6 visualisasi interaktif, minimal 5 insight | `notebooks/03_eda_and_insights.ipynb` |
| **Final Submission** | Pertemuan 10 | Reproduktivitas penuh, dokumentasi, riwayat commit bertahap | `Dockerfile`, `requirements.txt`, README lengkap, repo siap dinilai |

## 3. Struktur Repo yang Harus Dipenuhi

```text
.
├── .github/workflows/lint_check.yml
├── data/
│   ├── raw/                # data mentah (JANGAN di-commit)
│   ├── processed/          # hasil cleaning (bisa disimpan bila wajar)
│   └── README.md           # sumber, lisensi, ukuran, cara unduh
├── notebooks/
│   ├── 01_data_profiling.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda_and_insights.ipynb
├── output/figures/         # (opsional) simpan figure jika diperlukan
├── src/                    # (opsional) modul reusable jika mau dipisah
├── Dockerfile
├── requirements.txt
└── README.md
```

## 4. Alur Kerja Per Milestone

### Milestone 1 - Data Profiling
**File:** `notebooks/01_data_profiling.ipynb`

- [ ] **Dokumentasi dataset**: Isi tabel di `data/README.md` (Nama, Sumber, Lisensi, Ukuran >=500MB/>1jt baris, Periode, Unit Analisis)
- [ ] **Siapkan data**: Letakkan file ke `data/raw/`. Sesuaikan `DATA_PATH` ke format yang dipakai (`.parquet`/`.csv`).
- [ ] **Profil dengan Polars**: Pakai `pl.scan_parquet()` (lazy) lalu `collect()`. Lihat schema, jumlah baris, jumlah `null` per kolom, 10 baris contoh.
- [ ] **Profil dengan DuckDB**: Pakai `SUMMARIZE SELECT * FROM read_parquet(?)` untuk dapat tipe data, min/max, distinct, null count, dll dalam 1 perintah.
- [ ] **Catatan awal**: Tulis temuan di bagian "Catatan Milestone 1" (ukuran, baris, kolom bermasalah, dugaan anomali).

> Tips: Utamakan `.parquet` kalau memungkinkan (lebih efisien buat dataset besar).

### Milestone 2 - Data Cleaning & Quality
**File:** `notebooks/02_data_cleaning.ipynb` | **Output:** `data/processed/dataset_bersih.parquet`

- [ ] **Load data mentah**: Baca dari `data/raw/` via Polars.
- [ ] **SUMMARIZE ulang**: Pakai DuckDB `SUMMARIZE` dari DataFrame ter-load untuk cross-check.
- [ ] **Deteksi missing**: Hitung jumlah & persentase `null` per kolom, urutkan yang paling bermasalah.
- [ ] **Penanganan missing**: Tentukan strategi per kolom (numerik -> median/mean, kategorik -> modus/default). Dokumentasikan alasannya.
- [ ] **Deteksi & penanganan outlier**: Mulai dari metode **IQR** (hitung Q1,Q3,IQR, batas bawah/atas). Direkomendasikan **winsorization/clipping** ke batas valid ketimbang langsung drop seluruh baris.
- [ ] **Deduplikasi**: **JANGAN** deduplikasi seluruh baris. Tentukan **kolom kunci bisnis** (mis. ID unik) lalu `unique(subset=[...], keep='first')`.
- [ ] **Validasi dasar**: Buat minimal 1 cek (mis. nilai diluar batas IQR, null tersisa). Tampilkan hasil validasi.
- [ ] **Simpan**: `write_parquet` ke `data/processed/dataset_bersih.parquet`. Catat perubahan dimensi (baris sebelum/sesudah).
- [ ] **Catatan**: Dokumentasikan dimensi kualitas paling bermasalah, strategi per jenis masalah, dan aturan validasi di "Catatan Milestone 2".

### Milestone 3 - EDA, Temporal/Spasial & Insight
**File:** `notebooks/03_eda_and_insights.ipynb`

- [ ] **Load data bersih**: Baca `data/processed/dataset_bersih.parquet` dengan Polars.
- [ ] **Analisis temporal/windowing**: Terapkan minimal satu teknik. Contoh: `group_by_dynamic()`, `rolling_mean()`, `shift()`, atau window function DuckDB `OVER(PARTITION BY ... ORDER BY ...)`. Cocokkan dengan ada/tidaknya kolom waktu/tanggal.
- [ ] **Minimal 6 visualisasi interaktif** (Plotly Express/Graph Objects). Usahakan cakup:
  1. **Tren waktu** (line chart + range slider)
  2. **Distribusi/outlier** (boxplot/histogram/violin)
  3. **Korelasi antar variabel numerik** (heatmap/correlation matrix)
  4. **Komposisi kategori** (bar/treemap)
  5. **Pola berkala/siklus** (heatmap per periode)
  6. **Analisis lanjutan/spasial** (scatter/choropleth/map) bila relevan
- [ ] **Minimal 5 insight**: Isi bagian "Rumusan 5 Insight Analitik Utama" dengan temuan berbasis data (bukan asumsi), hubungkan ke visualisasi, dan berikan rekomendasi praktis.
- [ ] **Rapikan notebook**: Beri judul, nama/NIM/username GitHub, penjelasan singkat tiap bagian.

## 5. Aturan Teknis Penting

| Aturan | Keterangan |
|---|---|
| **Tools wajib** | Gunakan **Polars** untuk manipulasi & transformasi, **DuckDB** untuk analitik SQL & `SUMMARIZE`. |
| **Ukuran dataset** | Minimal **500 MB** atau **> 1.000.000 baris**. |
| **Data besar** | Jangan commit file di `data/raw/` atau hasil besar. Hanya dokumentasikan sumber + cara unduh di `data/README.md`. |
| **Efisiensi** | Biasakan `scan_*` + lazy evaluation di Polars sebelum `collect()`. |
| **Cleaning bijak** | Lebih aman *clip/winsorize* outlier ketimbang menghapus massal. Deduplikasi harus berdasar **kunci bisnis**. |
| **Reproduktivitas** | Harus bisa dijalankan via Docker: `docker build -t tugas1-bigdata .` lalu `docker run ... -p 8888:8888 -v "$(pwd)":/home/jovyan/work tugas1-bigdata` → buka `http://localhost:8888/lab` |
| **Git hygiene** | Commit bertahap & deskriptif (contoh: `feat: add initial dataset profiling`, `fix: handle missing values`, `feat: add temporal eda and insights`). |
| **Integritas akademik** | Boleh pakai AI untuk belajar/debug/review, **wajib** bisa jelasin tiap cell & isi **AI Disclosure Statement** di README kalau dipakai. Dilarang copy-paste full repo/orang lain tanpa atribusi. |

## 6. Sumber Dataset yang Aman Digunakan

| Sumber | Cocok Untuk |
|---|---|
| [Satu Data Indonesia](https://data.go.id/) | Data lintas K/L, banyak topik Indonesia |
| [BPS](https://www.bps.go.id/) | Sosial-ekonomi, kependudukan, wilayah |
| [BMKG Data Online](https://dataonline.bmkg.go.id/) | Cuaca/iklim/gempa (cocok buat analisis temporal) |
| [HuggingFace Datasets](https://huggingface.co/datasets) | Dataset publik, mudah difilter |
| [Kaggle](https://www.kaggle.com/datasets) | Beragam, **selalu cek lisensi** |
| [Google Dataset Search](https://datasetsearch.research.google.com/) | Pencarian lintas portal |

## 7. Checklist Cepat Sebelum Submit

- [ ] `data/README.md` lengkap (sumber, lisensi, ukuran, periode, unit analisis)
- [ ] Dataset ada di `data/raw/` (lokal) & memenuhi >=500MB/>1jt baris
- [ ] `01_data_profiling.ipynb` selesai + catatan Milestone 1
- [ ] `02_data_cleaning.ipynb` selesai, ada `data/processed/dataset_bersih.parquet`, catatan Milestone 2
- [ ] `03_eda_and_insights.ipynb` ada >=6 visualisasi interaktif + >=5 insight
- [ ] `Dockerfile`, `requirements.txt`, `README.md` update
- [ ] Commit bertahap terlihat di history Git
- [ ] Bisa `docker build && docker run` & buka JupyterLab tanpa error
- [ ] Bisa jelasin alur Polars/DuckDB + keputusan cleaning + insight yang ditulis
- [ ] Isi **AI Disclosure Statement** di README (jika pakai AI)

## 8. Action Plan Singkat (Mulai Sekarang)

1. **Hari ini**: Fork/clone repo, baca ulang README + ketiga notebook. Tentukan kandidat dataset di `data/README.md`.
2. **M1**: Unduh dataset ke `data/raw/`, sesuaikan `DATA_PATH`, jalankan profiling (Polars + DuckDB), isi catatan.
3. **M2**: Lanjut ke cleaning, tentukan kunci unik + strategi missing/outlier, simpan ke `data/processed/`.
4. **M3**: Rancang minimal 6 chart (fokus ke pertanyaan menarik terkait dataset), tarik 5 insight + rekomendasi.
5. **Final**: Pastikan Docker bisa run, rapikan commit, isi AI disclosure, verifikasi repo GitHub.
