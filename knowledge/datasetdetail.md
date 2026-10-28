Daily Rainfall 460 Stations West Java + Flood Catalog ⭐ TERBAIK
Atribut	Detail
Nama Dataset	Daily Rainfall Observations from 460 Stations and Flood Event Records across West Java, Indonesia (2020–2025)
Sumber	Mendeley Data, diterbitkan oleh IPB University (BMKG + BBWS + BNPB)
URL	https://data.mendeley.com/datasets/d7j3s64vvr/3
DOI	10.17632/d7j3s64vvr.3
Lisensi	CC BY 4.0 ✅ — bebas digunakan, cukup sebut sumber
Format	CSV
Jumlah baris (estimasi)	~1.008.320 baris (460 stasiun × 2.192 hari) jika format long ✅
Periode data	1 Januari 2020 – 31 Desember 2025
Unit analisis	Satu baris = satu hari pengukuran di satu stasiun BMKG
Kolom utama	station_id, date (daily), rainfall_mm (curah hujan mm), quality_flag, province_code, regency_code (kode admin BPS 2023)
File tambahan	station_metadata.csv (460 baris — nama, lat, lon, ketinggian, jenis stasiun), flood_events.csv (4.231 kejadian banjir, BNPB), consensus_table.csv (3.514 baris — linking kejadian banjir ke stasiun terdekat)
Kolom waktu?	✅ date (daily, 2020–2025)
Kolom lokasi/wilayah?	✅ Lat/lon per stasiun + kode wilayah BPS (kabupaten/kota) Jawa Barat
QC data	4-tahap WMO-compliant; stasiun dengan >30% missing data diflagging, tidak diimputasi
Cara unduh	Buka URL → klik “Download All” (tidak perlu login di Mendeley untuk dataset publik)

Kelayakan Ukuran:

✅ ~1.008.320 baris (long format) → MEMENUHI >1 juta baris
⚠️ CATATAN PENTING: Perlu dikonfirmasi bahwa file CSV disimpan dalam format long (baris per stasiun per hari), bukan wide (matriks hari × stasiun). Jika wide format → hanya 2.192 baris × 460 kolom = tetap kaya data tetapi baris sedikit. Lakukan pengecekan saat download.

Kelebihan:

Sumber resmi BMKG + terverifikasi oleh peneliti IPB
CC BY 4.0 — lisensi paling aman untuk tugas akademik
Ada data kejadian banjir untuk enrichment analisis
Koordinat WGS84 lengkap → siap peta spasial

Kekurangan:

Cakupan hanya Jawa Barat (bukan seluruh Indonesia)
Variabel tunggal (curah hujan), bukan multi-parameter iklim

Potensi Insight:

Korelasi curah hujan dengan kejadian banjir per kabupaten
Tren musim hujan 2020–2025 (dampak La Niña/El Niño)
Peta hotspot curah hujan tinggi per bulan di Jawa Barat
Anomali curah hujan di stasiun tertentu dibanding rata-rata regional

Kelayakan: ✅ LAYAK — Satu-satunya kandidat yang secara konkret memenuhi syarat jumlah baris >1 juta (jika long format), lisensi jelas, dan sumber terverifikasi