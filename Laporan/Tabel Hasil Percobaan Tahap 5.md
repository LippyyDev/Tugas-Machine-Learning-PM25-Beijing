# Tabel Hasil Percobaan Tahap 5

Semua percobaan model lanjutan pada validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` di data latih 9 stasiun, diurutkan dari RMSE rata-rata terendah (terbaik) ke tertinggi (terburuk).

**Kriteria masuk tabel:** model dijalankan dan dilatih langsung pada data latih 9 stasiun yang digabung, dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*, sehingga punya nilai RMSE di kelima *fold*. **Tingkat kesulitan 4 (Sangat sulit) tidak dimasukkan** atas permintaan penulis (22 Nov 2026), sehingga tabel hanya memuat tingkat 1 sampai 3. Konfigurasi *tuning* acak yang hanya tercatat rata-rata dan simpangan baku (tanpa nilai tiap *fold*) tidak dimasukkan. Catatannya tetap ada di `Hasil/Tabel/t5_tabel_tuning.csv` dan `t5_tabel_tuning_putaran2.csv`. **Data uji tidak dibuka.** Angka berasal dari eksekusi `Notebook/Tahap 2 EDA dan Praproses.ipynb` (bagian 05.1, 05.5, dan 05.7) dan digabung oleh `Notebook/bangun_tabel_hasil_percobaan.py` dari CSV di `Hasil/Tabel/`. Berkas CSV gabungan: `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.

## Cara membaca

* **RMSE** adalah rata-rata RMSE dari 5 *fold* (µg/m³, makin kecil makin baik). **sd RMSE** adalah simpangan baku RMSE antar 5 *fold* (n minus 1), yaitu sebaran kesulitan antar periode, bukan ketidakpastian rata-rata.
* **MSE** adalah rata-rata dari RMSE kuadrat di tiap *fold* (jadi bukan kuadrat dari RMSE rata-rata). **MAE** dan **sd MAE** dihitung dengan cara yang sama seperti RMSE.
* **Perbaikan vs *naive*** memakai RMSE *naive forecast* 86,82. **Selisih vs Ridge `alpha=1`** dihitung berpasangan per *fold* (negatif berarti lebih baik dari Ridge), dengan simpangan baku selisih di dalam kurung.
* **Periode validasi tiap *fold*:** *fold* 1 2013-09-11 sampai 2014-03-25, *fold* 2 sampai 2014-10-05, *fold* 3 sampai 2015-04-18, *fold* 4 sampai 2015-10-30, *fold* 5 sampai 2016-05-11. *Fold* 1, 3, dan 5 lebih sulit (RMSE *naive* 101,7; 103,6; 108,8).
* **Fitur:** F1 adalah 29 fitur awal, F2 menambah 11 fitur cuaca dinamis dan 6 fitur statistik, F3 menambah 4 fitur **lintas stasiun** (rata-rata stasiun latih lain pada jam yang sama). F3 mengubah aturan di bagian 01 dan keputusan memakainya ada pada penulis.

## Peringatan

1. Selisih antar hampir semua konfigurasi jauh di bawah sd RMSE antar *fold* (sekitar 19), jadi urutan di tabel **tidak berarti** bahwa peringkat yang berdekatan berbeda nyata.
2. Skor terbaik dipilih dari puluhan konfigurasi pada lima *fold* yang sama, sehingga optimistis dan bukan kinerja akhir. Kinerja akhir hanya dari data uji, satu kali.
3. Langkah 3 sampai 6 di bagian 05.5 ditentukan setelah melihat hasil langkah sebelumnya. Grid 05.7 ditetapkan sebelum dijalankan.
4. Baris yang sama di beberapa bagian (misalnya Ridge `alpha=1`) digabung, kolom Sumber menunjukkan asalnya. Nilai per *fold* di bagian 05.1 dibulatkan dua desimal di berkasnya.

## Tingkat kesulitan

Kolom "Kesulitan (skor)" di Tabel 1 menilai seberapa sulit konfigurasi itu **diimplementasikan, dijalankan, dan dipertanggungjawabkan**. Rubrik ini **[Usulan]**, dibuat dari struktur konfigurasi saja dan **tidak memakai hasil RMSE**, jadi tidak ada pengaruh dari peringkat. Skor adalah jumlah lima komponen:

