# Gambar

Tujuh gambar: enam grafik praproses dari *notebook* tahap 2 (`t2_`) dan satu diagram pembagian data (`t3_`, dibuat dengan skrip `matplotlib`, bukan keluaran *notebook*). Keenam grafik `t2_` berasal dari eksekusi *notebook* 9/3 pada 16 Nov 2026 (9 stasiun latih digabung, hanya data latih) dan ditimpa setiap *notebook* dijalankan. Nomor mengikuti urutan di *notebook*. Setiap grafik berjudul berupa pertanyaan atau pernyataan yang menyebut data latih, dengan satu kalimat cara membaca di bawah judul.

Grafik deret waktu harian, rata-rata per stasiun, bulanan antarstasiun, dan RMSE *baseline* per *fold* (`t2_02`, `t2_08`, `t2_09`, `t4_01`) tidak lagi dibuat karena tidak mendukung keputusan praproses; angka *baseline* tetap ada di tabel `Hasil/Tabel/`.

| Berkas | Isi | Keputusan praproses yang didukung |
|---|---|---|
| `t2_01_sebaran_pm25.png` | Sebaran PM2.5 per jam, dengan median dan rata-rata | Nilai ekstrem dipertahankan, tidak dibuang |
| `t2_03_pola_jam_bulan.png` | Pola PM2.5 menurut jam dan bulan | Fitur jam dan bulan |
| `t2_04_nilai_hilang_per_kolom.png` | Persen nilai hilang per kolom | Penanganan nilai hilang |
| `t2_05_panjang_celah.png` | Lama data PM2.5 kosong berturut-turut | Tanpa *forward fill* dan batas celah |
| `t2_06_korelasi_dengan_besok.png` | Korelasi tiap variabel jam *t* dengan PM2.5 jam *t*+24 | Pemilihan variabel masukan |
| `t2_07_autokorelasi.png` | Korelasi PM2.5 dengan PM2.5 beberapa jam sebelumnya | Fitur *lag* |
| `t3_pembagian_data.png` | Diagram pembagian data: 9 stasiun latih, 3 stasiun asing, uji 20% periode terakhir | Skema pembagian data |
