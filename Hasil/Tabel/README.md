# Tabel

Beberapa tabel dibuat *notebook*: tiga dari EDA dan pemilihan stasiun uji (bagian 02), satu dari dasar keputusan *forward fill* (04.6), satu dari *baseline* tahap 4 (04.5), dan tabel model lanjutan serta *tuning* tahap 5 (bagian 05).

| Berkas | Isi |
|---|---|
| `t2_tabel_nilai_hilang.csv` | Persen nilai hilang per kolom (9 stasiun latih, data latih) |
| `t2_tabel_ringkas_stasiun.csv` | Rata-rata, median, dan persen hilang PM2.5 per stasiun (12 stasiun, sebelum batas uji), dengan kolom `kelompok` (latih atau uji) |
| `t2_tabel_distribusi_stasiun.csv` | Jarak distribusi PM2.5 tiap stasiun terhadap 11 stasiun lain (Wasserstein dan KS, sebelum batas uji), dasar memilih tiga stasiun uji |
| `t2_tabel_ffill.csv` | RMSE Ridge dan *HistGradientBoosting* untuk batas *forward fill* 0 sampai 24 jam (9 stasiun latih, data latih) |
| `t4_tabel_baseline.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive forecast* |
| `t5_tabel_ridge.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive* dan Ridge, perbaikan terhadap *naive* (bagian 05.2) |
| `t5_tabel_ridge_per_fold.csv` | RMSE tiap *fold* untuk *naive* dan Ridge (bagian 05.2) |
| `t5_tabel_tuning_ridge.csv` | Ringkasan 5 nilai `alpha` *tuning* Ridge (bagian 05.1): RMSE dan MAE rata-rata dan sd, selisih berpasangan terhadap `alpha=1` |
| `t5_tabel_tuning_ridge_per_fold.csv` | RMSE dan MAE tiap *fold* untuk 5 nilai `alpha` Ridge |
| `t5_tabel_semua_eksperimen.csv` | 8 konfigurasi Tahap 5 dengan RMSE, MAE, sd, perbaikan terhadap *naive*, dan RMSE tiap *fold*. Sumber `Laporan/Tabel Hasil Percobaan Tahap 5.md` |

Dibuat ulang setiap *notebook* tahap 2 dijalankan.

**Catatan 21 Nov 2026:** lima tabel (`t2_tabel_distribusi_stasiun`, `t2_tabel_ffill`, `t2_tabel_nilai_hilang`, `t2_tabel_ringkas_stasiun`, `t4_tabel_baseline`) dibuat dari jalan penuh *notebook* desain 9/3. `t2_tabel_ffill.csv` bergeser kecil pada HGB bila dijalankan di Colab. `t2_tabel_transfer.csv` (RMSE model Tiantan di stasiun lain) adalah sisa pilot dan tidak dibuat lagi oleh *notebook* 9/3.
