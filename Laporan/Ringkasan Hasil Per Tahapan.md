# Ringkasan Hasil Per Tahapan: Peramalan PM2.5 Beijing

Berisi inti hasil tiap tahap, diperbarui setiap satu tahap selesai. Rincian lengkap tahap 1 ada di `Proposal/Proposal Proyek ML PM25 Beijing (Versi Panjang).md`.

| Tahap | Status |
|---|---|
| 1. Proposal dan rumusan masalah | Selesai sebagian (draf selesai, menunggu konfirmasi dosen) |
| 2. EDA dan praproses | Selesai sebagian (*notebook* tahap 2 sudah dijalankan ulang di Colab; belum dipindah ke *notebook* utama dan batas *forward fill* belum diputuskan) |
| 3. Skema validasi | Belum dikerjakan |
| 4. *Baseline* | Belum dikerjakan |
| 5. Model lanjutan dan *tuning* | Belum dikerjakan |
| 6. Evaluasi dan diagnosis | Belum dikerjakan |
| 7. Analisis kesalahan dan etika | Belum dikerjakan |

## Tahap 1. Proposal

- **Topik dan *dataset*:** peramalan PM2.5 per jam, regresi deret waktu, Beijing Multi-Site Air Quality (UCI, 12 stasiun, 1 Maret 2013 sampai 28 Februari 2017).
- **Rumusan masalah:** memprediksi PM2.5 pada 24 jam ke depan dari riwayat PM2.5, polutan lain, dan cuaca sampai jam prediksi, sebagai dasar keputusan warga membatasi paparan.
- **Metrik utama:** RMSE, karena galat besar paling merugikan, terutama ramalan terlalu rendah saat konsentrasi tinggi. Pendamping: MAE.
- **Validasi:** data diurutkan menurut waktu, 20% terakhir sebagai data uji (dibuka satu kali), `TimeSeriesSplit` pada 80% awal.
- ***Baseline*:** *naive forecast*. Model lanjutan dan pembanding tambahan belum ditentukan.
- **Tiga tantangan:** nilai hilang (imputasi kausal di dalam *pipeline*), validasi berurutan waktu (tanpa kebocoran), pergeseran distribusi (latih dan validasi di satu stasiun utama, uji model akhir di stasiun lain pada periode uji yang sama).
- **Keputusan yang sudah ditetapkan:** horizon 24 jam (alasan: waktu bagi warga untuk membatasi paparan), skema uji stasiun lain berupa latih di satu stasiun lalu uji di stasiun lain, nilai ekstrem 999 dipertahankan, stasiun utama Tiantan (kandidat stasiun uji: Dingling, Huairou, Dongsi).
- **Referensi:** [1] Cui dkk. 2023; [2] Hewamalage dkk. 2023; [3] Hua dkk. 2024 (detail ada di versi panjang).

## Tahap 2. EDA dan praproses

Semua angka berasal dari eksekusi `Notebook/Tahap 2 EDA dan Praproses.ipynb` pada stasiun Tiantan dan **hanya memakai data latih**, kecuali disebut lain. Hasil eksekusi di Colab (15 Nov 2026) sudah dicocokkan dengan eksekusi awal: ukuran kedua berkas fitur, dua tabel ringkasan, dan hitungan panjang celah sama.

Keluaran *notebook*: sembilan grafik di `Hasil/Gambar/`, dua tabel di `Hasil/Tabel/`, dan fitur siap pakai (latih dan uji, Tiantan) di `Data/Data Olahan/`. Berkas fitur uji hanya disimpan, tidak dibuka untuk analisis.

- **Pembagian waktu:** data uji dimulai 2016-05-12 19:00 (20% jam terakhir), disisihkan sebelum eksplorasi dan tidak dibuka. Data latih seluruh stasiun 336.612 baris (80%).
- **Sebaran PM2.5:** median 59, rata-rata 82,2, miring ke kanan (*skewness* 1,91). Galat besar saat episode polusi tinggi akan mendominasi RMSE.
- **Nilai ekstrem (12 stasiun, data latih):** 659 jam di atas 500, 32 jam di atas 700, 3 jam di atas 900, 1 jam bernilai tepat 999. Pada jam-jam di atas 700, median 10 dari 12 stasiun ikut di atas 300, jadi lonjakan itu terjadi serempak dan sejalan dengan keputusan mempertahankan nilai ekstrem. Belum ada bukti batas alat ukur.
- **Pola waktu:** rata-rata tertinggi bulan Desember (106), terendah Agustus (59). Per jam, tertinggi pukul 23.00 (89), terendah pukul 16.00 (76).
- **Nilai hilang PM2.5:** 2,08% pada data latih Tiantan, dalam 313 celah. Median celah 1 jam, terpanjang 24 jam. Celah sampai 3 jam mencakup 91% celah tetapi hanya 65% jam yang hilang.
- **Korelasi dengan PM2.5 24 jam kemudian:** PM2.5 sekarang 0,39, CO 0,34, NO2 0,33, PM10 0,32. Korelasi PM2.5 dengan nilai sebelumnya turun dari 0,39 (24 jam) ke 0,12 (48 jam) dan 0,03 (72 jam), sehingga *lag* lebih dari dua hari hampir tidak informatif.
- **Antarstasiun (rata-rata PM2.5 data latih):** Dingling 67,0, Huairou 71,0, Tiantan 82,2, Dongsi 85,7. Secara visual, pola bulanan Tiantan searah dengan tiga kandidat stasiun uji (belum diukur). Rata-rata yang berbeda belum membuktikan stasiun itu paling sulit diramal.
- **Fitur dan target:** target PM2.5 pada jam t+24, 29 fitur yang hanya memakai data sampai jam t (kondisi sekarang, *lag* 1 sampai 48 jam, *rolling mean* 6, 24, 72 jam, kalender, arah angin). Baris latih 27.443, baris uji 6.896 (disimpan, tidak dibuka).
- **Penutupan celah kebocoran:** baris latih yang targetnya jatuh di periode uji (24 jam terakhir) dibuang.
- **Nilai hilang pada fitur [Usulan]:** target yang hilang dibuang, fitur diisi nilai terakhir (*forward fill*) paling lama 3 jam, sisanya diisi median di dalam *pipeline* per *fold*. Interpolasi tidak dipakai karena melihat nilai sesudahnya. Batas 3 jam adalah usulan dan belum diputuskan penulis.
- **Belum diputuskan atau belum dikerjakan:** batas *forward fill*, stasiun uji (opsi A sudah ditetapkan, stasiunnya belum), pemindahan isi ke *notebook* utama, dan pengujian *pipeline* bersama model (tahap 4).
