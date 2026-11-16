# DESIGN.md: Panduan Gaya dan Asal Angka Presentasi Tahap 1 sampai 4

Gaya mengikuti presentasi Tugas Besar Algoritma Komputasi (repo `LippyyDev/Tugas-Besar-Algoritma-Komputasi`, folder `PRESENTASI`): tema gelap bergaya Palantir, garis tipis, label mono kapital, satu warna aksen biru, satu warna pendamping kuning. Bila dokumen ini berbeda dengan kode, kode yang benar.

## 1. Prinsip

* Layar bukan tempat membaca. Teks sedikit, gambar yang menjelaskan, dan setiap gambar bisa disentuh (geser, klik, atau arahkan kursor).
* Satu langkah satu ide. Langkah bisa diulang dengan tombol Reset atau tombol `R`.
* Warna selalu bermakna (bagian 3).
* Semua angka berasal dari eksekusi kode (bagian 5). Angka yang hanya contoh diberi label **CONTOH HIPOTETIS** di gambar.
* Dugaan diberi kata "dugaan". Keputusan yang belum disetujui dosen diberi tanda [Usulan].
* Aturan tulis: Bahasa Indonesia, istilah asing miring, tanpa tanda pisah panjang, tanpa tanda hubung sebagai pemisah kalimat.

## 2. Struktur berkas

| Berkas | Fungsi |
|---|---|
| `SLIDE1.html` sampai `SLIDE6.html` | Satu slide satu berkas (HTML, CSS, JS sendiri) |
| `INDEX.html` | Daftar slide dengan pratinjau; daftar `SLIDES` berisi judul, menit, berkas |
| `ASET/` | `LOGO-UNHAS.png`, `tema.css`, `tema.js` (tema terang atau gelap dan transisi tirai) |
| `Skrip/bangun_data_slide.py` | Menghitung data yang ditampilkan, hanya dari data latih |
| `Skrip/data_slide.json` | Keluaran skrip di atas (kurva contoh, sebaran, per bulan, per jam, porsi galat) |
| `vercel.json` | Alamat pendek `/slide1` sampai `/slide6` bila di-*deploy* |
| `Presentasi_Slide.pdf` | Satu halaman per slide, langkah terakhir |

## 3. Token dan makna warna

| Token | Nilai | Makna di slide ini |
|---|---|---|
| `--bg` | `#050507` | latar |
| `--panel` | `#0a0b0f` | permukaan kartu dan dock |
| `--text` / `--body` / `--mute` | `#f1f2f6` / `#c4c7d4` / `#80849a` | teks utama / isi / label |
| `--accent` | `#7db4ff` | biru: data latih, ramalan *naive*, tahap yang sudah dikerjakan, aturan yang aman |
| `--accent-bright` | `#c4dcff` | biru terang: sorotan dan judul miring |
| `--amber` | `#ffc266` | kuning: data uji dan peringatan, kenyataan, galat (meleset), validasi musim dingin, kebocoran, hal yang butuh keputusan |
| abu | `#80849a` | tidak dipakai, belum dikerjakan, netral |

Huruf: Space Grotesk (isi dan judul) dan JetBrains Mono (label, angka, penanda). Tema terang dibuat dengan `filter: invert(1) hue-rotate(180deg)` pada `html`, jadi warna di dalam SVG tidak perlu dibuat dua versi.

## 4. Tata letak dan pola slide

Panggung 1920 × 1080. Kolom kiri berisi blok teks bertahap (yang aktif terang, dua sebelumnya redup, yang lebih lama disembunyikan). Kolom kanan berisi satu panel dengan judul gambar (`Fig. N`), angka bacaan di kanan atas, area gambar SVG 942 × 526, dan keterangan satu sampai dua baris di bawah. Langkah ditulis sebagai fungsi yang tidak bergantung urutan, supaya `?step=N` dan tombol mundur selalu menghasilkan tampilan yang sama.

## 5. Langkah per slide dan asal angka