| Komponen | Skor | Alasan kesulitan |
|---|---|---|
| Jenis model | *Naive* 0, linear (Ridge, Elastic Net) 1, pohon atau *boosting* (*gradient boosting*, HGB, *random forest*, *Extra Trees*) 3 | Linear tinggal satu pemanggilan dan koefisiennya bisa dibaca. Model pohon memiliki banyak hiperparameter, hubungannya nonlinear sehingga sulit dijelaskan per fitur, lebih lambat dilatih, dan hasilnya peka pada seed. |
| Komposisi | Tunggal 0, dua model (rata-rata atau dua tahap) 1, tiga model atau lebih 2 | Setiap model tambahan perlu dilatih per *fold*, prediksinya disimpan dan digabung, dan satu kesalahan di satu model memengaruhi semuanya. |
| Fitur | F1 0, F2 1, F3 2 | F2 memerlukan fitur turunan baru (angin u dan v, hujan kumulatif, statistik mingguan) beserta uji kebocoran. F3 memerlukan penggabungan deret antar stasiun (rata-rata stasiun lain, tanpa stasiun itu sendiri), mengubah aturan bagian 01, dan di data uji harus diisi dari 9 stasiun latih. |
| *Tuning* | Tanpa pencarian 0, hasil pencarian acak 2 | Perlu pencarian beberapa hiperparameter, pemilihan jumlah iterasi dari kurva rata-rata 5 *fold*, dan waktu komputasi besar (mengulang seluruh eksperimen sekitar 45 menit pada 2 inti CPU). Skor terpilihnya juga lebih optimistis. |
| Transformasi target | Tidak ada 0, akar kuadrat atau `log1p` 1 | Prediksi harus dikembalikan ke skala asli, dan koreksi bias bisa diperlukan (di sini tidak dikoreksi). |

Tingkat dari skor: **1 Mudah** (0 sampai 1), **2 Sedang** (2 sampai 3), **3 Sulit** (4 sampai 6), **4 Sangat sulit** (7 atau lebih). Contoh: Ridge dengan F1 skor 1 (Mudah), Ridge dengan F3 skor 3 (Sedang), *random forest* bawaan dengan F3 skor 5 (Sulit), Ridge + *random forest* hasil *tuning* dengan F3 skor 8 (Sangat sulit).

Hubungan kesulitan dan hasil, dihitung **sebelum** 26 konfigurasi tingkat 4 dikeluarkan dari tabel, tanpa *naive forecast* (nilai per *fold*-nya tetap ada di `Hasil/Tabel/t5_tabel_eksperimen_per_fold.csv` dan semuanya tetap dicatat di *notebook* bagian 05.5):

| Tingkat | Jumlah konfigurasi | RMSE terbaik | RMSE median | RMSE terburuk |
|---|---|---|---|---|
| 1 Mudah | 24 | 72,26 | 72,87 | 76,09 |
| 2 Sedang | 8 | 71,93 | 73,66 | 80,10 |
| 3 Sulit | 14 | 71,92 | 73,53 | 79,59 |
| 4 Sangat sulit | 26 | 71,09 | 71,68 | 77,82 |

Tingkat 4 **tidak tampil di Tabel 1 dan 2**, tetapi angkanya perlu disebut agar pembaca tidak mengira tidak ada yang lebih baik: model tingkat 1 terbaik (selain *naive*) mendapat RMSE 72,26, sedangkan tingkat 4 terbaik 71,09. Naiknya kesulitan implementasi dari tingkat 1 ke tingkat 4 hanya menurunkan RMSE sekitar 1,18 (sekitar 1,6%), jauh di bawah simpangan baku antar *fold* (sekitar 19), dan sebagian dari selisih itu masih optimisme pemilihan dari banyak konfigurasi. Ini alasan memilih model yang mudah dijelaskan dan dipertanggungjawabkan: ongkos implementasi, risiko kebocoran, dan beban penjelasannya jauh lebih besar daripada perbaikan yang didapat.

Keterbatasan rubrik: bobot skor adalah usulan dan bukan standar baku, dan skor tidak mengukur waktu latih tiap model (waktu per model tidak diukur terpisah).

## Tabel 1. Ringkasan, urut dari terbaik ke terburuk (47 konfigurasi)

