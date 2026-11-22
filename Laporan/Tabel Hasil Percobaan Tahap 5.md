# Tabel Hasil Percobaan Tahap 5

Percobaan model lanjutan pada validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` di data latih 9 stasiun, urut dari RMSE rata-rata terendah. Tabel hanya memuat konfigurasi yang dilatih langsung pada 9 stasiun dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*, dan hanya tingkat kesulitan 1 (Mudah) atas permintaan penulis (22 Nov 2026). **Data uji tidak dibuka.** Dua model yang dipakai di *notebook* Tahap 5 ditebalkan.

## Tabel (25 konfigurasi)

| No | Konfigurasi | Fitur | RMSE | sd RMSE | MAE | Perbaikan vs *naive* (%) | *Fold* lebih baik dari *naive* |
|---|---|---|---|---|---|---|---|
| 1 | **Elastic Net (alpha=1, l1_ratio=0,9), pembanding** | F1 (29 fitur awal) | 72,26 | 19,23 | 54,43 | 16,8 | 5 dari 5 |
| 2 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + cuaca dinamis | 72,49 | 19,22 | 54,22 | 16,5 | 5 dari 5 |
| 3 | Elastic Net (alpha=0,1, l1_ratio=0,1) | F1 (29 fitur awal) | 72,51 | 19,34 | 54,30 | 16,5 | 5 dari 5 |
| 4 | Elastic Net (alpha=1, l1_ratio=0,5) | F1 (29 fitur awal) | 72,53 | 19,37 | 54,79 | 16,5 | 5 dari 5 |
| 5 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 + statistik PM dan polutan | 72,56 | 19,58 | 54,23 | 16,4 | 5 dari 5 |
| 6 | Elastic Net (alpha=0,1, l1_ratio=0,5) | F1 (29 fitur awal) | 72,60 | 19,33 | 54,35 | 16,4 | 5 dari 5 |
| 7 | Elastic Net (alpha=1, l1_ratio=0,1) | F1 (29 fitur awal) | 72,75 | 19,38 | 55,07 | 16,2 | 5 dari 5 |
| 8 | Elastic Net (alpha=3, l1_ratio=0,9) | F1 (29 fitur awal) | 72,75 | 19,38 | 55,32 | 16,2 | 5 dari 5 |
| 9 | Elastic Net (alpha=0,1, l1_ratio=0,9) | F1 (29 fitur awal) | 72,76 | 19,33 | 54,47 | 16,2 | 5 dari 5 |
| 10 | **Ridge (alpha=1000), model utama** | F1 (29 fitur awal) | 72,83 | 19,38 | 54,51 | 16,1 | 5 dari 5 |
| 11 | Ridge | F1 + cuaca dinamis | 72,85 | 19,27 | 54,50 | 16,1 | 5 dari 5 |
| 12 | Elastic Net (alpha=0,01, l1_ratio=0,1) | F1 (29 fitur awal) | 72,85 | 19,37 | 54,51 | 16,1 | 5 dari 5 |
| 13 | Elastic Net (alpha=0,01, l1_ratio=0,5) | F1 (29 fitur awal) | 72,88 | 19,38 | 54,54 | 16,1 | 5 dari 5 |
| 14 | Elastic Net (alpha=0,01, l1_ratio=0,9) | F1 (29 fitur awal) | 72,92 | 19,38 | 54,56 | 16,0 | 5 dari 5 |
| 15 | Ridge (alpha=100) | F1 (29 fitur awal) | 72,93 | 19,39 | 54,57 | 16,0 | 5 dari 5 |
| 16 | Ridge (alpha=10) | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 17 | Ridge (alpha=1) | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 18 | Ridge (alpha=0,1) | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 19 | Ridge | F1 + statistik PM dan polutan | 72,98 | 19,65 | 54,50 | 15,9 | 5 dari 5 |
| 20 | Elastic Net (alpha=3, l1_ratio=0,5) | F1 (29 fitur awal) | 73,45 | 19,39 | 55,99 | 15,4 | 5 dari 5 |
| 21 | Elastic Net (alpha=3, l1_ratio=0,1) | F1 (29 fitur awal) | 73,81 | 19,39 | 56,34 | 15,0 | 5 dari 5 |
| 22 | Elastic Net (alpha=10, l1_ratio=0,9) | F1 (29 fitur awal) | 75,63 | 19,44 | 57,89 | 12,9 | 5 dari 5 |
| 23 | Elastic Net (alpha=10, l1_ratio=0,5) | F1 (29 fitur awal) | 76,02 | 19,40 | 58,22 | 12,4 | 5 dari 5 |
| 24 | Elastic Net (alpha=10, l1_ratio=0,1) | F1 (29 fitur awal) | 76,09 | 19,41 | 58,34 | 12,4 | 5 dari 5 |
| 25 | *Naive forecast* | n/a | 86,82 | 24,70 | 59,39 | 0,0 | 0 dari 5 |

## Cara membaca

* **RMSE** dan **MAE** adalah rata-rata 5 *fold* (µg/m³, makin kecil makin baik). **sd RMSE** adalah simpangan baku antar *fold*, yaitu sebaran kesulitan antar periode. Perbaikan dihitung terhadap RMSE *naive forecast* 86,82.
* Selisih antar hampir semua konfigurasi jauh di bawah sd RMSE (sekitar 19), jadi urutan **tidak berarti** peringkat yang berdekatan berbeda nyata.
* Skor dipilih dari puluhan konfigurasi pada lima *fold* yang sama, sehingga optimistis dan bukan kinerja akhir. Kinerja akhir hanya dari data uji, satu kali.
* Tingkat kesulitan memakai rubrik **[Usulan]** dari struktur konfigurasi saja, tanpa melihat RMSE (lihat kolom skor di `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`). Tingkat 1 berarti *naive* atau model linear (Ridge, Elastic Net) dengan F1 atau F1 ditambah satu kelompok fitur, tanpa penggabungan model, *tuning* acak, atau transformasi target.

## Yang tidak ditampilkan

Konfigurasi tingkat 2 sampai 4 (48 konfigurasi) dikeluarkan dari tabel. Ringkasannya, dihitung sebelum dikeluarkan:

| Tingkat | Jumlah konfigurasi | RMSE terbaik | RMSE median | RMSE terburuk |
|---|---|---|---|---|
| 1 Mudah | 24 | 72,26 | 72,87 | 76,09 |
| 2 Sedang | 8 | 71,93 | 73,66 | 80,10 |
| 3 Sulit | 14 | 71,92 | 73,53 | 79,59 |
| 4 Sangat sulit | 26 | 71,09 | 71,68 | 77,82 |

RMSE terbaik tingkat 1 (selain *naive*) adalah 72,26, sedangkan tingkat 4 terbaik 71,09. Selisih sekitar 1,18 (1,6%) jauh di bawah sd antar *fold*, jadi model yang lebih sulit tidak sepadan dengan beban implementasi dan penjelasannya. Nilai per *fold* semuanya ada di `Hasil/Tabel/t5_tabel_eksperimen_per_fold.csv`, dan tabel lengkap tiap *fold* untuk yang tampil ada di `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.