| Slide | Langkah (Fig.) | Interaksi | Asal angka |
|---|---|---|---|
| 2 | 01 deret waktu PM2.5, studi kasus dan jam t ke t+24 (tiga langkah); 02 rumusan satu kalimat; 03 RMSE dan MAE pada contoh hipotetis; 04 siapa yang menentukan RMSE; 05 tiga tantangan | seret jam t, seret ujung batang galat, tombol skenario (Awal, Stabil, Meleset ekstrem) | Kurva contoh: `data_slide.json` (Tiantan, 336 jam dari 2013-11-11, data latih). Porsi 5% galat terbesar di Fig. 04: `porsi_galat` di berkas yang sama. Contoh di Fig. 03 hanya hitungan hipotetis (galat 10, 10, 10, dan satu galat yang bisa diseret; awal 100 memberi MAE 32,5 dan RMSE 50,7; skenario Stabil 25 ×4 memberi MAE 25,0 dan RMSE 25,0, skenario Meleset ekstrem 0, 0, 0, 100 memberi MAE 25,0 dan RMSE 50,0). Kartu MAE dan RMSE di Fig. 03 menampilkan rumus yang terisi angka batang dan ikut berubah saat diseret. Persegi di Fig. 03 berukuran sisi = 0,72 × galat (skala sendiri, terpisah dari skala batang), sehingga luasnya sebanding dengan galat kuadrat; arsiran kuning adalah selisih RMSE dan MAE |
| 3 | 06 dataset; 07 satu baris latihan; 08 aturan fitur; 09 EDA; 10 nilai hilang; 11 alur praproses | geser jam t, arahkan kursor ke lima kelompok pada batang 29 fitur (11, 7, 3, 2, 6) untuk menyorot bagian kurva yang terkait, sakelar aman atau bocor, tiga tab EDA | 420.768 baris, 29 fitur, 246.798 latih dan 82.151 uji dari notebook dan `data_slide.json`; PM2.5 kosong 2,16%, 1.730 celah (terpanjang 343 jam) dari notebook |
| 4 | 12 urut atau acak; 13 lima lipatan; 14 jarak aman; 15 *pipeline*; 16 stasiun; 17 dicegah dan diakui | sakelar, klik lipatan, geser jarak aman, sakelar salah atau benar, kursor di matriks stasiun | Tanggal lipatan di-*assert* terhadap notebook; batas uji 2016-05-12 19:00 (jam ke 28.051) |
| 5 | 18 tebakan *naive*; 19 RMSE tiap lipatan; 20 RMSE dan MAE; 21 membaca hasil model nanti | seret jam t, kursor di batang, seret penanda | RMSE *naive* 86,82 ± 24,70 (lipatan 101,7 / 62,2 / 103,6 / 57,7 / 108,8), MAE 59,39 ± 16,53 dari notebook; 5% galat terbesar menyumbang 48,7% jumlah kuadrat galat dan 22,1% galat mutlak, dihitung di `Skrip/bangun_data_slide.py` pada seluruh data latih (bukan per lipatan). Penanda di Fig. 21 adalah contoh hipotetis |
| 6 | 22 peta jalan; 23 rencana dan gerbang data uji; 24 kendala; 25 yang pasti dan yang ditanyakan | klik tahap, klik kartu, kursor di baris kendala dan petak angka | Isi tahap 5 sampai 7 dari Penjelasan Proyek; periode uji 7.013 jam (292 hari, sekitar 9,6 bulan) dihitung dari 35.064 dikurangi 28.051 |

## 6. Batas kejujuran isi

* Data uji tidak dipakai di slide mana pun. Skrip data hanya membaca baris sebelum 2016-05-12 19:00 dan men-*assert* batas itu.
* Musim tiap lipatan diturunkan dari tanggal validasi. Penjelasan bahwa simpangan baku besar karena beda musim adalah dugaan.
* Statistik ringkas periode uji pernah terlihat (7 dan 15 Nov 2026) dan tidak dipakai. Hal ini diakui di slide 4 dan 6.
* Aturan jarak aman sama dengan horizon belum punya sumber *peer review* yang terbaca. Slide 4 dan 6 menyebutnya.
* Tidak ada sitasi pustaka di slide. Bila nanti ditambahkan, ikuti Aturan Sitasi proyek dan verifikasi dulu.

## 7. Daftar periksa per slide

1. Tidak ada galat JavaScript di konsol.
2. Tidak ada elemen di bawah y = 1000 atau di kanan x = 1830 pada panggung 1920 × 1080.
3. Tiap langkah dicek dengan `?step=N` dalam tema gelap dan terang.
4. Maju di langkah terakhir dan mundur di langkah pertama berpindah slide dengan benar.
5. Angka di slide dicocokkan dengan keluaran notebook atau skrip, bukan diketik dari ingatan.