| No | Konfigurasi | Fitur | Kesulitan (skor) | RMSE | sd RMSE | MSE | MAE | sd MAE | Perbaikan vs *naive* (%) | *Fold* lebih baik dari *naive* | Selisih RMSE vs Ridge `alpha=1` (sd selisih) | *Fold* lebih baik dari Ridge | Sumber |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Rata-rata Ridge dan boosting (0,5) | F3 (F2 + lintas stasiun) | 3 Sulit (6) | 71,92 | 19,90 | 5490 | 53,23 | 13,51 | 17,2 | 5 dari 5 | -1,02 (0,94) | 5 dari 5 | 05.5 (langkah 2 model) |
| 2 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F3 (F2 + lintas stasiun) | 2 Sedang (3) | 71,93 | 19,30 | 5471 | 53,57 | 13,07 | 17,2 | 5 dari 5 | -1,01 (0,36) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 3 | Elastic Net (alpha=1, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,26 | 19,23 | 5518 | 54,43 | 13,31 | 16,8 | 5 dari 5 | -0,68 (0,84) | 3 dari 5 | 05.7 |
| 4 | Random forest terpilih | F2 (F1 + cuaca + statistik) | 3 Sulit (6) | 72,27 | 19,63 | 5532 | 53,83 | 13,48 | 16,8 | 5 dari 5 | -0,67 (1,36) | 4 dari 5 | 05.5 (langkah 3 tuning) |
| 5 | Ridge | F3 (F2 + lintas stasiun) | 2 Sedang (3) | 72,28 | 19,31 | 5522 | 53,84 | 13,01 | 16,7 | 5 dari 5 | -0,66 (0,34) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 6 | Rata-rata Ridge dan boosting (0,5) | F2 (F1 + cuaca + statistik) | 3 Sulit (5) | 72,28 | 19,83 | 5540 | 53,85 | 13,42 | 16,7 | 5 dari 5 | -0,66 (1,00) | 4 dari 5 | 05.5 (langkah 2 model) |
| 7 | HGB terpilih | F2 (F1 + cuaca + statistik) | 3 Sulit (6) | 72,35 | 19,16 | 5528 | 54,11 | 13,12 | 16,7 | 5 dari 5 | -0,59 (1,64) | 4 dari 5 | 05.5 (langkah 3 tuning) |
| 8 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F2 (F1 + cuaca + statistik) | 2 Sedang (2) | 72,44 | 19,50 | 5551 | 54,10 | 13,27 | 16,6 | 5 dari 5 | -0,51 (0,26) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 9 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + cuaca dinamis | 1 Mudah (1) | 72,49 | 19,22 | 5550 | 54,22 | 12,94 | 16,5 | 5 dari 5 | -0,45 (0,35) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 10 | Elastic Net (alpha=0,1, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,51 | 19,34 | 5557 | 54,30 | 13,08 | 16,5 | 5 dari 5 | -0,43 (0,37) | 5 dari 5 | 05.7 |
| 11 | Elastic Net (alpha=1, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 72,53 | 19,37 | 5561 | 54,79 | 13,38 | 16,5 | 5 dari 5 | -0,41 (1,06) | 3 dari 5 | 05.1, 05.7 |
| 12 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + statistik PM dan polutan | 1 Mudah (1) | 72,56 | 19,58 | 5572 | 54,23 | 13,30 | 16,4 | 5 dari 5 | -0,38 (0,25) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 13 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 72,60 | 19,33 | 5570 | 54,35 | 13,04 | 16,4 | 5 dari 5 | -0,34 (0,26) | 5 dari 5 | 05.1, 05.7, 05.5 (langkah 1 ablasi fitur) |
| 14 | Random forest | F3 (F2 + lintas stasiun) | 3 Sulit (5) | 72,71 | 19,79 | 5600 | 53,52 | 13,31 | 16,2 | 5 dari 5 | -0,23 (1,43) | 2 dari 5 | 05.5 (langkah 2 model) |
| 15 | Elastic Net (alpha=1, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,75 | 19,38 | 5593 | 55,07 | 13,37 | 16,2 | 5 dari 5 | -0,19 (1,19) | 2 dari 5 | 05.7 |
| 16 | Elastic Net (alpha=3, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,75 | 19,38 | 5593 | 55,32 | 13,63 | 16,2 | 5 dari 5 | -0,19 (1,37) | 2 dari 5 | 05.7 |
| 17 | Elastic Net (alpha=0,1, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,76 | 19,33 | 5594 | 54,47 | 12,99 | 16,2 | 5 dari 5 | -0,18 (0,13) | 5 dari 5 | 05.7 |
| 18 | Ridge (alpha=1000) | F1 (29 fitur awal) | 1 Mudah (1) | 72,83 | 19,38 | 5605 | 54,51 | 13,00 | 16,1 | 5 dari 5 | -0,11 (0,09) | 5 dari 5 | 05.7 |
| 19 | Ridge | F1 + cuaca dinamis | 1 Mudah (1) | 72,85 | 19,27 | 5604 | 54,50 | 12,85 | 16,1 | 5 dari 5 | -0,10 (0,18) | 3 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 20 | Elastic Net (alpha=0,01, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,85 | 19,37 | 5607 | 54,51 | 12,98 | 16,1 | 5 dari 5 | -0,09 (0,05) | 5 dari 5 | 05.7 |
| 21 | Ridge | F2 (F1 + cuaca + statistik) | 2 Sedang (2) | 72,87 | 19,56 | 5617 | 54,42 | 13,22 | 16,1 | 5 dari 5 | -0,07 (0,32) | 2 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 22 | Elastic Net (alpha=0,01, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 72,88 | 19,38 | 5612 | 54,54 | 12,97 | 16,1 | 5 dari 5 | -0,06 (0,03) | 5 dari 5 | 05.1, 05.7 |
| 23 | Elastic Net (alpha=0,01, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,92 | 19,38 | 5618 | 54,56 | 12,97 | 16,0 | 5 dari 5 | -0,02 (0,01) | 5 dari 5 | 05.7 |
| 24 | Ridge (alpha=100) | F1 (29 fitur awal) | 1 Mudah (1) | 72,93 | 19,39 | 5619 | 54,57 | 12,97 | 16,0 | 5 dari 5 | -0,01 (0,01) | 5 dari 5 | 05.7 |
| 25 | Ridge (alpha=10) | F1 (29 fitur awal) | 1 Mudah (1) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | -0,00 (0,00) | 5 dari 5 | 05.7 |
| 26 | Ridge (alpha=1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | 0,00 (0,00) | 0 dari 5 | 05.1, 05.7, 05.5 (langkah 1 ablasi fitur) |
| 27 | Ridge (alpha=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | 0,00 (0,00) | 0 dari 5 | 05.7 |
| 28 | Rata-rata Ridge dan boosting (0,5) | F1 (29 fitur awal) | 3 Sulit (4) | 72,97 | 19,81 | 5638 | 54,05 | 13,11 | 16,0 | 5 dari 5 | 0,03 (1,64) | 3 dari 5 | 05.5 (langkah 2 model) |
| 29 | Ridge | F1 + statistik PM dan polutan | 1 Mudah (1) | 72,98 | 19,65 | 5635 | 54,50 | 13,25 | 15,9 | 5 dari 5 | 0,04 (0,35) | 1 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 30 | Random forest | F2 (F1 + cuaca + statistik) | 3 Sulit (4) | 73,21 | 19,96 | 5679 | 54,34 | 13,66 | 15,7 | 5 dari 5 | 0,27 (1,92) | 2 dari 5 | 05.5 (langkah 2 model) |
| 31 | Elastic Net (alpha=3, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 73,45 | 19,39 | 5695 | 55,99 | 13,35 | 15,4 | 5 dari 5 | 0,51 (1,48) | 2 dari 5 | 05.7 |
| 32 | Elastic Net (alpha=3, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 73,81 | 19,39 | 5749 | 56,34 | 13,26 | 15,0 | 5 dari 5 | 0,87 (1,51) | 2 dari 5 | 05.7 |
| 33 | Ridge, target akar kuadrat | F3 (F2 + lintas stasiun) | 3 Sulit (4) | 73,84 | 21,34 | 5817 | 52,44 | 13,52 | 14,9 | 5 dari 5 | 0,90 (2,11) | 2 dari 5 | 05.5 (langkah 5 transformasi target) |
| 34 | Ridge, target akar kuadrat | F2 (F1 + cuaca + statistik) | 2 Sedang (3) | 74,44 | 21,66 | 5917 | 53,00 | 13,76 | 14,3 | 5 dari 5 | 1,50 (2,43) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 35 | Ridge lalu boosting pada residual | F3 (F2 + lintas stasiun) | 3 Sulit (6) | 74,59 | 22,21 | 5958 | 54,68 | 14,20 | 14,1 | 5 dari 5 | 1,65 (3,04) | 1 dari 5 | 05.5 (langkah 2 model) |
| 36 | Gradient boosting | F2 (F1 + cuaca + statistik) | 3 Sulit (4) | 75,24 | 21,19 | 6020 | 55,73 | 14,41 | 13,3 | 5 dari 5 | 2,30 (2,89) | 1 dari 5 | 05.5 (langkah 2 model) |
| 37 | Gradient boosting | F3 (F2 + lintas stasiun) | 3 Sulit (5) | 75,37 | 21,92 | 6066 | 55,22 | 14,87 | 13,2 | 5 dari 5 | 2,43 (3,26) | 1 dari 5 | 05.5 (langkah 2 model) |
| 38 | Ridge lalu boosting pada residual | F2 (F1 + cuaca + statistik) | 3 Sulit (5) | 75,58 | 22,05 | 6102 | 55,85 | 14,28 | 12,9 | 5 dari 5 | 2,64 (3,25) | 1 dari 5 | 05.5 (langkah 2 model) |
| 39 | Elastic Net (alpha=10, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 75,63 | 19,44 | 6022 | 57,89 | 12,74 | 12,9 | 5 dari 5 | 2,69 (1,93) | 0 dari 5 | 05.7 |
| 40 | Elastic Net (alpha=10, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 76,02 | 19,40 | 6080 | 58,22 | 12,61 | 12,4 | 5 dari 5 | 3,08 (1,93) | 0 dari 5 | 05.7 |
| 41 | Elastic Net (alpha=10, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 76,09 | 19,41 | 6092 | 58,34 | 12,68 | 12,4 | 5 dari 5 | 3,15 (1,84) | 0 dari 5 | 05.7 |
| 42 | Ridge lalu boosting pada residual | F1 (29 fitur awal) | 3 Sulit (4) | 76,71 | 22,01 | 6272 | 55,81 | 14,31 | 11,6 | 5 dari 5 | 3,77 (4,88) | 2 dari 5 | 05.5 (langkah 2 model) |
| 43 | Gradient boosting (*early stopping* bawaan) | F1 (29 fitur awal) | 2 Sedang (3) | 76,97 | 21,75 | 6302 | 56,04 | 14,07 | 11,3 | 5 dari 5 | 4,03 (4,79) | 1 dari 5 | 05.1 |
| 44 | Gradient boosting (200 iterasi, kedalaman 4) | F1 (29 fitur awal) | 2 Sedang (3) | 77,10 | 22,10 | 6335 | 56,11 | 14,50 | 11,2 | 5 dari 5 | 4,16 (5,84) | 1 dari 5 | 05.1, 05.5 (langkah 2 model) |
| 45 | Ridge, target log1p | F3 (F2 + lintas stasiun) | 3 Sulit (4) | 79,59 | 24,61 | 6819 | 53,44 | 14,68 | 8,3 | 5 dari 5 | 6,65 (5,33) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 46 | Ridge, target log1p | F2 (F1 + cuaca + statistik) | 2 Sedang (3) | 80,10 | 25,06 | 6918 | 53,85 | 14,94 | 7,7 | 5 dari 5 | 7,16 (5,77) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 47 | *Naive forecast* | n/a | 1 Mudah (0) | 86,82 | 24,70 | 8025 | 59,39 | 16,53 | 0,0 | 0 dari 5 | 13,88 (5,95) | 0 dari 5 | 05.1 |

## Tabel 2. RMSE tiap *fold*, urutan sama dengan Tabel 1

| No | Konfigurasi | *Fold* 1 | *Fold* 2 | *Fold* 3 | *Fold* 4 | *Fold* 5 |
|---|---|---|---|---|---|---|
| 1 | Rata-rata Ridge dan boosting (0,5) | 84,4 | 53,6 | 81,8 | 47,7 | 92,2 |
| 2 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 83,7 | 53,0 | 81,8 | 49,4 | 91,7 |
| 3 | Elastic Net (alpha=1, l1_ratio=0,9) | 84,1 | 52,7 | 82,6 | 50,4 | 91,6 |
| 4 | Random forest terpilih | 85,8 | 54,0 | 82,0 | 48,4 | 91,2 |
| 5 | Ridge | 83,9 | 53,8 | 82,1 | 49,4 | 92,1 |
| 6 | Rata-rata Ridge dan boosting (0,5) | 85,0 | 54,1 | 81,4 | 48,2 | 92,7 |
| 7 | HGB terpilih | 86,1 | 54,0 | 82,0 | 49,4 | 90,3 |
| 8 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,3 | 53,4 | 82,3 | 49,7 | 92,5 |
| 9 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,6 | 82,2 | 50,2 | 92,3 |
| 10 | Elastic Net (alpha=0,1, l1_ratio=0,1) | 84,1 | 53,3 | 82,4 | 50,3 | 92,5 |
| 11 | Elastic Net (alpha=1, l1_ratio=0,5) | 84,5 | 52,4 | 83,0 | 50,9 | 91,9 |
| 12 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,5 | 82,5 | 49,7 | 92,9 |
| 13 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,5 | 82,4 | 50,2 | 92,7 |
| 14 | Random forest | 86,2 | 54,5 | 82,6 | 48,4 | 91,8 |
| 15 | Elastic Net (alpha=1, l1_ratio=0,1) | 84,8 | 52,5 | 83,3 | 51,2 | 92,0 |
| 16 | Elastic Net (alpha=3, l1_ratio=0,9) | 85,2 | 52,3 | 83,2 | 51,3 | 91,7 |
| 17 | Elastic Net (alpha=0,1, l1_ratio=0,9) | 84,3 | 53,9 | 82,4 | 50,3 | 92,9 |
| 18 | Ridge (alpha=1000) | 84,3 | 54,0 | 82,4 | 50,3 | 93,2 |
| 19 | Ridge | 84,5 | 54,2 | 82,4 | 50,3 | 92,9 |
| 20 | Elastic Net (alpha=0,01, l1_ratio=0,1) | 84,4 | 54,0 | 82,4 | 50,3 | 93,1 |
| 21 | Ridge | 84,6 | 54,3 | 82,6 | 49,7 | 93,1 |
| 22 | Elastic Net (alpha=0,01, l1_ratio=0,5) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 23 | Elastic Net (alpha=0,01, l1_ratio=0,9) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 24 | Ridge (alpha=100) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 25 | Ridge (alpha=10) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 26 | Ridge (alpha=1) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 27 | Ridge (alpha=0,1) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 28 | Rata-rata Ridge dan boosting (0,5) | 86,7 | 55,3 | 81,3 | 48,6 | 93,0 |
| 29 | Ridge | 84,6 | 54,3 | 82,8 | 49,7 | 93,5 |
| 30 | Random forest | 87,7 | 55,0 | 82,8 | 48,6 | 92,1 |
| 31 | Elastic Net (alpha=3, l1_ratio=0,5) | 85,9 | 52,8 | 83,9 | 52,2 | 92,5 |
| 32 | Elastic Net (alpha=3, l1_ratio=0,1) | 86,3 | 53,0 | 84,1 | 52,7 | 92,9 |
| 33 | Ridge, target akar kuadrat | 87,1 | 54,0 | 83,2 | 48,3 | 96,5 |
| 34 | Ridge, target akar kuadrat | 87,8 | 54,4 | 83,9 | 48,5 | 97,6 |
| 35 | Ridge lalu boosting pada residual | 87,6 | 54,8 | 84,6 | 47,4 | 98,5 |
| 36 | Gradient boosting | 91,0 | 56,7 | 83,8 | 48,7 | 96,0 |
| 37 | Gradient boosting | 91,3 | 55,9 | 85,4 | 48,0 | 96,3 |
| 38 | Ridge lalu boosting pada residual | 89,0 | 56,5 | 83,8 | 48,5 | 100,1 |
| 39 | Elastic Net (alpha=10, l1_ratio=0,9) | 89,0 | 54,3 | 85,1 | 55,0 | 94,7 |
| 40 | Elastic Net (alpha=10, l1_ratio=0,5) | 89,2 | 54,7 | 85,4 | 55,6 | 95,3 |
| 41 | Elastic Net (alpha=10, l1_ratio=0,1) | 89,0 | 54,8 | 85,6 | 55,6 | 95,5 |
| 42 | Ridge lalu boosting pada residual | 96,0 | 57,9 | 82,4 | 49,5 | 97,7 |
| 43 | Gradient boosting (*early stopping* bawaan) | 95,7 | 59,5 | 83,3 | 49,0 | 97,3 |
| 44 | Gradient boosting (200 iterasi, kedalaman 4) | 98,1 | 59,5 | 83,0 | 48,8 | 96,2 |
| 45 | Ridge, target log1p | 94,9 | 57,2 | 90,2 | 49,8 | 105,8 |
| 46 | Ridge, target log1p | 95,2 | 57,4 | 91,1 | 49,8 | 107,0 |
| 47 | *Naive forecast* | 101,7 | 62,2 | 103,6 | 57,7 | 108,8 |
