# Prompt Claude - Pencarian Dataset Tugas 1 ABD 2026

Copy paste prompt ini ke Claude untuk mencari dataset Indonesia yang **cocok, valid, dan siap dipakai** untuk Tugas 1 Analisis Big Data.

```text
Kamu adalah asisten pencari dataset untuk Tugas 1 mata kuliah Analisis Big Data (ABD) 2026 Universitas Muhammadiyah Malang.

TUGAS KAMU:
Cari dan rekomendasikan dataset Indonesia yang BENAR-BENAR memenuhi persyaratan tugas ini dengan hasil yang siap dipakai.

PERSYARATAN WAJIB:
- Berasal dari sumber Indonesia yang legal & bisa diverifikasi (Satu Data Indonesia, BPS, BMKG Data Online, HuggingFace, Kaggle, Google Dataset Search)
- Ukuran minimal 500 MB ATAU jumlah baris > 1.000.000 baris (wajib salah satu / keduanya lebih baik)
- Bertema Indonesia / relevan untuk analisis Indonesia
- Memiliki deskripsi yang jelas (nama file, format, struktur kolom, periode data, unit analisis)
- Bisa diunduh secara publik (cek lisensi / ketentuan pakai)
- Cocok dianalisis dengan Polars + DuckDB
- Memiliki potensi analisis temporal ATAU spasial (sangat disarankan) karena ada tuntutan minimal 6 visualisasi interaktif + 5 insight di Milestone 3
- Format yang diutamakan: .CSV, .JSON, .JSONL, .PARQUET, .XLSX/.XLS (utamakan yang bisa langsung dibaca Polars/DuckDB)

BATASAN & PERINGATAN:
- Jangan merekomendasikan dataset yang terlalu kecil (< 500MB atau < 1jt baris)
- Jangan merekomendasikan link download yang membutuhkan login berbayar / akses tertutup
- Jangan merekomendasikan dataset dengan lisensi "No License" yang ambigu atau jelas dilarang komersial tanpa izin (jelaskan risikonya)
- Jangan hanya asal ambil yang populer di Kaggle tanpa cek ukuran aslinya
- Fokus pada dataset mentah yang bisa langsung di-load, bukan hasil agregat kecil

YANG HARUS KAMU LAKUKAN:
1. Carikan minimal 3 kandidat dataset yang PALING RELEVAN
2. Untuk SETIAP kandidat, berikan detail lengkap:
   - Nama dataset
   - Sumber (URL persis)
   - Lisensi / ketentuan pakai
   - Format file (csv/parquet/json/xlsx)
   - Estimasi ukuran file (MB/GB) ATAU estimasi jumlah baris (dari metadata/deskripsi)
   - Periode data (tahun/bulan jika ada)
   - Unit analisis (apa yang diwakili tiap baris)
   - Struktur kolom (daftar kolom penting + tipe data yang diperkirakan)
   - Ada kolom waktu (tanggal/waktu)? Ada kolom lokasi/wilayah (provinsi/kabupaten/kota/lat-lon)?
   - Kesesuaian untuk Milestone 1-3
   - Potensi insight menarik (minimal 1)
   - Cara unduh (link langsung atau langkah-langkah)
   - Kelayakan: LAYAK / PERLU CEK / TIDAK LAYAK + alasan singkat
3. Rekomendasikan SATU kandidat TERBAIK untuk dikerjakan (berdasarkan kelayakan, potensi EDA, kemudahan analisis dengan Polars+DuckDB)
4. Berikan saran konkret: kolom mana yang bisa dipakai buat analisis temporal/spasial, ide minimal 6 visualisasi interaktif yang realistis
5. Berikan template siap isi untuk `data/README.md` berdasarkan kandidat terpilih

FORMAT OUTPUT:
Keluarkan hasil dalam bentuk terstruktur, mudah dibaca, dan LANGSUNG bisa aku copy ke:
- `data/README.md` (tabel + cara unduh)
- Catatan Milestone 1 di `notebooks/01_data_profiling.ipynb`

GUNAKAN PENDEKATAN PRAKTIS:
- Prioritaskan dataset dari Satu Data Indonesia/BPS/BMKG (cenderung kredibel & aman untuk tugas kuliah)
- Jika dari Kaggle/HuggingFace, wajib verifikasi ukuran file saat download / link metadata-nya
- Hindari rekomendasi yang hanya berupa "kumpulan gambar" atau dataset non-tabular
- Utamakan dataset TABULAR (baris x kolom) karena notebook Polars/DuckDB yang disediakan berbasis tabular

Mulai pencarian sekarang berdasarkan semua poin di atas.
``` 

## Cara Pakai

1. Buka [claude.ai](https://claude.ai/) (atau Claude di platform yang kamu pakai)
2. Copy seluruh isi prompt di atas
3. Paste ke chat Claude
4. Tunggu hasil rekomendasi (minimal 3 kandidat + 1 rekomendasi terbaik)
5. Pilih salah satu kandidat, ikuti saran cara unduh, letakkan file ke `data/raw/`, isi `data/README.md` sesuai template yang Claude berikan
6. Lanjut ke `notebooks/01_data_profiling.ipynb` untuk mulai profiling
