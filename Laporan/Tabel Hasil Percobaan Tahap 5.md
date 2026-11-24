# Tabel Hasil Percobaan Tahap 5

Hasil validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` pada data latih 9 stasiun, dikelompokkan per model dan diurutkan dari RMSE rata-rata terendah di dalam tiap kelompok. Semua konfigurasi dilatih langsung pada 9 stasiun dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*. **Data uji tidak dibuka.** Model lanjutan yang dipakai di Tahap 5 ditebalkan. Pembanding Ridge adalah *random forest*, dengan *grid* 6 konfigurasi yang ditetapkan sebelum dijalankan.

## Tabel (14 konfigurasi)

| No | Konfigurasi | Fitur | RMSE | sd RMSE | MAE | Perbaikan vs *naive* (%) | *Fold* lebih baik dari *naive* |
|---|---|---|---|---|---|---|---|
| | **Ridge** | | | | | | |
| 1 | **`alpha=1000`, model lanjutan** | F1 (29 fitur awal) | 72,83 | 19,38 | 54,52 | 16,1 | 5 dari 5 |
| 2 | `alpha=1000` | F1 + cuaca dinamis | 72,85 | 19,27 | 54,50 | 16,1 | 5 dari 5 |
| 3 | `alpha=100` | F1 (29 fitur awal) | 72,93 | 19,39 | 54,57 | 16,0 | 5 dari 5 |
| 4 | `alpha=10` | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 5 | `alpha=1` | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 6 | `alpha=0,1` | F1 (29 fitur awal) | 72,94 | 19,39 | 54,58 | 16,0 | 5 dari 5 |
| 7 | `alpha=1000` | F1 + statistik PM dan polutan | 72,98 | 19,65 | 54,50 | 15,9 | 5 dari 5 |
| | ***Random forest*** | | | | | | |
| 1 | **`min_samples_leaf=200`, `max_features=0,33`, pembanding** | F1 (29 fitur awal) | 72,91 | 19,39 | 54,38 | 16,0 | 5 dari 5 |
| 2 | `min_samples_leaf=50`, `max_features=0,33` | F1 (29 fitur awal) | 73,69 | 19,76 | 54,66 | 15,1 | 5 dari 5 |
| 3 | `min_samples_leaf=200`, `max_features=0,60` | F1 (29 fitur awal) | 73,97 | 19,46 | 54,98 | 14,8 | 5 dari 5 |
| 4 | `min_samples_leaf=10`, `max_features=0,33` | F1 (29 fitur awal) | 74,32 | 19,73 | 54,99 | 14,4 | 5 dari 5 |
| 5 | `min_samples_leaf=50`, `max_features=0,60` | F1 (29 fitur awal) | 75,21 | 19,86 | 55,52 | 13,4 | 5 dari 5 |
| 6 | `min_samples_leaf=10`, `max_features=0,60` | F1 (29 fitur awal) | 75,79 | 19,78 | 55,91 | 12,7 | 5 dari 5 |
| | ***Naive forecast*** | | | | | | |
| 1 | tanpa parameter | PM2.5 jam t | 86,82 | 24,70 | 59,39 | 0,0 | 0 dari 5 |

## Cara membaca

* **RMSE** dan **MAE** adalah rata-rata 5 *fold* (µg/m³, makin kecil makin baik). **sd RMSE** adalah simpangan baku antar *fold*. Perbaikan dihitung terhadap RMSE *naive forecast* 86,82.
* **Ridge dan *random forest* tidak terbedakan.** Selisih RMSE berpasangan (RF dikurangi Ridge) rata-rata 0,08 dengan sd 1,15, dan RF lebih baik di 3 dari 5 *fold*. Selisih antar konfigurasi lain juga jauh di bawah sd RMSE (sekitar 19), jadi urutan tidak berarti peringkat yang berdekatan berbeda nyata.
* Optimum RF ada di tepi *grid* (`min_samples_leaf=200`, `max_features=0,33`), dan *grid* tidak diperluas. RF terpilih belum tentu RF terbaik. Eksperimen lama 22 Nov yang memuat RF pernah dilihat, sehingga *tuning* tidak sepenuhnya buta.
* Skor dipilih dari beberapa konfigurasi pada lima *fold* yang sama, sehingga optimistis dan bukan kinerja akhir. Kinerja akhir hanya dari data uji, satu kali.
* Dua baris Ridge dengan fitur tambahan berasal dari percobaan lama. Kodenya tidak ada lagi di *notebook*, tetapi ada di riwayat Git.
* Rincian tiap *fold*, *seed*, dan galat menurut rentang konsentrasi ada di `Hasil/Tabel/` (`t5_tabel_tuning_rf*.csv`, `t5_tabel_rf_vs_ridge*.csv`, `t5_tabel_rf_seed.csv`, `t5_tabel_galat_rentang.csv`, `t5_tabel_semua_eksperimen.csv`). Bagian *notebook*: 05.3 sampai 05.7.
