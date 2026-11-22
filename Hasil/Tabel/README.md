# Tabel

Beberapa tabel dibuat *notebook*: tiga dari EDA dan pemilihan stasiun uji (bagian 02), satu dari dasar keputusan *forward fill* (04.6), satu dari *baseline* tahap 4 (04.5), dan tabel dua model lanjutan serta *tuning* tahap 5 (bagian 05).

| Berkas | Isi |
|---|---|
| `t2_tabel_nilai_hilang.csv` | Persen nilai hilang per kolom (9 stasiun latih, data latih) |
| `t2_tabel_ringkas_stasiun.csv` | Rata-rata, median, dan persen hilang PM2.5 per stasiun (12 stasiun, sebelum batas uji), dengan kolom `kelompok` (latih atau uji) |
| `t2_tabel_distribusi_stasiun.csv` | Jarak distribusi PM2.5 tiap stasiun terhadap 11 stasiun lain (Wasserstein dan KS, sebelum batas uji), dasar memilih tiga stasiun uji |
| `t2_tabel_ffill.csv` | RMSE Ridge dan *HistGradientBoosting* untuk batas *forward fill* 0 sampai 24 jam (9 stasiun latih, data latih) |
| `t4_tabel_baseline.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive forecast* |
| `t5_tabel_dua_model.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive*, Ridge utama, dan Elastic Net pembanding, perbaikan terhadap *naive* (bagian 05.2) |
| `t5_tabel_dua_model_per_fold.csv` | RMSE tiap *fold* untuk *naive* dan kedua model (bagian 05.2) |
| `t5_tabel_tuning_linear.csv` | Ringkasan 20 konfigurasi *tuning* Ridge dan Elastic Net (bagian 05.7): RMSE dan MAE rata-rata dan sd, selisih berpasangan terhadap Ridge `alpha=1`, peringatan konvergensi |
| `t5_tabel_tuning_linear_per_fold.csv` | RMSE dan MAE tiap *fold* untuk 20 konfigurasi *tuning* linear |
| `t5_tabel_semua_eksperimen.csv` | 25 konfigurasi Tahap 5 dengan RMSE, MAE, sd, perbaikan terhadap *naive*, dan RMSE tiap *fold*. Sumber `Laporan/Tabel Hasil Percobaan Tahap 5.md` |

Dibuat ulang setiap *notebook* tahap 2 dijalankan.

**Catatan 21 Nov 2026:** lima tabel (`t2_tabel_distribusi_stasiun`, `t2_tabel_ffill`, `t2_tabel_nilai_hilang`, `t2_tabel_ringkas_stasiun`, `t4_tabel_baseline`) dibuat dari jalan penuh *notebook* desain 9/3. `t2_tabel_ffill.csv` bergeser kecil pada HGB bila dijalankan di Colab. `t2_tabel_transfer.csv` (RMSE model Tiantan di stasiun lain) adalah sisa pilot dan tidak dibuat lagi oleh *notebook* 9/3.
