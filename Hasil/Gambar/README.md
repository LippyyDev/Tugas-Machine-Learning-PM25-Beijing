# Gambar

Sebelas gambar: satu diagram pembagian data (`t3_`), sembilan EDA tahap 2 (isi saat ini masih hasil pilot data latih Tiantan, kecuali nomor 08 dan 09 yang membandingkan stasiun; *notebook* 9/3 memakai 9 stasiun latih digabung dan menimpa gambar ini saat dijalankan). Awalan `t2_` menandai tahap 2, `t3_` tahap 3 (diagram dibuat dengan skrip `matplotlib`, bukan keluaran *notebook*), dan `t4_` tahap 4, nomor mengikuti urutan di *notebook*.

| Berkas | Isi |
|---|---|
| `t2_01_sebaran_pm25.png` | Sebaran PM2.5 |
| `t2_02_deret_waktu_harian.png` | Deret waktu harian |
| `t2_03_pola_jam_bulan.png` | Pola menurut jam dan bulan |
| `t2_04_nilai_hilang_per_kolom.png` | Nilai hilang per kolom |
| `t2_05_panjang_celah.png` | Panjang celah nilai hilang |
| `t2_06_korelasi_dengan_besok.png` | Korelasi tiap variabel jam *t* dengan PM2.5 jam *t*+24 |
| `t2_07_autokorelasi.png` | Autokorelasi PM2.5 |
| `t2_08_rata_rata_per_stasiun.png` | Rata-rata PM2.5 per stasiun |
| `t2_09_bulanan_antarstasiun.png` | Rata-rata bulanan antarstasiun |
| `t3_pembagian_data.png` | Diagram pembagian data: 9 stasiun latih, 3 stasiun ditahan, uji 20% periode terakhir |
| `t4_01_baseline_rmse_per_fold.png` | RMSE *naive forecast* dan regresi linear di tiap *fold* validasi data latih |
