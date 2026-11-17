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
| 1 | Judul | 0,5 mnt | 1 | Judul "Peramalan PM2.5 Beijing 24 Jam ke Depan dengan Validasi Berurutan Waktu", tiga tantangan wajib, penyaji, NIM, tiga gambar meme (kakek di depan, emoji jempol dan *social credit* di belakangnya, tidak sejajar) dengan balon ucapan kecil | |
| 2 | Tahap 1: rumusan masalah dan metrik | 1,5 | 7 | Mengalir dari PM2.5 dan deret waktu, studi kasus warga, yang diramal (jam t+24), rumusan satu kalimat, RMSE dan MAE (contoh sederhana lalu data nyata), tiga tantangan | Tahap 1 |
| 3 | Tahap 2: eksplorasi dan praproses | 2,5 | 6 | 12 × 35.064 = 420.768 baris, satu baris latihan dengan 29 fitur, aturan fitur (aman atau bocor), EDA, nilai hilang, alur praproses | Tahap 2 |
| 4 | Tahap 3: skema validasi | 2,5 | 6 | Berurutan lawan acak, lima lipatan, jarak aman 24 jam, praproses di dalam *pipeline*, 9 stasiun latih dan 3 asing, yang dicegah dan yang diakui | Tahap 3 |
| 5 | Tahap 4: *baseline* | 1,5 | 4 | *Naive forecast*, RMSE 86,82 ± 24,70 per lipatan, RMSE dan MAE, cara membaca hasil model nanti | Tahap 4 |
| 6 | Ringkasan hasil Tahap 1 sampai 4 | 1,5 | 5 | Satu langkah per tahap (alasan memilih RMSE, 246.798 baris latih dan 82.151 baris uji dengan 29 fitur, lima lipatan dengan jeda 24 jam, RMSE *naive* per lipatan) dan satu petak ringkasan yang bisa diklik. Tanpa rencana tahap 5 sampai 7 | Tahap 1 sampai 4, hasil eksekusi *notebook* |

Total 10 menit.

## Hal yang perlu dicek sebelum tampil

* Slide 2 kini 7 langkah (sebelumnya 5), jadi mungkin butuh lebih dari 1,5 menit. Sesuaikan jatah waktu atau pangkas langkah saat latihan.
* Panduan dosen membatasi slide progres Pertemuan 13 hingga 5 slide. Presentasi ini 6 halaman karena memakai satu slide judul. Konfirmasikan apakah slide judul dihitung.
* Desain 9 stasiun latih dan 3 stasiun asing adalah keputusan penulis (16 Nov 2026) dan belum dikonfirmasi dosen. Penanda "usulan penulis, belum dikonfirmasi dosen" di slide 4 dan 6 dihapus atas permintaan penulis (17 Nov 2026), jadi statusnya tidak lagi terlihat di slide dan perlu disampaikan lisan atau di laporan.
* Slide 6 hanya merangkum hasil Tahap 1 sampai 4 (permintaan penulis 17 Nov 2026): rencana tahap 5 sampai 7, daftar kendala, dan tiga pertanyaan untuk dosen dihapus dari slide. Pengakuan bahwa statistik ringkas periode uji pernah terlihat tetap ada di Fig. 26.
* Slide 6 kini 5 langkah dalam jatah 1,5 menit, sama seperti slide 2 yang perlu dilatih waktunya.
* Nama dosen tidak dicantumkan karena belum tertulis di sumber.
