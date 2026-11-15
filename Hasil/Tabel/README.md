# Tabel

Enam tabel: dua dari EDA tahap 2, tiga dari dasar keputusan tahap 2 (bagian 04.6 dan 04.7), dan satu dari *baseline* tahap 4.

| Berkas | Isi |
|---|---|
| `t2_tabel_nilai_hilang.csv` | Ringkasan nilai hilang |
| `t2_tabel_ringkas_stasiun.csv` | Ringkasan per stasiun |
| `t2_tabel_ffill.csv` | RMSE Ridge dan *HistGradientBoosting* untuk batas *forward fill* 0 sampai 24 jam (data latih Tiantan) |
| `t2_tabel_distribusi_stasiun.csv` | Statistik distribusi PM2.5 tiap stasiun terhadap Tiantan (data latih saja) |
| `t2_tabel_transfer.csv` | RMSE model Tiantan di stasiun lain dibanding model yang dilatih sendiri (data latih saja) |
| `t4_tabel_baseline.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive forecast* dan regresi linear |

Dibuat ulang setiap *notebook* tahap 2 dijalankan.
