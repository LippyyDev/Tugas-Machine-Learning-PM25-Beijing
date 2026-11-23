# Tabel Hasil Percobaan Tahap 5

Hasil validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` pada data latih 9 stasiun, urut dari RMSE rata-rata terendah. Semua konfigurasi dilatih langsung pada 9 stasiun dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*. **Data uji tidak dibuka.** Model lanjutan yang dipakai di Tahap 5 ditebalkan.

## Tabel (8 konfigurasi)

| No | Konfigurasi | Fitur | RMSE | sd RMSE | MAE | Perbaikan vs *naive* (%) | *Fold* lebih baik dari *naive* |
|---|---|---|---|---|---|---|---|
| 1 | **Ridge (alpha=1000), model lanjutan** | F1 (29 fitur awal) | 72,83 | 19,38 | 54,52 | 16,1 | 5 dari 5 |
| 2 | Ridge | F1 + cuaca dinamis | 72,85 | 19,27 | 54,50 | 16,1 | 5 dari 5 |
| 3 | Ridge (alpha=100) | F1 (29 fitur awal) | 72,93 | 19,39 | 54,57 | 16,0 | 5 dari 5 |
| 4 | Ridge (alpha=10) | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 5 | Ridge (alpha=1) | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 6 | Ridge (alpha=0,1) | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 7 | Ridge | F1 + statistik PM dan polutan | 72,98 | 19,65 | 54,50 | 15,9 | 5 dari 5 |
| 8 | *Naive forecast* |  | 86,82 | 24,70 | 59,39 | 0,0 | 0 dari 5 |

## Cara membaca

* **RMSE** dan **MAE** adalah rata-rata 5 *fold* (µg/m³, makin kecil makin baik). **sd RMSE** adalah simpangan baku antar *fold*, yaitu sebaran kesulitan antar periode. Perbaikan dihitung terhadap RMSE *naive forecast* 86,82.
* Selisih antar konfigurasi Ridge jauh di bawah sd RMSE (sekitar 19), jadi urutan **tidak berarti** peringkat yang berdekatan berbeda nyata.
* Skor dipilih dari beberapa konfigurasi pada lima *fold* yang sama, sehingga optimistis dan bukan kinerja akhir. Kinerja akhir hanya dari data uji, satu kali.
* Dua baris dengan fitur tambahan (cuaca dinamis, statistik PM dan polutan) berasal dari percobaan lama. Kodenya tidak ada lagi di *notebook*, tetapi ada di riwayat Git.
* Nilai tiap *fold* ada di `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.
