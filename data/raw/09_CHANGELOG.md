# CHANGELOG

All notable changes to the dataset *Daily Rainfall Observations from 460 Stations and Flood Event Records across West Java, Indonesia (2020–2025)* (Mendeley Data DOI: 10.17632/d7j3s64vvr) will be documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [Version 1] — 2026-04-27 (initial release)

### Added
- **File 1** `Data-Ch-Jabar-2020-2025.xlsx` — daily rainfall matrix (2,192 days × 460 stations).
- **File 2** `West_Java_Rainfall_Station_Metadata_Lengkap.xlsx` — 460 rainfall-station metadata records.
- **File 3** `Data-Event_Banjir-2020-2025.xlsx` — 4,231 flood event records (DIBI-BNPB + BPBD West Java).
- **File 4** `04_consensus_rainfall_flood.csv` — 4,231 event–rainfall links with `API_5d`, threshold/ML/consensus classes, confidence, and `is_flash_flood` flag.
- **File 5** `05_missing_data_summary.csv` — per-station × per-month missing-data percentages (33,120 rows).
- **File 6** `06_spatial_layers.gpkg` — GeoPackage (EPSG:4326) with `stations`, `districts`, `events`, `flash_flood_events` layers.
- **File 7** `07_figures/` — six diagnostic and descriptive PNG figures (Fig. 1–6).
- **File 8** `08_README.md` — dataset description, file inventory, methods overview, citation.
- **File 9** `09_CHANGELOG.md` — this file.

### Quality control
- Format harmonization, range check (0–500 mm/day), persistence check (≥7 identical non-zero values), and spatial coherence (nearest-3 stations) per WMO-No. 1186.
- Stations with >30 % missing daily values flagged but **retained**.
- Rainfall matrix (File 1) left **unimputed** to preserve raw observational integrity.
- Consensus table (File 4) uses Inverse Distance Weighting (IDW, power = 2) for short gaps (≤2 days).

### Notes
- Aligned with companion Data in Brief manuscript v7 (flash-flood focus).
- Flash-flood ground truth based on "banjir bandang" tags in original reports and onset ≤6 h after triggering rainfall, per WMO-No. 1072.
- Event–rainfall linking is a first-order spatial proxy (Haversine, ≤25 km). For hydrological modelling, downstream users should aggregate rainfall to basin scale (Thiessen / kriging) — see manuscript Section 3.5.

---

## Planned (Version 2, tentative)
- Basin-aggregated rainfall (Thiessen polygons + ordinary kriging) for the 14 major catchments of West Java.
- Sub-daily rainfall (hourly) for the subset of stations where AWS data is available.
- Cross-validation against GSMaP and IMERG satellite precipitation products.
