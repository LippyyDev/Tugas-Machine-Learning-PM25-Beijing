# Penjelasan Proyek dan Alur Tahapan

Ringkasan versi mudah dibaca. Angka diambil dari hasil eksekusi *notebook* pada data latih. Data uji belum pernah dibuka.

## 1. Topik dan studi kasus

**Meramalkan konsentrasi PM2.5 di Beijing, 24 jam ke depan.**

PM2.5 adalah partikel debu sangat halus (diameter 2,5 mikrometer atau kurang) yang bisa masuk ke paru-paru. Semakin tinggi konsentrasinya, semakin berbahaya bagi kesehatan.

Jenis tugasnya adalah **regresi deret waktu**: model menebak sebuah angka (PM2.5) dari data yang urut menurut waktu.

### Studi kasus (skenario ilustrasi)

Bayangkan seorang warga Beijing pada pukul 10.00 yang ingin tahu apakah besok pukul 10.00 aman untuk berolahraga di luar ruangan atau mengantar anak ke sekolah dengan berjalan kaki. Ia tidak butuh tahu PM2.5 sekarang, karena itu bisa dilihat di aplikasi. Ia butuh perkiraan untuk besok, supaya punya waktu menyiapkan masker atau mengubah rencana.

Dari skenario ini kita tahu apa yang harus dibuat: sebuah model yang pada pukul 10.00 hari ini menebak PM2.5 pada pukul 10.00 besok, yaitu 24 jam ke depan.

Agar model bisa belajar menebak, ia butuh contoh dari masa lalu. Setiap contoh berisi kondisi udara dan cuaca pada satu jam, beserta PM2.5 yang terukur 24 jam sesudahnya. Semakin banyak dan semakin beragam contohnya, semakin baik model belajar pola, misalnya kapan polusi cenderung naik. Contoh seperti itu tersedia di dataset berikut.

## 2. Dataset

