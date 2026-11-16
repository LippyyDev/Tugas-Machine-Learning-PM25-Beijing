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

## 2. Dataset: kolom-kolomnya

**Beijing Multi-Site Air Quality** dari UCI (https://archive.ics.uci.edu/dataset/501).

Dataset ini berupa 12 berkas CSV, satu per stasiun pemantau udara di Beijing. Setiap baris adalah satu jam pengukuran. Total 420.768 baris (12 stasiun × 35.064 jam), dari 1 Maret 2013 pukul 00.00 sampai 28 Februari 2017 pukul 23.00. Setiap berkas punya 18 kolom yang sama.

### Kolom waktu dan tempat

| Kolom | Arti | Isi |
|---|---|---|
| `No` | Nomor urut baris dalam satu stasiun | 1 sampai 35.064 |
| `year` | Tahun | 2013 sampai 2017 |
| `month` | Bulan | 1 sampai 12 |
| `day` | Tanggal | 1 sampai 31 |
| `hour` | Jam | 0 sampai 23 |
| `station` | Nama stasiun | 12 nama, misalnya Tiantan dan Dingling |

Kolom `year`, `month`, `day`, dan `hour` digabung menjadi satu penanda waktu. Kolom `No` dan `station` tidak dipakai sebagai fitur.

### Kolom polutan udara

| Kolom | Arti | Rentang nilai | Kosong |
|---|---|---|---|
| `PM2.5` | Partikel halus 2,5 mikrometer atau kurang. **Ini yang diramal** | 2 sampai 999 | 2,08% |
| `PM10` | Partikel 10 mikrometer atau kurang | 2 sampai 999 | 1,53% |
| `SO2` | Sulfur dioksida | 0,3 sampai 500 | 2,14% |
| `NO2` | Nitrogen dioksida | 1 sampai 290 | 2,88% |
| `CO` | Karbon monoksida | 100 sampai 10.000 | 4,92% |
| `O3` | Ozon | 0,2 sampai 1.071 | 3,16% |

### Kolom cuaca

| Kolom | Arti | Rentang nilai | Kosong |
|---|---|---|---|
| `TEMP` | Suhu udara | −19,9 sampai 41,6 | 0,09% |
| `PRES` | Tekanan udara | 982,4 sampai 1.042,8 | 0,09% |
| `DEWP` | Suhu titik embun | −43,4 sampai 29,1 | 0,10% |
| `RAIN` | Curah hujan | 0 sampai 72,5 | 0,09% |
| `wd` | Arah datangnya angin, 16 kategori (N, NNE, NE, ENE, E, dan seterusnya sampai NNW). Satu-satunya kolom berupa teks | 16 kategori | 0,43% |
| `WSPM` | Kecepatan angin | 0 sampai 13,2 | 0,08% |

Satuan mengikuti dokumentasi UCI: polutan dalam mikrogram per meter kubik, suhu dan titik embun dalam derajat Celsius, tekanan dalam hPa, hujan dalam mm, kecepatan angin dalam meter per detik. Satuan ini belum dicek ulang pada halaman UCI saat berkas ini disusun. Rentang nilai dan persentase kosong dihitung dari seluruh 420.768 baris.

### Contoh satu baris (Tiantan, 1 Maret 2013 pukul 00.00)

`PM2.5` = 6, `PM10` = 6, `SO2` = 4, `NO2` = 8, `CO` = 300, `O3` = 81, `TEMP` = −0,5, `PRES` = 1024,5, `DEWP` = −21,4, `RAIN` = 0, `wd` = NNW, `WSPM` = 5,7.

### Kolom mana yang dipakai di proyek ini

| Peran | Kolom |
|---|---|
| **Target** | `PM2.5` pada jam t+24. Ini bukan kolom asli, tetapi nilai `PM2.5` yang digeser 24 jam |
| Fitur langsung | `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3`, `TEMP`, `PRES`, `DEWP`, `RAIN`, `WSPM` pada jam t |
| Fitur turunan | `PM2.5` pada jam-jam sebelumnya, rata-rata bergulir `PM2.5`, `wd` (diubah menjadi angka), dan kalender dari `month`, `day`, `hour` |
| Pembentuk waktu dan tempat | `year`, `month`, `day`, `hour`, dan `station` |
| Tidak dipakai | `No` |

Nilai kosong ditandai `NA` di berkas CSV. Stasiun utama untuk membangun model adalah **Tiantan**, dan stasiun uji adalah **Dingling**. Dataset ini berisi pengukuran, bukan data pribadi warga.

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

### Tahap 1. Rumusan masalah dan metrik (selesai sebagian)

Menentukan apa yang diramal, untuk siapa, dan bagaimana mengukurnya.
- Target: PM2.5 pada jam t+24. Metrik utama: RMSE.
- Keputusan: horizon 24 jam, stasiun utama Tiantan, nilai ekstrem 999 dipertahankan.
- Proposal tertulis sudah ada dengan lima referensi. Belum: persetujuan dosen dan versi PDF.

### Tahap 2. Eksplorasi dan praproses (selesai)

Mengenali data, lalu mengubahnya menjadi tabel masukan (fitur) dan target untuk model.

**Fitur dan target.** Fitur adalah kolom masukan yang dibaca model. Target adalah angka yang harus ditebak model. Satu baris tabel berisi fitur yang diukur pada jam t (misalnya pukul 10.00 hari ini) dan target berupa PM2.5 pada jam t+24 (pukul 10.00 besok).

**Aturan fitur.** Setiap fitur dihitung hanya dari data pada jam t atau sebelum jam t. Tidak ada fitur yang berasal dari jam sesudah t. Alasannya, saat ramalan dibuat di dunia nyata, data sesudah jam t belum ada. Jika sebuah fitur memakai data sesudah jam t, skor model terlihat bagus tetapi model itu tidak bisa dipakai di dunia nyata. Itu disebut kebocoran data.

Ada 29 fitur untuk stasiun Tiantan:

| Kelompok | Isi | Jumlah |
|---|---|---|
| Kondisi pada jam t | PM2.5, PM10, SO2, NO2, CO, O3, suhu, tekanan, titik embun, hujan, kecepatan angin | 11 |
| Riwayat PM2.5 (*lag*) | nilai PM2.5 pada 1, 2, 3, 6, 12, 24, dan 48 jam sebelum jam t | 7 |
| Rata-rata bergulir | rata-rata PM2.5 selama 6, 24, dan 72 jam sebelum dan termasuk jam t | 3 |
| Arah angin | diubah menjadi sinus dan kosinus | 2 |
| Kalender | jam, hari, dan bulan, masing-masing sebagai sinus dan kosinus, agar pukul 23.00 tercatat dekat dengan pukul 00.00 | 6 |

Yang dilakukan di tahap ini:

1. **Mengenali data (EDA).** PM2.5 miring ke kanan, jadi episode polusi tinggi akan mendominasi RMSE. Rata-rata tertinggi terjadi di bulan Desember dan pada pukul 23.00. Nilai PM2.5 yang kosong pada data latih Tiantan 2,08%, dengan celah terpanjang 24 jam. Nilai ekstrem 999 dipertahankan.
2. **Menyimpan data uji sejak awal.** Data mulai 12 Mei 2016 disisihkan sebelum eksplorasi dan tidak dibuka.
3. **Membuat fitur dan target** seperti tabel di atas. Baris latih yang targetnya jatuh di periode uji (24 jam terakhir sebelum batas) dibuang.
4. **Menangani nilai hilang.** Baris yang targetnya kosong dibuang. Fitur yang kosong diisi median, dan median itu dihitung dari data latih saja. Nilai dari jam sesudah celah tidak dipakai untuk mengisi.
5. **Menjustifikasi dua pilihan.** Pengisian nilai hilang dengan beberapa batas jam dibandingkan, dan hasilnya tidak berbeda nyata, sehingga dipilih cara paling sederhana (tanpa *forward fill*). Dingling dipilih sebagai stasiun uji karena distribusi PM2.5-nya paling berbeda dari Tiantan. Hasil uji pada data latih tidak membuktikan Dingling paling sulit diramal.

Hasilnya: 27.443 baris latih dengan 29 fitur, dan 6.896 baris uji yang disimpan tanpa dibuka.

### Tahap 3. Skema validasi (selesai)

Menetapkan cara menguji model supaya skornya jujur.
- Data diurutkan menurut waktu. **20% terakhir disimpan sebagai data uji** (mulai 12 Mei 2016) dan hanya dibuka satu kali di akhir.
- Sisanya (80%) dipakai untuk memilih model dengan `TimeSeriesSplit` 5 lipatan, dengan jarak aman 24 jam. Target sebuah baris latih adalah PM2.5 24 jam sesudahnya, jadi tanpa jarak, target baris latih terakhir bisa jatuh di periode validasi. Jarak 24 jam mencegah hal itu.
- Pengisian nilai hilang dan penskalaan dihitung dari data latih saja pada setiap lipatan, tidak dari data validasi atau data uji. Ini dilakukan dengan menaruhnya di dalam *pipeline*.
- Kelemahan yang diakui: hanya 5 lipatan, simpangan baku antar lipatan besar, dan statistik ringkas periode uji pernah dilihat (7 dan 15 Nov 2026), tetapi tidak dipakai untuk memilih fitur, model, atau pengaturan.

### Tahap 4. *Baseline* (selesai sebagian)

Hasil acuan. Model lanjutan baru dianggap berguna jika RMSE-nya lebih kecil dari angka ini.

| Model | RMSE (rata-rata ± sd antar lipatan) |
|---|---|
| *Naive forecast* (tebak PM2.5 besok sama dengan sekarang) | 86,97 ± 25,19 |
| Regresi linear (pembanding tambahan) | 73,38 ± 19,73 |

Regresi linear lebih baik dari *naive* di kelima lipatan. Ini hasil pada data latih, bukan data uji. Belum: dibahas di Pertemuan 13 dan dicek dosen.

### Tahap 5. Model lanjutan dan *tuning* (belum dikerjakan)

Minimal dua model yang lebih kuat (misalnya *random forest* dan *gradient boosting*), disetel dengan validasi silang pada data latih. Data uji tetap tidak disentuh.

### Tahap 6. Evaluasi dan diagnosis (belum dikerjakan)

Memeriksa apakah model terlalu sederhana (*underfitting*) atau terlalu menghafal (*overfitting*) dengan *learning curve*. Setelah model final dipilih, **data uji dibuka satu kali**, di Tiantan dan Dingling. Jika skornya jauh lebih buruk dari validasi, model tidak disetel ulang. Selisihnya dilaporkan dan dianalisis.

### Tahap 7. Analisis kesalahan dan etika (belum dikerjakan)

Mencari di mana model paling sering salah (jam, musim, stasiun, rentang konsentrasi), fitur mana yang paling berpengaruh, dan siapa yang dirugikan jika ramalan terlalu rendah. Model dipakai sebagai alat bantu peringatan, bukan pengambil keputusan otomatis.

## 6. Posisi saat ini

| Tahap | Status |
|---|---|
| 1. Rumusan masalah | Selesai sebagian (menunggu dosen dan PDF) |
| 2. Eksplorasi dan praproses | Selesai |
| 3. Skema validasi | Selesai |
| 4. *Baseline* | Selesai sebagian (belum dibahas dengan dosen) |
| 5 sampai 7 | Belum dikerjakan |

Berikutnya: Pertemuan 13 (maksimal 5 slide tentang tahap 1 sampai 4), lalu tahap 5.
