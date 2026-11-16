# Penjelasan Proyek dan Alur Tahapan

Ringkasan versi mudah dibaca. Angka diambil dari hasil eksekusi *notebook* pada data latih. Data uji belum pernah dibuka.

## 1. Topik

**Meramalkan konsentrasi PM2.5 di Beijing, 24 jam ke depan.**

PM2.5 adalah partikel debu sangat halus (diameter 2,5 mikrometer atau kurang) yang bisa masuk ke paru-paru. Semakin tinggi konsentrasinya, semakin berbahaya bagi kesehatan. Jika kita bisa meramalkan nilainya untuk besok, warga punya waktu untuk memutuskan apakah perlu memakai masker atau mengurangi aktivitas di luar ruangan.

Jenis tugasnya adalah **regresi deret waktu**: model menebak sebuah angka (PM2.5) dari data yang urut menurut waktu.

## 2. Dataset

**Beijing Multi-Site Air Quality** dari UCI (https://archive.ics.uci.edu/dataset/501).

| Hal | Isi |
|---|---|
| Sumber data | 12 stasiun pemantau udara di Beijing |
| Frekuensi | Satu baris per jam |
| Periode | 1 Maret 2013 sampai 28 Februari 2017 |
| Ukuran | 420.768 baris (12 stasiun × 35.064 jam) |
| Isi | PM2.5, polutan lain (PM10, SO2, NO2, CO, O3), dan cuaca (suhu, tekanan, titik embun, hujan, angin) |
| Nilai hilang | PM2.5 hilang sekitar 2,08%, karena sensor kadang tidak mencatat |
| Stasiun utama | **Tiantan** (untuk membangun dan memilih model) |
| Stasiun uji | **Dingling** (untuk menguji apakah model masih bagus di tempat lain) |

## 3. Rumusan masalah

> Model ini membantu warga dan otoritas kesehatan lingkungan memutuskan pembatasan paparan, dengan memprediksi PM2.5 24 jam ke depan dari riwayat PM2.5, polutan lain, dan cuaca sampai jam prediksi. Kesalahan paling mahal adalah galat besar, terutama ramalan yang terlalu rendah saat polusi tinggi, sehingga metrik utama adalah RMSE.

**RMSE** adalah ukuran rata-rata seberapa jauh tebakan dari kenyataan, dengan kesalahan besar dihukum lebih berat. Cocok di sini karena meleset jauh saat polusi tinggi paling merugikan. MAE dipakai sebagai pendamping.

Tiga tantangan wajib dari dosen:

1. **Nilai hilang pada sensor.** Data yang kosong harus ditangani tanpa "mengintip" masa depan.
2. **Validasi berurutan waktu.** Data tidak boleh diacak, karena model hanya boleh belajar dari masa lalu untuk menebak masa depan.
3. **Uji di stasiun lain.** Model dari satu stasiun dicoba di stasiun berbeda untuk melihat apakah kinerjanya turun (pergeseran distribusi).

## 4. Tujuan

1. Membangun model peramalan PM2.5 24 jam ke depan yang dievaluasi dengan **jujur dan bebas kebocoran data**.
2. Menunjukkan seberapa jauh model lebih baik dari tebakan paling sederhana (*baseline*).
3. Menguji apakah model tetap andal di stasiun lain.
4. Menganalisis kapan dan mengapa model salah, termasuk siapa yang dirugikan.

Yang dinilai dosen bukan skor tertinggi. Model sederhana yang dievaluasi dengan benar lebih berharga daripada model rumit yang skornya bagus karena bocor.

*Kebocoran data* berarti informasi dari data uji ikut terlihat oleh model saat belajar, sehingga skor tampak lebih bagus daripada kenyataannya. Seluruh rancangan tahap 1 sampai 4 dibuat untuk mencegah hal ini.

## 5. Alur dari tahap ke tahap

```
Tahap 1          Tahap 2           Tahap 3            Tahap 4
Rumusan    →    Eksplorasi   →    Aturan ujian  →    Tebakan
masalah         dan rapikan       (validasi)         pembanding
                data                                 (baseline)
                                                         │
                                          Pertemuan 13 (cek bersama dosen)
                                                         │
Tahap 5          Tahap 6           Tahap 7               ↓
Model       →    Evaluasi     →    Analisis kesalahan
lanjutan         akhir pada        dan etika
dan tuning       data uji
```

Urutannya penting. Aturan ujian (tahap 3) dibuat **sebelum** model dibangun, supaya hasil model tidak bisa memengaruhi aturannya.

### Tahap 1. Rumusan masalah dan metrik (selesai sebagian)

Menentukan apa yang diramal, untuk siapa, dan bagaimana mengukurnya.
- Target: PM2.5 pada jam t+24. Metrik utama: RMSE.
- Keputusan: horizon 24 jam, stasiun utama Tiantan, nilai ekstrem 999 dipertahankan.
- Proposal tertulis sudah ada dengan lima referensi. Belum: persetujuan dosen dan versi PDF.

### Tahap 2. Eksplorasi dan praproses (selesai)

Mengenali data, lalu menyiapkannya menjadi fitur untuk model.
- Fitur hanya memakai informasi sampai jam sekarang: nilai PM2.5 lampau (*lag*), rata-rata bergulir, kalender, cuaca, arah angin. Ada 29 fitur.
- Data hilang tidak diisi dengan nilai dari masa depan. Hasil perbandingan menunjukkan pilihan pengisian tidak berbeda nyata, jadi dipilih yang paling sederhana: tanpa *forward fill*.
- Stasiun uji dipilih Dingling karena pola PM2.5-nya paling berbeda dari Tiantan.

### Tahap 3. Skema validasi (selesai)

Membuat "aturan ujian" yang adil.
- Data diurutkan menurut waktu. **20% terakhir disimpan sebagai data uji** (mulai 12 Mei 2016) dan hanya dibuka satu kali di akhir.
- Sisanya (80%) dipakai untuk memilih model dengan `TimeSeriesSplit` 5 lipatan, dengan jarak aman 24 jam agar tidak ada tumpang tindih antara data latih dan validasi.
- Semua praproses dilakukan di dalam *pipeline*, sehingga hanya belajar dari data latih.
- Kelemahan yang diakui: hanya 5 lipatan, simpangan baku antar lipatan besar, dan ringkasan statistik periode uji pernah terlihat (tidak dipakai untuk keputusan apa pun).

### Tahap 4. *Baseline* (selesai sebagian)

Titik acuan: model apa pun harus lebih baik dari sini.

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
