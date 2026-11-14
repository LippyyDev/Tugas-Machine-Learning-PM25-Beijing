# Proposal Proyek Individu Pembelajaran Mesin: Peramalan PM2.5 Beijing

**Nama:** Muhammad Alif Qadri | **NIM:** D082261018 | **Program:** S2 Teknik Informatika, Universitas Hasanuddin | **Mata kuliah:** Pembelajaran Mesin

## 1. Latar Belakang dan Rumusan Masalah

Konsentrasi PM2.5 yang tinggi berdampak buruk pada kesehatan, sehingga ramalan untuk satu hari ke depan dapat membantu warga mengatur paparannya. Penelitian terbaru pada data Beijing banyak memakai model *deep learning*, misalnya perbandingan *transformer* dan CNN-LSTM-*attention* pada PM2.5 per jam di 12 stasiun [1]. Namun skor suatu model baru dapat dipercaya apabila evaluasinya benar, sebab praktik evaluasi yang keliru dapat membuat metode yang sebenarnya tidak kompetitif tampak kompetitif [2]. Karena itu proyek ini akan menekankan desain evaluasi yang bebas kebocoran data (*data leakage*), bukan skor tertinggi.

Berdasarkan latar belakang tersebut, masalah yang dikaji pada proyek ini adalah peramalan konsentrasi PM2.5 pada 24 jam ke depan sebagai tugas regresi deret waktu. Hasil ramalan ditujukan bagi warga dan otoritas kesehatan lingkungan sebagai dasar keputusan pembatasan paparan, misalnya aktivitas luar ruang dan pemakaian masker. Konsentrasi PM2.5 diprediksi dari riwayat PM2.5, polutan lain, dan data cuaca yang tersedia sampai jam prediksi. Kesalahan yang paling merugikan adalah galat besar, terutama ramalan yang terlalu rendah pada saat konsentrasi tinggi karena warga tidak akan mendapat peringatan. Oleh sebab itu, RMSE dipilih sebagai metrik utama.

## 2. Dataset

*Dataset* yang dipakai adalah Beijing Multi-Site Air Quality dari UCI (https://archive.ics.uci.edu/dataset/501). Isinya data per jam dari 12 stasiun, mulai 1 Maret 2013 sampai 28 Februari 2017, yang mencakup PM2.5, polutan lain, dan variabel cuaca. Jenis tugasnya adalah regresi deret waktu. Data ini bersifat publik dan tidak memuat data pribadi.

## 3. Tiga Tantangan dan Rencana Penanganan

1. **Nilai hilang pada sensor.** Panjang dan pola celah akan diprofilkan lebih dulu pada tahap EDA. Imputasi harus bersifat kausal dan berada di dalam *pipeline*, sehingga hanya belajar dari data latih pada setiap *fold*. Interpolasi dua arah tidak akan dipakai karena memanfaatkan nilai sesudah celah. Pengaruh pilihan imputasi terhadap hasil prediksi pada data kualitas udara telah dikaji pada [3], dan di proyek ini akan diuji sebagai perbandingan terkontrol, misalnya *forward fill* terbatas melawan imputer yang dipelajari per *fold*.
2. **Validasi berurutan waktu.** Data diurutkan menurut waktu. Data uji adalah 20% periode paling akhir yang tidak diacak, dan baru dibuka satu kali di akhir pekerjaan. Pemilihan model dan *tuning* memakai `TimeSeriesSplit` pada 80% data awal. Seluruh fitur hanya berasal dari waktu sampai jam prediksi (*lag*, rata-rata bergulir dari masa lalu, kalender, dan cuaca), sedangkan polutan lain pada jam target tidak dipakai. Alasan metodologis ini sejalan dengan panduan evaluasi peramalan yang menyoroti kebocoran lewat pembagian data dan praproses [2].
3. **Pergeseran distribusi antar stasiun.** Model dilatih dan divalidasi pada satu stasiun utama, lalu model akhir diuji pada beberapa stasiun lain yang tidak ikut dipakai untuk memilih model. Uji di stasiun lain memakai periode 20% terakhir yang sama dengan data uji stasiun utama, agar tidak ada kebocoran waktu, dan dibuka satu kali di akhir. Stasiun utama dan stasiun uji dipilih setelah EDA, dengan stasiun uji yang beragam. Hasilnya dibandingkan dengan uji pada stasiun yang sama untuk melihat besar penurunan kinerjanya. Pergeseran antar musim dan tahun juga diperiksa sebagai pembanding.

## 4. Metrik dan Rencana Model

- **Metrik utama** adalah RMSE, karena galat besar paling merugikan dan PM2.5 memiliki episode konsentrasi tinggi. MAE menjadi pendamping, ditambah RMSE pada rentang konsentrasi tinggi untuk memeriksa *underestimation*. Hasil CV dilaporkan sebagai rata-rata ± simpangan baku.
- **Nilai ekstrem PM2.5 (termasuk 999)** dipertahankan, tidak dibuang dan tidak dipotong. Pada 80% data awal, nilai 999 hanya muncul satu kali dan terjadi di tengah episode polusi berat yang serempak di banyak stasiun, sehingga belum ada bukti bahwa nilai itu merupakan batas alat ukur. Membuang episode tinggi juga akan menghilangkan bagian yang paling ingin diukur, yaitu ramalan yang terlalu rendah saat konsentrasi tinggi.
- **Horizon peramalan** ditetapkan 24 jam ke depan. Alasannya kebutuhan pengguna: warga memerlukan waktu untuk memutuskan pembatasan paparan, sedangkan peringatan satu jam sebelumnya terlalu singkat. Panduan tidak menetapkan horizon, dan pilihan ini bukan didasarkan pada kekuatan *baseline*.
- ***Baseline*** adalah *naive forecast*, yaitu nilai PM2.5 terakhir yang teramati, disesuaikan dengan horizon 24 jam.
- **Model lanjutan** (minimal dua) dan pembanding tambahan: belum ditentukan.
- **Diagnosis dan analisis** mencakup *learning curve* dengan CV berurutan waktu, galat per jam, musim, tahun, stasiun, dan rentang konsentrasi, serta pembahasan etis tentang siapa yang dirugikan oleh ramalan yang terlalu rendah dan bagaimana model sebaiknya dipakai sebagai alat bantu manusia.

## 5. Keputusan Terbuka

- **Stasiun utama dan stasiun uji.** Belum dipilih. Pemilihan didasarkan pada kelengkapan data dan keterwakilan (rata-rata mendekati rata-rata seluruh stasiun), bukan pada skor model, dan dilakukan setelah EDA pada 80% data awal.

## Daftar Pustaka

[1] B. Cui, M. Liu, S. Li, Z. Jin, Y. Zeng, and X. Lin, "Deep learning methods for atmospheric PM2.5 prediction: A comparative study of transformer and CNN-LSTM-attention," *Atmospheric Pollution Research*, vol. 14, no. 9, Art. no. 101833, 2023, doi: 10.1016/j.apr.2023.101833.

[2] H. Hewamalage, K. Ackermann, and C. Bergmeir, "Forecast evaluation for data scientists: Common pitfalls and best practices," *Data Mining and Knowledge Discovery*, vol. 37, no. 2, pp. 788–832, 2023, doi: 10.1007/s10618-022-00894-5.

[3] V. Hua, T. Nguyen, M.-S. Dao, H. D. Nguyen, and B. T. Nguyen, "The impact of data imputation on air quality prediction problem," *PLOS ONE*, vol. 19, no. 9, 2024, doi: 10.1371/journal.pone.0306303.
