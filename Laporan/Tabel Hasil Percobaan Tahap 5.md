# Tabel Hasil Percobaan Tahap 5

Semua percobaan model lanjutan pada validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` di data latih 9 stasiun, diurutkan dari RMSE rata-rata terendah (terbaik) ke tertinggi (terburuk).

**Kriteria masuk tabel:** model dijalankan dan dilatih langsung pada data latih 9 stasiun yang digabung, dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*, sehingga punya nilai RMSE di kelima *fold*. **Hanya tingkat kesulitan 1 (Mudah) yang dimasukkan** atas permintaan penulis (22 Nov 2026); tingkat 2 (Sedang), 3 (Sulit), dan 4 (Sangat sulit) tidak ditampilkan. Konfigurasi *tuning* acak yang hanya tercatat rata-rata dan simpangan baku (tanpa nilai tiap *fold*) tidak dimasukkan. Catatannya tetap ada di `Hasil/Tabel/t5_tabel_tuning.csv` dan `t5_tabel_tuning_putaran2.csv`. **Data uji tidak dibuka.** Angka berasal dari eksekusi `Notebook/Tahap 2 EDA dan Praproses.ipynb` (bagian 05.1, 05.5, dan 05.7) dan digabung oleh `Notebook/bangun_tabel_hasil_percobaan.py` dari CSV di `Hasil/Tabel/`. Berkas CSV gabungan: `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.

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

Hubungan kesulitan dan hasil, dihitung **sebelum** 48 konfigurasi tingkat 2 sampai 4 dikeluarkan dari tabel, tanpa *naive forecast* (nilai per *fold*-nya tetap ada di `Hasil/Tabel/t5_tabel_eksperimen_per_fold.csv` dan semuanya tetap dicatat di *notebook* bagian 05.5):

| Tingkat | Jumlah konfigurasi | RMSE terbaik | RMSE median | RMSE terburuk |
|---|---|---|---|---|
| 1 Mudah | 24 | 72,26 | 72,87 | 76,09 |
| 2 Sedang | 8 | 71,93 | 73,66 | 80,10 |
| 3 Sulit | 14 | 71,92 | 73,53 | 79,59 |
| 4 Sangat sulit | 26 | 71,09 | 71,68 | 77,82 |

Tingkat 2 sampai 4 **tidak tampil di Tabel 1 dan 2**, tetapi angkanya perlu disebut agar pembaca tidak mengira tidak ada yang lebih baik: model tingkat 1 terbaik (selain *naive*) mendapat RMSE 72,26, sedangkan tingkat 4 terbaik 71,09. Naiknya kesulitan implementasi dari tingkat 1 ke tingkat 4 hanya menurunkan RMSE sekitar 1,18 (sekitar 1,6%), jauh di bawah simpangan baku antar *fold* (sekitar 19), dan sebagian dari selisih itu masih optimisme pemilihan dari banyak konfigurasi. Ini alasan memilih model yang mudah dijelaskan dan dipertanggungjawabkan: ongkos implementasi, risiko kebocoran, dan beban penjelasannya jauh lebih besar daripada perbaikan yang didapat.

Keterbatasan rubrik: bobot skor adalah usulan dan bukan standar baku, dan skor tidak mengukur waktu latih tiap model (waktu per model tidak diukur terpisah).

## Tabel 1. Ringkasan, urut dari terbaik ke terburuk (25 konfigurasi)