**Beijing Multi-Site Air Quality** dari UCI (https://archive.ics.uci.edu/dataset/501).

12 berkas CSV, satu per stasiun pemantau udara di Beijing. Satu baris adalah satu jam pengukuran, dari 1 Maret 2013 sampai 28 Februari 2017. Total 420.768 baris (12 stasiun × 35.064 jam), dengan 18 kolom yang sama di tiap berkas.

| Kelompok | Kolom | Arti |
|---|---|---|
| Waktu dan tempat | `No`, `year`, `month`, `day`, `hour`, `station` | Nomor baris, tahun, bulan, tanggal, jam, dan nama stasiun |
| Polutan | `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3` | Konsentrasi partikel dan gas di udara. `PM2.5` adalah yang diramal |
| Cuaca | `TEMP`, `PRES`, `DEWP`, `RAIN`, `WSPM`, `wd` | Suhu, tekanan, titik embun, hujan, kecepatan angin, dan arah angin (16 kategori teks) |

Nilai kosong ditandai `NA`. `PM2.5` kosong pada 2,08% baris, dan kolom lain 0,08% sampai 4,92%. Satuan mengikuti dokumentasi UCI (belum dicek ulang di halaman UCI).

**Peran kolom di proyek:** target adalah `PM2.5` pada jam t+24 (nilai `PM2.5` yang digeser 24 jam). Fitur berasal dari polutan dan cuaca pada jam t, riwayat `PM2.5`, dan kalender dari bulan, hari, dan jam. Kolom `No` tidak dipakai.

### Stasiun latih dan stasiun asing

![Pembagian data: 9 stasiun latih, 3 stasiun asing, uji 20% periode terakhir](../Hasil/Gambar/t2_02_pembagian_data.png)

Data mencakup 2013-03-01 sampai 2017-02-28. Gambar dan tabel berikut membagi 9 stasiun latih dan 3 stasiun asing menurut waktu: 80% awal adalah sebelum 2016-05-12 19:00, 20% akhir mulai 2016-05-12 19:00, dengan batas waktu yang sama untuk semua stasiun.

| Kotak | Isi | Porsi baris | Peran |
|---|---|---|---|
| 9 stasiun latih, 80% awal | LATIH | 60% | Melatih model, memilih model, dan *tuning* (`TimeSeriesSplit`, 5 *fold*, jarak aman 24 jam) |
| 9 stasiun latih, 20% akhir | UJI | 15% | Menguji masa depan di stasiun yang ikut dilatih |
| 3 stasiun asing, 80% awal | TIDAK DIPAKAI | 20% | Sengaja dibuang supaya model belum pernah melihat 3 stasiun ini sebelum diuji |
| 3 stasiun asing, 20% akhir | UJI | 5% | Menguji stasiun yang tidak ikut dilatih, sekaligus masa depan |

Dari 12 stasiun, **9 dipakai untuk melatih model** dan **3 asing**: model tidak pernah melihat data 3 stasiun itu. Data waktu dibagi sama untuk semua stasiun: 80% awal untuk latih dan 20% akhir untuk uji. Ini keputusan penulis (16 Nov 2026), belum dikonfirmasi dosen. Aturan dosen hanya menetapkan uji = 20% periode terakhir dan adanya uji di stasiun lain.

Uji akhir dilakukan pada 20% periode terakhir dari semua 12 stasiun, dilaporkan terpisah: (1) 9 stasiun latih, untuk melihat apakah model bagus meramal masa depan, dan (2) 3 stasiun asing, untuk melihat apakah model masih bagus di stasiun yang belum pernah dilihat. Selisih galat keduanya menunjukkan pergeseran distribusi. Tiga stasiun asing dipilih dengan aturan: satu yang jauh, satu sedang, dan satu dekat dari stasiun lain berdasarkan data periode latih saja. Hasilnya Dingling, Wanliu, dan Shunyi, yang sudah ditetapkan LIP (16 Nov 2026). Tiantan dan Dingling dipakai pada tahap awal sebagai percobaan (pilot), dan hasilnya dihitung ulang untuk desain ini.

Pembagian murni per stasiun pada seluruh periode tidak dipakai karena jam yang sama muncul di data latih dan uji. PM2.5 antar stasiun saling berkaitan pada jam yang sama (korelasi median 0,89), sehingga model bisa seolah-olah "mengintip" jawabannya.

## 3. Rumusan masalah

> Model ini membantu warga dan otoritas kesehatan lingkungan memutuskan pembatasan paparan, dengan memprediksi PM2.5 24 jam ke depan dari riwayat PM2.5, polutan lain, dan cuaca sampai jam prediksi. Kesalahan paling mahal adalah galat besar, terutama ramalan yang terlalu rendah saat polusi tinggi, sehingga metrik utama adalah RMSE.

**RMSE** adalah ukuran rata-rata seberapa jauh tebakan dari kenyataan, dengan kesalahan besar dihukum lebih berat. Cocok di sini karena meleset jauh saat polusi tinggi paling merugikan. MAE dipakai sebagai pendamping.

Tiga tantangan wajib dari dosen:

1. **Nilai hilang pada sensor.** Data yang kosong tidak boleh diisi dengan nilai dari jam sesudahnya.
2. **Validasi berurutan waktu.** Data tidak boleh diacak, karena model hanya boleh belajar dari masa lalu untuk menebak masa depan.
3. **Uji di stasiun lain.** Model dari satu stasiun dicoba di stasiun berbeda untuk melihat apakah kinerjanya turun (pergeseran distribusi).

## 4. Tujuan

1. Membangun model peramalan PM2.5 24 jam ke depan yang dievaluasi dengan **jujur dan bebas kebocoran data**.
2. Mengukur seberapa jauh model lebih baik dari tebakan paling sederhana, yaitu menganggap PM2.5 besok sama dengan PM2.5 sekarang (*baseline*).
3. Menguji apakah model tetap andal di stasiun lain.
4. Menganalisis kapan dan mengapa model salah, termasuk siapa yang dirugikan.

Yang dinilai dosen bukan skor tertinggi. Model sederhana yang dievaluasi dengan benar lebih berharga daripada model rumit yang skornya bagus karena bocor.

*Kebocoran data* berarti informasi dari data uji ikut terlihat oleh model saat belajar, sehingga skor tampak lebih bagus daripada kenyataannya. Seluruh rancangan tahap 1 sampai 4 dibuat untuk mencegah hal ini.

## 5. Alur dari tahap ke tahap

```
Tahap 1          Tahap 2           Tahap 3            Tahap 4
Rumusan    →    Eksplorasi   →    Cara menguji  →    Model acuan
masalah         dan rapikan       model              (baseline)
                data              (validasi)
                                                         │
                                          Pertemuan 13 (cek bersama dosen)
                                                         │
Tahap 5          Tahap 6           Tahap 7               ↓
Model       →    Evaluasi     →    Analisis kesalahan
lanjutan         akhir pada        dan etika
dan tuning       data uji
```

Urutannya penting. Cara menguji model (tahap 3) ditetapkan **sebelum** model dibangun, supaya hasil model tidak bisa mengubah cara pengujiannya.

### Tahap 1. Rumusan masalah dan metrik

Tahap 1 dikerjakan sebelum membuka data. Panduan meminta tiga pertanyaan dijawab tertulis (siapa pemakainya, keputusan apa yang diambil, kesalahan mana yang paling merugikan). Di sini ditambah dua baris: apa yang diramal dan bagaimana mengukurnya.

| Pertanyaan | Jawaban di proyek ini |
|---|---|
| Apa yang diramal? | PM2.5 pada 24 jam ke depan (jam t+24) di stasiun pemantau Beijing. Model dilatih dari 9 stasiun dan dicoba di 3 stasiun asing untuk melihat apakah berlaku di tempat lain |
| Untuk siapa? | Warga dan otoritas kesehatan lingkungan |
| Keputusan apa yang diambil dari ramalan? | Membatasi paparan, misalnya aktivitas di luar ruangan dan pemakaian masker |
| Kesalahan mana yang paling merugikan? | Galat besar, terutama ramalan yang terlalu rendah saat polusi tinggi |
| Bagaimana mengukurnya? | **RMSE** sebagai metrik utama, karena menghukum galat besar lebih berat. MAE sebagai pendamping |

### Tahap 2. Eksplorasi dan praproses

**Tujuan:** mengubah data mentah menjadi tabel latihan yang siap dibaca model. Setiap baris tabel berisi dua hal: **fitur** (yang sudah diketahui) dan **target** (yang harus ditebak).

**Contoh satu baris.** Anggap sekarang Senin pukul 10.00 (disebut jam t).

- Fitur: semua yang sudah terukur sampai saat ini, misalnya PM2.5 pagi ini, PM10, suhu, angin, dan PM2.5 kemarin.
- Target: PM2.5 pada Selasa pukul 10.00 (jam t+24), yang belum terjadi.

Model belajar dari banyak baris seperti ini: dari fitur pada jam t, tebak target 24 jam kemudian.

**Aturan terpenting: fitur tidak boleh memakai data sesudah jam t.** Saat ramalan dibuat di dunia nyata, data sesudah jam t memang belum ada. Jika sebuah fitur memakainya, skor model terlihat bagus tetapi model itu tidak bisa dipakai sungguhan. Inilah yang disebut *kebocoran data*.

#### Isi tabel: 29 fitur

| Kelompok | Isi | Jumlah | Mengapa dipakai |
|---|---|---|---|
| Kondisi pada jam t | PM2.5, PM10, SO2, NO2, CO, O3, suhu, tekanan, titik embun, hujan, kecepatan angin | 11 | Keadaan udara dan cuaca saat ini |
| Riwayat PM2.5 (*lag*) | PM2.5 pada 1, 2, 3, 6, 12, 24, dan 48 jam sebelum jam t | 7 | PM2.5 cenderung mirip dengan beberapa jam atau hari sebelumnya |
| Rata-rata bergulir | rata-rata PM2.5 selama 6, 24, dan 72 jam terakhir (jam t ikut dihitung, jam sesudahnya tidak) | 3 | Gambaran tren jangka pendek sampai menengah |
| Arah angin | diubah menjadi sinus dan kosinus | 2 | Arah berbentuk lingkaran (0 derajat sama dengan 360 derajat), jadi dipecah menjadi dua angka agar nilai yang berdekatan tetap tampak dekat |
| Kalender | jam, hari, dan bulan, masing-masing sebagai sinus dan kosinus | 6 | Pola yang berulang. Dengan sinus dan kosinus, pukul 23.00 tercatat dekat dengan pukul 00.00 |

Tabel ini dibuat dari stasiun Tiantan pada tahap pilot. Pada desain 9 stasiun latih dan 3 stasiun asing (bagian 2), fitur yang sama dibuat untuk setiap stasiun.

#### Langkah yang dikerjakan

1. **Mengenali data (EDA).** Temuan pada data latih Tiantan:
   - PM2.5 miring ke kanan: kebanyakan jam bernilai rendah, tetapi ada episode polusi sangat tinggi. Episode ini menghasilkan galat besar sehingga akan mendominasi RMSE.
   - Rata-rata tertinggi terjadi di bulan Desember dan pada pukul 23.00.
   - PM2.5 kosong pada 2,08% jam, dalam 313 celah. Celah terpanjang 24 jam.
   - Nilai ekstrem 999 dipertahankan.
2. **Menyisihkan data uji sejak awal.** Data mulai 12 Mei 2016 dipisahkan sebelum eksplorasi dan tidak dibuka.
3. **Membuat fitur dan target** seperti tabel di atas.
4. **Membuang baris latih yang targetnya masuk periode uji.** Contoh: baris pukul 20.00 tanggal 11 Mei 2016 punya target pukul 20.00 tanggal 12 Mei, padahal batas uji adalah 12 Mei pukul 19.00. Baris seperti ini (24 jam terakhir sebelum batas) dibuang supaya data latih tidak mengintip periode uji.
5. **Menangani nilai hilang.**
   - Baris yang targetnya kosong dibuang, karena tidak ada jawaban untuk dipelajari.
   - Fitur yang kosong diisi median, dan median itu dihitung dari data latih saja.
   - Nilai dari jam sesudah celah tidak dipakai untuk mengisi, karena itu sama dengan mengintip masa depan.
6. **Menjustifikasi dua pilihan.**
   - *Forward fill*: pengisian celah sampai beberapa batas jam dibandingkan, dan hasilnya tidak berbeda nyata (selisihnya sebanding dengan derau antar pengulangan). Maka dipilih cara paling sederhana, yaitu tanpa *forward fill*.
   - Stasiun uji: pada pilot, Dingling dipilih karena distribusi PM2.5-nya paling berbeda dari Tiantan. Namun uji pada data latih tidak membuktikan Dingling paling sulit diramal. Pada desain 9 stasiun latih dan 3 stasiun asing (16 Nov 2026), peran ini diganti tiga stasiun asing, yaitu Dingling, Wanliu, dan Shunyi (ditetapkan LIP, dasarnya aturan di *notebook* 02.2).

**Hasil (pilot Tiantan):** 27.443 baris latih dengan 29 fitur, dan 6.896 baris uji yang disimpan tanpa dibuka. Angka untuk desain 9/3 baru ada setelah *notebook* dijalankan ulang.

### Tahap 3. Skema validasi

Menetapkan cara menguji model supaya skornya jujur.
- Data diurutkan menurut waktu. **20% terakhir disimpan sebagai data uji** (mulai 12 Mei 2016) dan hanya dibuka satu kali di akhir.
- Sisanya (80%) dipakai untuk memilih model dengan `TimeSeriesSplit` 5 lipatan, dengan jarak aman 24 jam. Target sebuah baris latih adalah PM2.5 24 jam sesudahnya, jadi tanpa jarak, target baris latih terakhir bisa jatuh di periode validasi. Jarak 24 jam mencegah hal itu.
- Pengisian nilai hilang dan penskalaan dihitung dari data latih saja pada setiap lipatan, tidak dari data validasi atau data uji. Ini dilakukan dengan menaruhnya di dalam *pipeline*.
- Kelemahan yang diakui: hanya 5 lipatan, simpangan baku antar lipatan besar, dan statistik ringkas periode uji pernah dilihat (7 dan 15 Nov 2026), tetapi tidak dipakai untuk memilih fitur, model, atau pengaturan.

### Tahap 4. *Baseline*

Hasil acuan. Model lanjutan baru dianggap berguna jika RMSE-nya lebih kecil dari angka ini.

| Model | RMSE (rata-rata ± sd antar lipatan) |
|---|---|
| *Naive forecast* (tebak PM2.5 besok sama dengan sekarang) | 86,97 ± 25,19 |
| Regresi linear (pembanding tambahan) | 73,38 ± 19,73 |

Regresi linear lebih baik dari *naive* di kelima lipatan. Angka ini hasil pada data latih, bukan data uji.

### Tahap 5. Model lanjutan dan *tuning*

Minimal dua model yang lebih kuat (misalnya *random forest* dan *gradient boosting*), disetel dengan validasi silang pada data latih. Data uji tetap tidak disentuh.

### Tahap 6. Evaluasi dan diagnosis

Memeriksa apakah model terlalu sederhana (*underfitting*) atau terlalu menghafal (*overfitting*) dengan *learning curve*. Setelah model final dipilih, **data uji dibuka satu kali**, untuk 9 stasiun latih dan 3 stasiun asing. Jika skornya jauh lebih buruk dari validasi, model tidak disetel ulang. Selisihnya dilaporkan dan dianalisis.

### Tahap 7. Analisis kesalahan dan etika

Mencari di mana model paling sering salah (jam, musim, stasiun, rentang konsentrasi), fitur mana yang paling berpengaruh, dan siapa yang dirugikan jika ramalan terlalu rendah. Model dipakai sebagai alat bantu peringatan, bukan pengambil keputusan otomatis.
