# Tabel Hasil Percobaan Tahap 5

Semua percobaan model lanjutan pada validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` di data latih 9 stasiun, diurutkan dari RMSE rata-rata terendah (terbaik) ke tertinggi (terburuk).

**Kriteria masuk tabel:** model dijalankan dan dilatih langsung pada data latih 9 stasiun yang digabung, dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*, sehingga punya nilai RMSE di kelima *fold*. Konfigurasi *tuning* acak yang hanya tercatat rata-rata dan simpangan baku (tanpa nilai tiap *fold*) tidak dimasukkan. Catatannya tetap ada di `Hasil/Tabel/t5_tabel_tuning.csv` dan `t5_tabel_tuning_putaran2.csv`. **Data uji tidak dibuka.** Angka berasal dari eksekusi `Notebook/Tahap 2 EDA dan Praproses.ipynb` (bagian 05.1, 05.5, dan 05.7) dan digabung oleh `Notebook/bangun_tabel_hasil_percobaan.py` dari CSV di `Hasil/Tabel/`. Berkas CSV gabungan: `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.

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

## Tabel 1. Ringkasan, urut dari terbaik ke terburuk (73 konfigurasi)

| No | Konfigurasi | Fitur | RMSE | sd RMSE | MSE | MAE | sd MAE | Perbaikan vs *naive* (%) | *Fold* lebih baik dari *naive* | Selisih RMSE vs Ridge `alpha=1` (sd selisih) | *Fold* lebih baik dari Ridge | Sumber |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Ridge + Random forest putaran 2 terbaik | F3 (F2 + lintas stasiun) | 71,09 | 19,40 | 5354 | 52,71 | 13,13 | 18,1 | 5 dari 5 | -1,85 (0,59) | 5 dari 5 | 05.5 (langkah 6 putaran 2) |
| 2 | Ridge + Random forest + Extra Trees terbaik | F3 (F2 + lintas stasiun) | 71,10 | 19,44 | 5358 | 52,78 | 13,15 | 18,1 | 5 dari 5 | -1,84 (0,63) | 5 dari 5 | 05.5 (langkah 6 putaran 2) |
| 3 | Ridge + Random forest terpilih | F3 (F2 + lintas stasiun) | 71,12 | 19,32 | 5357 | 52,71 | 13,09 | 18,1 | 5 dari 5 | -1,82 (0,57) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 4 | Ridge + HGB + Random forest terpilih | F3 (F2 + lintas stasiun) | 71,14 | 19,26 | 5358 | 52,76 | 13,07 | 18,1 | 5 dari 5 | -1,80 (0,73) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 5 | Elastic Net + HGB + Random forest terpilih | F3 (F2 + lintas stasiun) | 71,16 | 19,23 | 5359 | 52,80 | 13,08 | 18,0 | 5 dari 5 | -1,79 (0,78) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 6 | Ridge + Extra Trees terbaik | F3 (F2 + lintas stasiun) | 71,27 | 19,40 | 5380 | 52,95 | 13,12 | 17,9 | 5 dari 5 | -1,68 (0,47) | 5 dari 5 | 05.5 (langkah 6 putaran 2) |
| 7 | Ridge + HGB terpilih | F3 (F2 + lintas stasiun) | 71,28 | 19,14 | 5375 | 52,95 | 13,00 | 17,9 | 5 dari 5 | -1,66 (0,67) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 8 | Random forest `{'min_samples_leaf': 100, 'max_features': 0.2, 'max_samples': 0.25}` | F3 (F2 + lintas stasiun) | 71,53 | 19,58 | 5423 | 52,99 | 13,27 | 17,6 | 5 dari 5 | -1,41 (1,10) | 4 dari 5 | 05.5 (langkah 6 putaran 2) |
| 9 | Random forest `{'min_samples_leaf': 300, 'max_features': 0.2, 'max_samples': 0.25}` | F3 (F2 + lintas stasiun) | 71,54 | 19,44 | 5420 | 53,19 | 13,25 | 17,6 | 5 dari 5 | -1,40 (1,28) | 5 dari 5 | 05.5 (langkah 6 putaran 2) |
| 10 | Elastic Net + HGB + Random forest terpilih | F2 (F1 + cuaca + statistik) | 71,61 | 19,30 | 5425 | 53,46 | 13,20 | 17,5 | 5 dari 5 | -1,33 (0,85) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 11 | Ridge + HGB + Random forest terpilih | F2 (F1 + cuaca + statistik) | 71,61 | 19,34 | 5427 | 53,42 | 13,18 | 17,5 | 5 dari 5 | -1,33 (0,78) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 12 | Random forest `{'min_samples_leaf': 300, 'max_features': 0.3, 'max_samples': 0.25}` | F3 (F2 + lintas stasiun) | 71,61 | 19,25 | 5425 | 53,14 | 13,13 | 17,5 | 5 dari 5 | -1,33 (1,13) | 5 dari 5 | 05.5 (langkah 6 putaran 2) |
| 13 | Ridge + Random forest terpilih | F2 (F1 + cuaca + statistik) | 71,64 | 19,50 | 5436 | 53,37 | 13,28 | 17,5 | 5 dari 5 | -1,30 (0,56) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 14 | Ridge + HGB terpilih | F2 (F1 + cuaca + statistik) | 71,73 | 19,22 | 5441 | 53,53 | 13,05 | 17,4 | 5 dari 5 | -1,21 (0,63) | 5 dari 5 | 05.5 (langkah 4 rata-rata) |
| 15 | Random forest terpilih | F3 (F2 + lintas stasiun) | 71,77 | 19,53 | 5456 | 53,06 | 13,24 | 17,3 | 5 dari 5 | -1,17 (1,16) | 4 dari 5 | 05.5 (langkah 3 tuning) |
| 16 | Random forest `{'min_samples_leaf': 300, 'max_features': 0.3, 'max_samples': 0.1}` | F3 (F2 + lintas stasiun) | 71,79 | 19,44 | 5456 | 53,39 | 13,22 | 17,3 | 5 dari 5 | -1,15 (1,67) | 3 dari 5 | 05.5 (langkah 6 putaran 2) |
| 17 | Extra Trees `{'min_samples_leaf': 50, 'max_features': 0.3}` | F3 (F2 + lintas stasiun) | 71,80 | 19,50 | 5459 | 53,46 | 13,17 | 17,3 | 5 dari 5 | -1,14 (0,84) | 4 dari 5 | 05.5 (langkah 6 putaran 2) |
| 18 | Extra Trees `{'min_samples_leaf': 100, 'max_features': 0.3}` | F3 (F2 + lintas stasiun) | 71,88 | 19,43 | 5468 | 53,71 | 13,17 | 17,2 | 5 dari 5 | -1,07 (1,13) | 4 dari 5 | 05.5 (langkah 6 putaran 2) |
| 19 | Rata-rata Ridge dan boosting (0,5) | F3 (F2 + lintas stasiun) | 71,92 | 19,90 | 5490 | 53,23 | 13,51 | 17,2 | 5 dari 5 | -1,02 (0,94) | 5 dari 5 | 05.5 (langkah 2 model) |
| 20 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F3 (F2 + lintas stasiun) | 71,93 | 19,30 | 5471 | 53,57 | 13,07 | 17,2 | 5 dari 5 | -1,01 (0,36) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 21 | HGB terpilih | F3 (F2 + lintas stasiun) | 72,08 | 19,30 | 5493 | 53,51 | 13,14 | 17,0 | 5 dari 5 | -0,87 (1,36) | 4 dari 5 | 05.5 (langkah 3 tuning) |
| 22 | Elastic Net (alpha=1, l1_ratio=0,9) | F1 (29 fitur awal) | 72,26 | 19,23 | 5518 | 54,43 | 13,31 | 16,8 | 5 dari 5 | -0,68 (0,84) | 3 dari 5 | 05.7 |
| 23 | Random forest terpilih | F2 (F1 + cuaca + statistik) | 72,27 | 19,63 | 5532 | 53,83 | 13,48 | 16,8 | 5 dari 5 | -0,67 (1,36) | 4 dari 5 | 05.5 (langkah 3 tuning) |
| 24 | Ridge | F3 (F2 + lintas stasiun) | 72,28 | 19,31 | 5522 | 53,84 | 13,01 | 16,7 | 5 dari 5 | -0,66 (0,34) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 25 | Rata-rata Ridge dan boosting (0,5) | F2 (F1 + cuaca + statistik) | 72,28 | 19,83 | 5540 | 53,85 | 13,42 | 16,7 | 5 dari 5 | -0,66 (1,00) | 4 dari 5 | 05.5 (langkah 2 model) |
| 26 | Random forest `{'min_samples_leaf': 1000, 'max_features': 0.3, 'max_samples': 0.25}` | F3 (F2 + lintas stasiun) | 72,29 | 19,53 | 5531 | 53,73 | 13,18 | 16,7 | 5 dari 5 | -0,65 (1,95) | 3 dari 5 | 05.5 (langkah 6 putaran 2) |
| 27 | Extra Trees `{'min_samples_leaf': 300, 'max_features': 0.3}` | F3 (F2 + lintas stasiun) | 72,33 | 19,49 | 5535 | 54,21 | 13,18 | 16,7 | 5 dari 5 | -0,61 (1,54) | 3 dari 5 | 05.5 (langkah 6 putaran 2) |
| 28 | HGB terpilih | F2 (F1 + cuaca + statistik) | 72,35 | 19,16 | 5528 | 54,11 | 13,12 | 16,7 | 5 dari 5 | -0,59 (1,64) | 4 dari 5 | 05.5 (langkah 3 tuning) |
| 29 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F2 (F1 + cuaca + statistik) | 72,44 | 19,50 | 5551 | 54,10 | 13,27 | 16,6 | 5 dari 5 | -0,51 (0,26) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 30 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + cuaca dinamis | 72,49 | 19,22 | 5550 | 54,22 | 12,94 | 16,5 | 5 dari 5 | -0,45 (0,35) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 31 | Elastic Net (alpha=0,1, l1_ratio=0,1) | F1 (29 fitur awal) | 72,51 | 19,34 | 5557 | 54,30 | 13,08 | 16,5 | 5 dari 5 | -0,43 (0,37) | 5 dari 5 | 05.7 |
| 32 | Elastic Net (alpha=1, l1_ratio=0,5) | F1 (29 fitur awal) | 72,53 | 19,37 | 5561 | 54,79 | 13,38 | 16,5 | 5 dari 5 | -0,41 (1,06) | 3 dari 5 | 05.1, 05.7 |
| 33 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + statistik PM dan polutan | 72,56 | 19,58 | 5572 | 54,23 | 13,30 | 16,4 | 5 dari 5 | -0,38 (0,25) | 5 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 34 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 (29 fitur awal) | 72,60 | 19,33 | 5570 | 54,35 | 13,04 | 16,4 | 5 dari 5 | -0,34 (0,26) | 5 dari 5 | 05.1, 05.7, 05.5 (langkah 1 ablasi fitur) |
| 35 | Random forest | F3 (F2 + lintas stasiun) | 72,71 | 19,79 | 5600 | 53,52 | 13,31 | 16,2 | 5 dari 5 | -0,23 (1,43) | 2 dari 5 | 05.5 (langkah 2 model) |
| 36 | Elastic Net (alpha=1, l1_ratio=0,1) | F1 (29 fitur awal) | 72,75 | 19,38 | 5593 | 55,07 | 13,37 | 16,2 | 5 dari 5 | -0,19 (1,19) | 2 dari 5 | 05.7 |
| 37 | Elastic Net (alpha=3, l1_ratio=0,9) | F1 (29 fitur awal) | 72,75 | 19,38 | 5593 | 55,32 | 13,63 | 16,2 | 5 dari 5 | -0,19 (1,37) | 2 dari 5 | 05.7 |
| 38 | Elastic Net (alpha=0,1, l1_ratio=0,9) | F1 (29 fitur awal) | 72,76 | 19,33 | 5594 | 54,47 | 12,99 | 16,2 | 5 dari 5 | -0,18 (0,13) | 5 dari 5 | 05.7 |
| 39 | Ridge (alpha=1000) | F1 (29 fitur awal) | 72,83 | 19,38 | 5605 | 54,51 | 13,00 | 16,1 | 5 dari 5 | -0,11 (0,09) | 5 dari 5 | 05.7 |
| 40 | Ridge | F1 + cuaca dinamis | 72,85 | 19,27 | 5604 | 54,50 | 12,85 | 16,1 | 5 dari 5 | -0,10 (0,18) | 3 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 41 | Elastic Net (alpha=0,01, l1_ratio=0,1) | F1 (29 fitur awal) | 72,85 | 19,37 | 5607 | 54,51 | 12,98 | 16,1 | 5 dari 5 | -0,09 (0,05) | 5 dari 5 | 05.7 |
| 42 | Ridge | F2 (F1 + cuaca + statistik) | 72,87 | 19,56 | 5617 | 54,42 | 13,22 | 16,1 | 5 dari 5 | -0,07 (0,32) | 2 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 43 | Elastic Net (alpha=0,01, l1_ratio=0,5) | F1 (29 fitur awal) | 72,88 | 19,38 | 5612 | 54,54 | 12,97 | 16,1 | 5 dari 5 | -0,06 (0,03) | 5 dari 5 | 05.1, 05.7 |
| 44 | Elastic Net (alpha=0,01, l1_ratio=0,9) | F1 (29 fitur awal) | 72,92 | 19,38 | 5618 | 54,56 | 12,97 | 16,0 | 5 dari 5 | -0,02 (0,01) | 5 dari 5 | 05.7 |
| 45 | Ridge (alpha=100) | F1 (29 fitur awal) | 72,93 | 19,39 | 5619 | 54,57 | 12,97 | 16,0 | 5 dari 5 | -0,01 (0,01) | 5 dari 5 | 05.7 |
| 46 | Ridge (alpha=10) | F1 (29 fitur awal) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | -0,00 (0,00) | 5 dari 5 | 05.7 |
| 47 | Ridge (alpha=1) | F1 (29 fitur awal) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | 0,00 (0,00) | 0 dari 5 | 05.1, 05.7, 05.5 (langkah 1 ablasi fitur) |
| 48 | Ridge (alpha=0,1) | F1 (29 fitur awal) | 72,94 | 19,39 | 5621 | 54,58 | 12,97 | 16,0 | 5 dari 5 | 0,00 (0,00) | 0 dari 5 | 05.7 |
| 49 | Rata-rata Ridge dan boosting (0,5) | F1 (29 fitur awal) | 72,97 | 19,81 | 5638 | 54,05 | 13,11 | 16,0 | 5 dari 5 | 0,03 (1,64) | 3 dari 5 | 05.5 (langkah 2 model) |
| 50 | Ridge | F1 + statistik PM dan polutan | 72,98 | 19,65 | 5635 | 54,50 | 13,25 | 15,9 | 5 dari 5 | 0,04 (0,35) | 1 dari 5 | 05.5 (langkah 1 ablasi fitur) |
| 51 | HGB terpilih, target akar kuadrat | F3 (F2 + lintas stasiun) | 73,00 | 20,40 | 5661 | 51,86 | 13,37 | 15,9 | 5 dari 5 | 0,06 (1,32) | 3 dari 5 | 05.5 (langkah 5 transformasi target) |
| 52 | Random forest `{'min_samples_leaf': 1000, 'max_features': 0.2, 'max_samples': 0.1}` | F3 (F2 + lintas stasiun) | 73,05 | 19,83 | 5650 | 54,58 | 13,16 | 15,9 | 5 dari 5 | 0,10 (2,65) | 2 dari 5 | 05.5 (langkah 6 putaran 2) |
| 53 | Random forest | F2 (F1 + cuaca + statistik) | 73,21 | 19,96 | 5679 | 54,34 | 13,66 | 15,7 | 5 dari 5 | 0,27 (1,92) | 2 dari 5 | 05.5 (langkah 2 model) |
| 54 | Elastic Net (alpha=3, l1_ratio=0,5) | F1 (29 fitur awal) | 73,45 | 19,39 | 5695 | 55,99 | 13,35 | 15,4 | 5 dari 5 | 0,51 (1,48) | 2 dari 5 | 05.7 |
| 55 | Elastic Net (alpha=3, l1_ratio=0,1) | F1 (29 fitur awal) | 73,81 | 19,39 | 5749 | 56,34 | 13,26 | 15,0 | 5 dari 5 | 0,87 (1,51) | 2 dari 5 | 05.7 |
| 56 | Ridge, target akar kuadrat | F3 (F2 + lintas stasiun) | 73,84 | 21,34 | 5817 | 52,44 | 13,52 | 14,9 | 5 dari 5 | 0,90 (2,11) | 2 dari 5 | 05.5 (langkah 5 transformasi target) |
| 57 | HGB terpilih, target akar kuadrat | F2 (F1 + cuaca + statistik) | 73,96 | 20,86 | 5818 | 52,77 | 13,89 | 14,8 | 5 dari 5 | 1,02 (1,68) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 58 | Ridge, target akar kuadrat | F2 (F1 + cuaca + statistik) | 74,44 | 21,66 | 5917 | 53,00 | 13,76 | 14,3 | 5 dari 5 | 1,50 (2,43) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 59 | Ridge lalu boosting pada residual | F3 (F2 + lintas stasiun) | 74,59 | 22,21 | 5958 | 54,68 | 14,20 | 14,1 | 5 dari 5 | 1,65 (3,04) | 1 dari 5 | 05.5 (langkah 2 model) |
| 60 | Gradient boosting | F2 (F1 + cuaca + statistik) | 75,24 | 21,19 | 6020 | 55,73 | 14,41 | 13,3 | 5 dari 5 | 2,30 (2,89) | 1 dari 5 | 05.5 (langkah 2 model) |
| 61 | Gradient boosting | F3 (F2 + lintas stasiun) | 75,37 | 21,92 | 6066 | 55,22 | 14,87 | 13,2 | 5 dari 5 | 2,43 (3,26) | 1 dari 5 | 05.5 (langkah 2 model) |
| 62 | Ridge lalu boosting pada residual | F2 (F1 + cuaca + statistik) | 75,58 | 22,05 | 6102 | 55,85 | 14,28 | 12,9 | 5 dari 5 | 2,64 (3,25) | 1 dari 5 | 05.5 (langkah 2 model) |
| 63 | Elastic Net (alpha=10, l1_ratio=0,9) | F1 (29 fitur awal) | 75,63 | 19,44 | 6022 | 57,89 | 12,74 | 12,9 | 5 dari 5 | 2,69 (1,93) | 0 dari 5 | 05.7 |
| 64 | Elastic Net (alpha=10, l1_ratio=0,5) | F1 (29 fitur awal) | 76,02 | 19,40 | 6080 | 58,22 | 12,61 | 12,4 | 5 dari 5 | 3,08 (1,93) | 0 dari 5 | 05.7 |
| 65 | Elastic Net (alpha=10, l1_ratio=0,1) | F1 (29 fitur awal) | 76,09 | 19,41 | 6092 | 58,34 | 12,68 | 12,4 | 5 dari 5 | 3,15 (1,84) | 0 dari 5 | 05.7 |
| 66 | Ridge lalu boosting pada residual | F1 (29 fitur awal) | 76,71 | 22,01 | 6272 | 55,81 | 14,31 | 11,6 | 5 dari 5 | 3,77 (4,88) | 2 dari 5 | 05.5 (langkah 2 model) |
| 67 | Gradient boosting (*early stopping* bawaan) | F1 (29 fitur awal) | 76,97 | 21,75 | 6302 | 56,04 | 14,07 | 11,3 | 5 dari 5 | 4,03 (4,79) | 1 dari 5 | 05.1 |
| 68 | Gradient boosting (200 iterasi, kedalaman 4) | F1 (29 fitur awal) | 77,10 | 22,10 | 6335 | 56,11 | 14,50 | 11,2 | 5 dari 5 | 4,16 (5,84) | 1 dari 5 | 05.1, 05.5 (langkah 2 model) |
| 69 | HGB terpilih, target log1p | F3 (F2 + lintas stasiun) | 77,51 | 22,64 | 6418 | 52,12 | 13,90 | 10,7 | 5 dari 5 | 4,57 (4,07) | 0 dari 5 | 05.5 (langkah 5 transformasi target) |
| 70 | HGB terpilih, target log1p | F2 (F1 + cuaca + statistik) | 77,82 | 22,77 | 6471 | 52,74 | 14,10 | 10,4 | 5 dari 5 | 4,88 (4,60) | 0 dari 5 | 05.5 (langkah 5 transformasi target) |
| 71 | Ridge, target log1p | F3 (F2 + lintas stasiun) | 79,59 | 24,61 | 6819 | 53,44 | 14,68 | 8,3 | 5 dari 5 | 6,65 (5,33) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 72 | Ridge, target log1p | F2 (F1 + cuaca + statistik) | 80,10 | 25,06 | 6918 | 53,85 | 14,94 | 7,7 | 5 dari 5 | 7,16 (5,77) | 1 dari 5 | 05.5 (langkah 5 transformasi target) |
| 73 | *Naive forecast* | n/a | 86,82 | 24,70 | 8025 | 59,39 | 16,53 | 0,0 | 0 dari 5 | 13,88 (5,95) | 0 dari 5 | 05.1 |

