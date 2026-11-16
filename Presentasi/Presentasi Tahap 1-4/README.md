# Presentasi Tahap 1 sampai 4

Slide web 6 halaman untuk progres Tugas Proyek Individu Pembelajaran Mesin: peramalan PM2.5 Beijing 24 jam ke depan dengan validasi berurutan waktu. Penyaji: Muhammad Alif Qadri. Rencana durasi 10 menit. Sumber isi: `Laporan/Penjelasan Proyek dan Alur Tahapan.md`.

## Cara pakai

Buka `INDEX.html` (daftar slide dan pratinjau) atau langsung `SLIDE1.html`. Slide memuat font dari Google Fonts dengan font cadangan sistem, jadi tetap terbaca tanpa internet.

| Aksi | Fungsi |
|---|---|
| Panah kiri atau kanan, Spasi, PageUp atau PageDown, klik tepi kiri atau kanan layar | Mundur atau maju |
| Kursor ke bawah layar | Kotak navigasi |
| `R` / `F` / `T` / `I` | Reset animasi / layar penuh / mode terang atau gelap / ke `INDEX.html` |
| `?step=N` di akhir alamat | Langsung ke langkah N (mulai dari 0) |

Maju di langkah terakhir pindah ke slide berikutnya, mundur di langkah pertama ke slide sebelumnya. Panggung tetap 1920 × 1080 dan diskalakan otomatis. Tema dan transisi tirai ada di `ASET/tema.css` dan `ASET/tema.js`. Aturan desain dan asal angka ada di `DESIGN.md`. PDF satu halaman per slide (langkah terakhir tiap slide): `Presentasi_Slide.pdf`.

## Isi per slide

| No | Slide | Waktu | Langkah | Isi utama | Sumber di Penjelasan Proyek |
|---|---|---|---|---|---|
| 1 | Judul | 0,5 mnt | 1 | Judul, tiga tantangan wajib, penyaji, NIM | |
| 2 | Tahap 1: rumusan masalah dan metrik | 1,5 | 7 | Mengalir dari PM2.5 dan deret waktu, studi kasus warga, yang diramal (jam t+24), rumusan satu kalimat, RMSE dan MAE (contoh sederhana lalu data nyata), tiga tantangan | Tahap 1 |
| 3 | Tahap 2: eksplorasi dan praproses | 2,5 | 6 | 12 × 35.064 = 420.768 baris, satu baris latihan dengan 29 fitur, aturan fitur (aman atau bocor), EDA, nilai hilang, alur praproses | Tahap 2 |
| 4 | Tahap 3: skema validasi | 2,5 | 6 | Berurutan lawan acak, lima lipatan, jarak aman 24 jam, praproses di dalam *pipeline*, 9 stasiun latih dan 3 asing, yang dicegah dan yang diakui | Tahap 3 |
| 5 | Tahap 4: *baseline* | 1,5 | 4 | *Naive forecast*, RMSE 86,82 ± 24,70 per lipatan, RMSE dan MAE, cara membaca hasil model nanti | Tahap 4 |
| 6 | Rencana dan kendala | 1,5 | 4 | Peta jalan 7 tahap, rencana tahap 5 sampai 7 dan gerbang data uji, lima kendala, pertanyaan untuk dosen | Tahap 5 sampai 7, bagian kelemahan |

Total 10 menit.

## Hal yang perlu dicek sebelum tampil

* Slide 2 kini 7 langkah (sebelumnya 5), jadi mungkin butuh lebih dari 1,5 menit. Sesuaikan jatah waktu atau pangkas langkah saat latihan.
* Panduan dosen membatasi slide progres Pertemuan 13 hingga 5 slide. Presentasi ini 6 halaman karena memakai satu slide judul. Konfirmasikan apakah slide judul dihitung.
* Desain 9 stasiun latih dan 3 stasiun asing adalah keputusan penulis (16 Nov 2026) dan belum dikonfirmasi dosen. Slide 4 dan 6 menandainya.
* Tiga pertanyaan di slide 6 (Fig. 25) adalah usulan penulis presentasi, bukan ketentuan dosen.
* Nama dosen tidak dicantumkan karena belum tertulis di sumber.