| No | Konfigurasi | Fitur | Kesulitan (skor) | RMSE | sd RMSE | MSE | MAE | sd MAE | Perbaikan vs *naive* (%) | *Fold* lebih baik dari *naive* | Selisih RMSE vs Ridge `alpha=1` (sd selisih) | *Fold* lebih baik dari Ridge | Sumber |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Elastic Net (alpha=1, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,26 | 19,23 | 5518 | 54,43 | 13,31 | 16,8 | 5 dari 5 | -0,68 (0,84) | 3 dari 5 | 05.7 |
| 2 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + cuaca dinamis | 1 Mudah (1) | 72,49 | 19,22 | 5550 | 54,22 | 12,94 | 16,5 | 5 dari 5 | -0,45 (0,35) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 3 | Elastic Net (alpha=0,1, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,51 | 19,34 | 5557 | 54,30 | 13,08 | 16,5 | 5 dari 5 | -0,43 (0,37) | 5 dari 5 | 05.7 |
| 4 | Elastic Net (alpha=1, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 72,53 | 19,37 | 5561 | 54,79 | 13,38 | 16,5 | 5 dari 5 | -0,41 (1,06) | 3 dari 5 | 05.1, 05.7 |
| 5 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + statistik PM dan polutan | 1 Mudah (1) | 72,56 | 19,58 | 5572 | 54,23 | 13,30 | 16,4 | 5 dari 5 | -0,38 (0,25) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 6 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 72,60 | 19,33 | 5570 | 54,35 | 13,04 | 16,4 | 5 dari 5 | -0,34 (0,26) | 5 dari 5 | 05.1, 05.7, 05.5 (langkah 1 ablasi fitur) |
| 7 | Elastic Net (alpha=1, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,75 | 19,38 | 5593 | 55,07 | 13,37 | 16,2 | 5 dari 5 | -0,19 (1,19) | 2 dari 5 | 05.7 |
| 8 | Elastic Net (alpha=3, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,75 | 19,38 | 5593 | 55,32 | 13,63 | 16,2 | 5 dari 5 | -0,19 (1,37) | 2 dari 5 | 05.7 |
| 9 | Elastic Net (alpha=0,1, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,76 | 19,33 | 5594 | 54,47 | 12,99 | 16,2 | 5 dari 5 | -0,18 (0,13) | 5 dari 5 | 05.7 |
| 10 | Ridge (alpha=1000) | F1 (29 fitur awal) | 1 Mudah (1) | 72,83 | 19,38 | 5605 | 54,51 | 13,00 | 16,1 | 5 dari 5 | -0,11 (0,09) | 5 dari 5 | 05.7 |
| 11 | Ridge | F1 + cuaca dinamis | 1 Mudah (1) | 72,85 | 19,27 | 5604 | 54,50 | 12,85 | 16,1 | 5 dari 5 | -0,10 (0,18) | 3 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 12 | Elastic Net (alpha=0,01, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,85 | 19,37 | 5607 | 54,51 | 12,98 | 16,1 | 5 dari 5 | -0,09 (0,05) | 5 dari 5 | 05.7 |
| 13 | Elastic Net (alpha=0,01, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 72,88 | 19,38 | 5612 | 54,54 | 12,97 | 16,1 | 5 dari 5 | -0,06 (0,03) | 5 dari 5 | 05.1, 05.7 |
| 14 | Elastic Net (alpha=0,01, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 72,92 | 19,38 | 5618 | 54,56 | 12,97 | 16,0 | 5 dari 5 | -0,02 (0,01) | 5 dari 5 | 05.7 |
| 15 | Ridge (alpha=100) | F1 (29 fitur awal) | 1 Mudah (1) | 72,93 | 19,39 | 5619 | 54,57 | 12,97 | 16,0 | 5 dari 5 | -0,01 (0,01) | 5 dari 5 | 05.7 |
| 16 | Ridge (alpha=10) | F1 (29 fitur awal) | 1 Mudah (1) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | -0,00 (0,00) | 5 dari 5 | 05.7 |
| 17 | Ridge (alpha=1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | 0,00 (0,00) | 0 dari 5 | 05.1, 05.7, 05.5 (langkah 1 ablasi fitur) |
| 18 | Ridge (alpha=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | 0,00 (0,00) | 0 dari 5 | 05.7 |
| 19 | Ridge | F1 + statistik PM dan polutan | 1 Mudah (1) | 72,98 | 19,65 | 5635 | 54,50 | 13,25 | 15,9 | 5 dari 5 | 0,04 (0,35) | 1 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 20 | Elastic Net (alpha=3, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 73,45 | 19,39 | 5695 | 55,99 | 13,35 | 15,4 | 5 dari 5 | 0,51 (1,48) | 2 dari 5 | 05.7 |
| 21 | Elastic Net (alpha=3, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 73,81 | 19,39 | 5749 | 56,34 | 13,26 | 15,0 | 5 dari 5 | 0,87 (1,51) | 2 dari 5 | 05.7 |
| 22 | Elastic Net (alpha=10, l1_ratio=0,9) | F1 (29 fitur awal) | 1 Mudah (1) | 75,63 | 19,44 | 6022 | 57,89 | 12,74 | 12,9 | 5 dari 5 | 2,69 (1,93) | 0 dari 5 | 05.7 |
| 23 | Elastic Net (alpha=10, l1_ratio=0,5) | F1 (29 fitur awal) | 1 Mudah (1) | 76,02 | 19,40 | 6080 | 58,22 | 12,61 | 12,4 | 5 dari 5 | 3,08 (1,93) | 0 dari 5 | 05.7 |
| 24 | Elastic Net (alpha=10, l1_ratio=0,1) | F1 (29 fitur awal) | 1 Mudah (1) | 76,09 | 19,41 | 6092 | 58,34 | 12,68 | 12,4 | 5 dari 5 | 3,15 (1,84) | 0 dari 5 | 05.7 |
| 25 | *Naive forecast* | n/a | 1 Mudah (0) | 86,82 | 24,70 | 8025 | 59,39 | 16,53 | 0,0 | 0 dari 5 | 13,88 (5,95) | 0 dari 5 | 05.1 |

## Tabel 2. RMSE tiap *fold*, urutan sama dengan Tabel 1

| No | Konfigurasi | *Fold* 1 | *Fold* 2 | *Fold* 3 | *Fold* 4 | *Fold* 5 |
|---|---|---|---|---|---|---|
| 1 | Elastic Net (alpha=1, l1_ratio=0,9) | 84,1 | 52,7 | 82,6 | 50,4 | 91,6 |
| 2 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,6 | 82,2 | 50,2 | 92,3 |
| 3 | Elastic Net (alpha=0,1, l1_ratio=0,1) | 84,1 | 53,3 | 82,4 | 50,3 | 92,5 |
| 4 | Elastic Net (alpha=1, l1_ratio=0,5) | 84,5 | 52,4 | 83,0 | 50,9 | 91,9 |
| 5 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,5 | 82,5 | 49,7 | 92,9 |
| 6 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,5 | 82,4 | 50,2 | 92,7 |
| 7 | Elastic Net (alpha=1, l1_ratio=0,1) | 84,8 | 52,5 | 83,3 | 51,2 | 92,0 |
| 8 | Elastic Net (alpha=3, l1_ratio=0,9) | 85,2 | 52,3 | 83,2 | 51,3 | 91,7 |
| 9 | Elastic Net (alpha=0,1, l1_ratio=0,9) | 84,3 | 53,9 | 82,4 | 50,3 | 92,9 |
| 10 | Ridge (alpha=1000) | 84,3 | 54,0 | 82,4 | 50,3 | 93,2 |
| 11 | Ridge | 84,5 | 54,2 | 82,4 | 50,3 | 92,9 |
| 12 | Elastic Net (alpha=0,01, l1_ratio=0,1) | 84,4 | 54,0 | 82,4 | 50,3 | 93,1 |
| 13 | Elastic Net (alpha=0,01, l1_ratio=0,5) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 14 | Elastic Net (alpha=0,01, l1_ratio=0,9) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 15 | Ridge (alpha=100) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 16 | Ridge (alpha=10) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 17 | Ridge (alpha=1) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 18 | Ridge (alpha=0,1) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 19 | Ridge | 84,6 | 54,3 | 82,8 | 49,7 | 93,5 |
| 20 | Elastic Net (alpha=3, l1_ratio=0,5) | 85,9 | 52,8 | 83,9 | 52,2 | 92,5 |
| 21 | Elastic Net (alpha=3, l1_ratio=0,1) | 86,3 | 53,0 | 84,1 | 52,7 | 92,9 |
| 22 | Elastic Net (alpha=10, l1_ratio=0,9) | 89,0 | 54,3 | 85,1 | 55,0 | 94,7 |
| 23 | Elastic Net (alpha=10, l1_ratio=0,5) | 89,2 | 54,7 | 85,4 | 55,6 | 95,3 |
| 24 | Elastic Net (alpha=10, l1_ratio=0,1) | 89,0 | 54,8 | 85,6 | 55,6 | 95,5 |
| 25 | *Naive forecast* | 101,7 | 62,2 | 103,6 | 57,7 | 108,8 |