## Tabel 2. RMSE tiap *fold*, urutan sama dengan Tabel 1

| No | Konfigurasi | *Fold* 1 | *Fold* 2 | *Fold* 3 | *Fold* 4 | *Fold* 5 |
|---|---|---|---|---|---|---|
| 1 | Ridge + Random forest putaran 2 terbaik | 83,3 | 52,5 | 80,9 | 48,0 | 90,6 |
| 2 | Ridge + Random forest + Extra Trees terbaik | 83,6 | 52,3 | 80,9 | 48,1 | 90,6 |
| 3 | Ridge + Random forest terpilih | 83,2 | 52,6 | 81,0 | 48,1 | 90,6 |
| 4 | Ridge + HGB + Random forest terpilih | 83,4 | 52,7 | 81,2 | 48,2 | 90,3 |
| 5 | Elastic Net + HGB + Random forest terpilih | 83,5 | 52,6 | 81,2 | 48,3 | 90,2 |
| 6 | Ridge + Extra Trees terbaik | 83,5 | 52,4 | 81,1 | 48,5 | 90,9 |
| 7 | Ridge + HGB terpilih | 83,0 | 52,9 | 81,5 | 48,6 | 90,5 |
| 8 | Random forest `{'min_samples_leaf': 100, 'max_features': 0.2, 'max_samples': 0.25}` | 84,7 | 52,9 | 81,3 | 48,0 | 90,7 |
| 9 | Random forest `{'min_samples_leaf': 300, 'max_features': 0.2, 'max_samples': 0.25}` | 84,4 | 52,4 | 82,3 | 48,6 | 90,0 |
| 10 | Elastic Net + HGB + Random forest terpilih | 84,2 | 53,1 | 81,4 | 48,6 | 90,7 |
| 11 | Ridge + HGB + Random forest terpilih | 84,1 | 53,2 | 81,4 | 48,5 | 90,8 |
| 12 | Random forest `{'min_samples_leaf': 300, 'max_features': 0.3, 'max_samples': 0.25}` | 84,2 | 52,9 | 82,1 | 48,7 | 90,1 |
| 13 | Ridge + Random forest terpilih | 83,9 | 53,1 | 81,4 | 48,3 | 91,4 |
| 14 | Ridge + HGB terpilih | 83,9 | 53,3 | 81,6 | 48,9 | 91,0 |
| 15 | Random forest terpilih | 85,1 | 53,2 | 81,5 | 48,3 | 90,8 |
| 16 | Random forest `{'min_samples_leaf': 300, 'max_features': 0.3, 'max_samples': 0.1}` | 85,0 | 52,2 | 82,8 | 49,2 | 89,7 |
| 17 | Extra Trees `{'min_samples_leaf': 50, 'max_features': 0.3}` | 84,7 | 52,7 | 81,4 | 49,0 | 91,2 |
| 18 | Extra Trees `{'min_samples_leaf': 100, 'max_features': 0.3}` | 85,0 | 52,6 | 81,9 | 49,2 | 90,6 |
| 19 | Rata-rata Ridge dan boosting (0,5) | 84,4 | 53,6 | 81,8 | 47,7 | 92,2 |
| 20 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 83,7 | 53,0 | 81,8 | 49,4 | 91,7 |
| 21 | HGB terpilih | 85,3 | 53,5 | 82,2 | 49,0 | 90,4 |
| 22 | Elastic Net (alpha=1, l1_ratio=0,9) | 84,1 | 52,7 | 82,6 | 50,4 | 91,6 |
| 23 | Random forest terpilih | 85,8 | 54,0 | 82,0 | 48,4 | 91,2 |
| 24 | Ridge | 83,9 | 53,8 | 82,1 | 49,4 | 92,1 |
| 25 | Rata-rata Ridge dan boosting (0,5) | 85,0 | 54,1 | 81,4 | 48,2 | 92,7 |
| 26 | Random forest `{'min_samples_leaf': 1000, 'max_features': 0.3, 'max_samples': 0.25}` | 86,3 | 52,3 | 82,9 | 49,9 | 90,0 |
| 27 | Extra Trees `{'min_samples_leaf': 300, 'max_features': 0.3}` | 85,9 | 52,5 | 82,6 | 50,0 | 90,7 |
| 28 | HGB terpilih | 86,1 | 54,0 | 82,0 | 49,4 | 90,3 |
| 29 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,3 | 53,4 | 82,3 | 49,7 | 92,5 |
| 30 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,6 | 82,2 | 50,2 | 92,3 |
| 31 | Elastic Net (alpha=0,1, l1_ratio=0,1) | 84,1 | 53,3 | 82,4 | 50,3 | 92,5 |
| 32 | Elastic Net (alpha=1, l1_ratio=0,5) | 84,5 | 52,4 | 83,0 | 50,9 | 91,9 |
| 33 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,5 | 82,5 | 49,7 | 92,9 |
| 34 | Elastic Net (alpha=0,1, l1_ratio=0,5) | 84,2 | 53,5 | 82,4 | 50,2 | 92,7 |
| 35 | Random forest | 86,2 | 54,5 | 82,6 | 48,4 | 91,8 |
| 36 | Elastic Net (alpha=1, l1_ratio=0,1) | 84,8 | 52,5 | 83,3 | 51,2 | 92,0 |
| 37 | Elastic Net (alpha=3, l1_ratio=0,9) | 85,2 | 52,3 | 83,2 | 51,3 | 91,7 |
| 38 | Elastic Net (alpha=0,1, l1_ratio=0,9) | 84,3 | 53,9 | 82,4 | 50,3 | 92,9 |
| 39 | Ridge (alpha=1000) | 84,3 | 54,0 | 82,4 | 50,3 | 93,2 |
| 40 | Ridge | 84,5 | 54,2 | 82,4 | 50,3 | 92,9 |
| 41 | Elastic Net (alpha=0,01, l1_ratio=0,1) | 84,4 | 54,0 | 82,4 | 50,3 | 93,1 |
| 42 | Ridge | 84,6 | 54,3 | 82,6 | 49,7 | 93,1 |
| 43 | Elastic Net (alpha=0,01, l1_ratio=0,5) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 44 | Elastic Net (alpha=0,01, l1_ratio=0,9) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 45 | Ridge (alpha=100) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 46 | Ridge (alpha=10) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 47 | Ridge (alpha=1) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 48 | Ridge (alpha=0,1) | 84,5 | 54,1 | 82,5 | 50,3 | 93,2 |
| 49 | Rata-rata Ridge dan boosting (0,5) | 86,7 | 55,3 | 81,3 | 48,6 | 93,0 |
| 50 | Ridge | 84,6 | 54,3 | 82,8 | 49,7 | 93,5 |
| 51 | HGB terpilih, target akar kuadrat | 83,9 | 53,9 | 83,1 | 48,9 | 95,3 |
| 52 | Random forest `{'min_samples_leaf': 1000, 'max_features': 0.2, 'max_samples': 0.1}` | 88,6 | 52,5 | 83,2 | 50,6 | 90,4 |
| 53 | Random forest | 87,7 | 55,0 | 82,8 | 48,6 | 92,1 |
| 54 | Elastic Net (alpha=3, l1_ratio=0,5) | 85,9 | 52,8 | 83,9 | 52,2 | 92,5 |
| 55 | Elastic Net (alpha=3, l1_ratio=0,1) | 86,3 | 53,0 | 84,1 | 52,7 | 92,9 |
| 56 | Ridge, target akar kuadrat | 87,1 | 54,0 | 83,2 | 48,3 | 96,5 |
| 57 | HGB terpilih, target akar kuadrat | 86,1 | 54,9 | 83,6 | 48,8 | 96,4 |
| 58 | Ridge, target akar kuadrat | 87,8 | 54,4 | 83,9 | 48,5 | 97,6 |
| 59 | Ridge lalu boosting pada residual | 87,6 | 54,8 | 84,6 | 47,4 | 98,5 |
| 60 | Gradient boosting | 91,0 | 56,7 | 83,8 | 48,7 | 96,0 |
| 61 | Gradient boosting | 91,3 | 55,9 | 85,4 | 48,0 | 96,3 |
| 62 | Ridge lalu boosting pada residual | 89,0 | 56,5 | 83,8 | 48,5 | 100,1 |
| 63 | Elastic Net (alpha=10, l1_ratio=0,9) | 89,0 | 54,3 | 85,1 | 55,0 | 94,7 |
| 64 | Elastic Net (alpha=10, l1_ratio=0,5) | 89,2 | 54,7 | 85,4 | 55,6 | 95,3 |
| 65 | Elastic Net (alpha=10, l1_ratio=0,1) | 89,0 | 54,8 | 85,6 | 55,6 | 95,5 |
| 66 | Ridge lalu boosting pada residual | 96,0 | 57,9 | 82,4 | 49,5 | 97,7 |
| 67 | Gradient boosting (*early stopping* bawaan) | 95,7 | 59,5 | 83,3 | 49,0 | 97,3 |
| 68 | Gradient boosting (200 iterasi, kedalaman 4) | 98,1 | 59,5 | 83,0 | 48,8 | 96,2 |
| 69 | HGB terpilih, target log1p | 87,1 | 57,3 | 88,2 | 50,7 | 104,3 |
| 70 | HGB terpilih, target log1p | 86,2 | 58,1 | 89,0 | 50,6 | 105,2 |
| 71 | Ridge, target log1p | 94,9 | 57,2 | 90,2 | 49,8 | 105,8 |
| 72 | Ridge, target log1p | 95,2 | 57,4 | 91,1 | 49,8 | 107,0 |
| 73 | *Naive forecast* | 101,7 | 62,2 | 103,6 | 57,7 | 108,8 |
