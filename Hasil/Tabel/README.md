# Tabel

Lima tabel dibuat *notebook* tahap 2: tiga dari EDA dan pemilihan stasiun uji (bagian 02), satu dari dasar keputusan *forward fill* (04.6), dan satu dari *baseline* tahap 4 (04.5).

| Berkas | Isi |
|---|---|
| `t2_tabel_nilai_hilang.csv` | Persen nilai hilang per kolom (9 stasiun latih, data latih) |
| `t2_tabel_ringkas_stasiun.csv` | Rata-rata, median, dan persen hilang PM2.5 per stasiun (12 stasiun, sebelum batas uji), dengan kolom `kelompok` (latih atau uji) |
| `t2_tabel_distribusi_stasiun.csv` | Jarak distribusi PM2.5 tiap stasiun terhadap 11 stasiun lain (Wasserstein dan KS, sebelum batas uji), dasar memilih tiga stasiun uji |
| `t2_tabel_ffill.csv` | RMSE Ridge dan *HistGradientBoosting* untuk batas *forward fill* 0 sampai 24 jam (9 stasiun latih, data latih) |
| `t4_tabel_baseline.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive forecast* |

Dibuat ulang setiap *notebook* tahap 2 dijalankan.

**Catatan 16 Nov 2026:** *notebook* sudah ditulis ulang untuk desain 9/3, tetapi belum dijalankan ulang di repo ini. Isi folder ini masih hasil pilot Tiantan (data latih Tiantan saja) sampai *notebook* dijalankan. `t2_tabel_transfer.csv` (RMSE model Tiantan di stasiun lain) adalah sisa pilot dan tidak dibuat lagi oleh *notebook* 9/3.
