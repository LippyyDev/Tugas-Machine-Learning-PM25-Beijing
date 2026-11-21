# Tabel

Dua belas tabel dibuat *notebook*: tiga dari EDA dan pemilihan stasiun uji (bagian 02), satu dari dasar keputusan *forward fill* (04.6), satu dari *baseline* tahap 4 (04.5), dan tujuh dari model lanjutan tahap 5 (bagian 05).

| Berkas | Isi |
|---|---|
| `t2_tabel_nilai_hilang.csv` | Persen nilai hilang per kolom (9 stasiun latih, data latih) |
| `t2_tabel_ringkas_stasiun.csv` | Rata-rata, median, dan persen hilang PM2.5 per stasiun (12 stasiun, sebelum batas uji), dengan kolom `kelompok` (latih atau uji) |
| `t2_tabel_distribusi_stasiun.csv` | Jarak distribusi PM2.5 tiap stasiun terhadap 11 stasiun lain (Wasserstein dan KS, sebelum batas uji), dasar memilih tiga stasiun uji |
| `t2_tabel_ffill.csv` | RMSE Ridge dan *HistGradientBoosting* untuk batas *forward fill* 0 sampai 24 jam (9 stasiun latih, data latih) |
| `t4_tabel_baseline.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive forecast* |
| `t5_tabel_model_lanjutan.csv` | RMSE dan MAE (rata-rata dan sd antar *fold*) *naive* dan enam konfigurasi model lanjutan, perbaikan RMSE terhadap *naive*, dan jumlah *fold* yang lebih baik dari *naive* |
| `t5_tabel_rmse_per_fold.csv` | RMSE tiap model di tiap *fold* validasi |
| `t5_tabel_selisih_vs_ridge.csv` | Selisih RMSE tiap model terhadap Ridge pada *fold* yang sama (rata-rata, sd selisih, jumlah *fold* lebih baik) |
| `t5_tabel_eksperimen_per_fold.csv` | RMSE dan MAE tiap *fold* untuk 53 eksperimen lanjutan (bagian 05.5): ablasi fitur, keluarga model, konfigurasi terbaik hasil *tuning*, rata-rata model, transformasi target, putaran 2 |
| `t5_tabel_eksperimen_ringkas.csv` | Ringkasan 53 eksperimen, diurutkan dari RMSE terendah: rata-rata dan sd, selisih berpasangan terhadap Ridge F1, jumlah *fold* lebih baik, perbaikan terhadap *naive* |
| `t5_tabel_tuning.csv` | Rata-rata dan sd RMSE 36 konfigurasi *tuning* acak (HGB dan *random forest* pada F2 dan F3) beserta hiperparameternya |
| `t5_tabel_tuning_putaran2.csv` | Rata-rata dan sd RMSE 9 konfigurasi putaran 2 (*random forest* yang diperluas dan *Extra Trees*, F3) |

Dibuat ulang setiap *notebook* tahap 2 dijalankan.

**Catatan 21 Nov 2026:** lima tabel (`t2_tabel_distribusi_stasiun`, `t2_tabel_ffill`, `t2_tabel_nilai_hilang`, `t2_tabel_ringkas_stasiun`, `t4_tabel_baseline`) dibuat dari jalan penuh *notebook* desain 9/3. `t2_tabel_ffill.csv` bergeser kecil pada HGB bila dijalankan di Colab. `t2_tabel_transfer.csv` (RMSE model Tiantan di stasiun lain) adalah sisa pilot dan tidak dibuat lagi oleh *notebook* 9/3.
