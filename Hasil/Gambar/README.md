# Gambar

Sebelas grafik dari *notebook* (`Notebook/Tahap 2 EDA dan Praproses.ipynb`), satu untuk tiap langkah pekerjaan tahap 2 sampai 5. Awalan `t2_`, `t3_`, `t4_`, `t5_` menandai tahap, nomor mengikuti urutan di *notebook*. Gambar dibuat dari eksekusi *notebook* 9/3 pada 16 Nov 2026 dan ditimpa setiap *notebook* dijalankan.

**Data uji tidak divisualisasikan nilainya.** Grafik yang menyebut data uji (`t2_01`, `t2_02`, `t3_01`) hanya memakai waktu dan jumlah baris. Nilai PM2.5 data uji dibuka satu kali di akhir proyek.

| Berkas | Langkah | Isi |
|---|---|---|
| `t2_01_jam_per_stasiun.png` | Muat data | Jumlah jam tercatat per stasiun (12 stasiun) |
| `t2_02_pembagian_data.png` | Sisihkan data uji | Pembagian latih, uji, dan stasiun uji, luas sebanding jumlah baris |
| `t2_03_jarak_stasiun_uji.png` | Pilih stasiun uji | Jarak Wasserstein PM2.5 tiap stasiun, tiga stasiun uji diberi warna |
| `t2_04_sebaran_pm25.png` | EDA data latih | Sebaran PM2.5 per jam dengan median dan rata-rata |
| `t2_05_nilai_hilang_per_kolom.png` | Praproses nilai hilang | Persen jam kosong per kolom |
| `t2_06_lama_nilai_hilang.png` | Praproses nilai hilang | Lama data PM2.5 kosong berturut-turut |
| `t3_01_fold_validasi.png` | Skema validasi | Lima *fold* `TimeSeriesSplit` dan posisi data uji |
| `t4_01_baseline_rmse_per_fold.png` | *Baseline* | RMSE *naive forecast* di tiap *fold* |
| `t4_02_pemeriksaan_desain.png` | Uji kebocoran | Ringkasan enam pemeriksaan desain 9/3 |
| `t5_01_rmse_model_lanjutan.png` | Model lanjutan | Rata-rata RMSE ± sd dan nilai tiap *fold* untuk *naive* dan enam konfigurasi model lanjutan (validasi silang, data uji tidak dipakai) |
| `t5_02_eksperimen_lanjutan.png` | Eksperimen lanjutan | Rata-rata RMSE ± sd dan nilai tiap *fold*: *naive*, Ridge F1, terbaik tanpa fitur lintas stasiun, dan terbaik dengan fitur lintas stasiun, dengan garis 70 |
