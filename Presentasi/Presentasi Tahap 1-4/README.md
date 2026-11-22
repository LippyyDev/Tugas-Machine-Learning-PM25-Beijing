# Presentasi Tahap 1 sampai 5

Slide web 6 halaman untuk progres Tahap 1 sampai 5 Tugas Proyek Individu Pembelajaran Mesin: peramalan PM2.5 Beijing 24 jam ke depan dengan validasi berurutan waktu. Penyaji: Muhammad Alif Qadri. Rencana durasi 10,5 menit. Sumber isi: `Laporan/Penjelasan Proyek dan Alur Tahapan.md`.

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
| 1 | Judul | 0,5 mnt | 1 | Judul "Peramalan PM2.5 Beijing 24 Jam ke Depan", satu baris teks kecil lima tahap (rumusan masalah, eksplorasi dan praproses, skema validasi, *baseline*, model lanjutan) tanpa kotak, penyaji, NIM, gambar garis SVG gerbang Tiananmen (ikon Beijing) lengkap dengan awan, pepohonan, tembok samping, tugu *huabiao*, dan perbukitan, memudar di bagian dasar, samar di belakang animasi *time series*, tiga gambar meme (kakek di depan, emoji jempol dan *social credit* di belakangnya, tidak sejajar) dengan balon ucapan kecil | |
| 2 | Tahap 1: rumusan masalah dan metrik | 1,5 | 7 | Mengalir dari PM2.5 dan deret waktu, studi kasus warga, yang diprediksi (jam t+24), rumusan satu kalimat, RMSE dan MAE (contoh sederhana lalu data nyata), tiga tantangan | Tahap 1 |
| 3 | Tahap 2: eksplorasi dan praproses | 2,5 | 6 | 12 × 35.064 = 420.768 baris, satu baris latihan dengan 29 fitur, aturan fitur (aman atau bocor), EDA, nilai hilang, alur praproses | Tahap 2 |
| 4 | Tahap 3: skema validasi | 2,5 | 6 | Berurutan lawan acak, lima *fold*, *gap* 24 jam, praproses di dalam *pipeline*, 9 stasiun latih dan 3 stasiun uji, yang dicegah dan yang diakui | Tahap 3 |
| 5 | Tahap 4: *baseline* | 1,5 | 4 | *Naive forecast*, RMSE 86,82 ± 24,70 per *fold*, RMSE dan MAE, cara membaca hasil model nanti | Tahap 4 |
| 6 | Tahap 5: model lanjutan | 2 | 5 | Dua model linear (Ridge utama, Elastic Net pembanding, 29 fitur sama), aturan uji sama dengan *naive* dan satu perbedaan yang diakui, kurva RMSE terhadap *alpha* (20 pengaturan, hampir datar), RMSE per *fold* (86,82 untuk *naive*, 72,83 Ridge, 72,26 Elastic Net, menang di 5 dari 5 *fold*), selisih kedua model 0,57 yang jauh di bawah sebaran antar *fold* sehingga setara. Slide ringkasan lama diganti | Tahap 5, hasil eksekusi *notebook* bagian 05 |

Total 10,5 menit.

## Hal yang perlu dicek sebelum tampil

* Slide 2 kini 7 langkah (sebelumnya 5), jadi mungkin butuh lebih dari 1,5 menit. Sesuaikan jatah waktu atau pangkas langkah saat latihan.
* Panduan dosen membatasi slide progres Pertemuan 13 hingga 5 slide. Presentasi ini 6 halaman karena memakai satu slide judul. Konfirmasikan apakah slide judul dihitung.
* Desain 9 stasiun latih dan 3 stasiun uji adalah keputusan penulis (16 Nov 2026) dan belum dikonfirmasi dosen. Penanda "usulan penulis, belum dikonfirmasi dosen" di slide 4 dan 6 dihapus atas permintaan penulis (17 Nov 2026), jadi statusnya tidak lagi terlihat di slide dan perlu disampaikan lisan atau di laporan.
* Slide ringkasan Tahap 1 sampai 4 sudah diganti slide Tahap 5 atas permintaan penulis (22 Nov 2026). Slide 6 tidak lagi merangkum Tahap 1 sampai 4 dan tidak memuat rencana tahap 6 dan 7. Pengakuan bahwa statistik ringkas periode uji pernah terlihat tetap ada di slide 4.
* Slide 6 berisi 5 langkah dalam jatah 2 menit, jadi latih waktunya. Total durasi kini 10,5 menit.
* Slide 6 menyebut Ridge dipilih karena lebih sederhana. Model belum dibekukan dan belum final, dan aturan pemilihan di protokol masih menunggu persetujuan.
* Nama folder `Presentasi Tahap 1-4` tidak diubah supaya tautan lama tetap berlaku, walaupun isinya sampai Tahap 5.
* Nama dosen tidak dicantumkan karena belum tertulis di sumber.
