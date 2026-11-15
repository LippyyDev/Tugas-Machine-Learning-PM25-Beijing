# Data Olahan

Fitur hasil tahap 2 untuk stasiun Tiantan, siap dipakai pada tahap berikutnya. Dibuat oleh `Notebook/Tahap 2 EDA dan Praproses.ipynb` dari `Data/Data Mentah/Tiantan.csv`. Berkas ini bisa dibuat ulang dengan menjalankan *notebook* itu, jadi jangan diedit manual.

## Ringkasan

| Item | Isi |
|---|---|
| Jumlah berkas | 2 CSV: `fitur_latih_Tiantan.csv` dan `fitur_uji_Tiantan.csv` |
| Stasiun | Tiantan |
| Target | PM2.5 pada 24 jam ke depan (jam *t*+24) |
| Batas latih dan uji | 2016-05-12 19:00, berdasarkan waktu jam *t* (20% jam terakhir menjadi data uji, tanpa diacak) |
| Kolom | `waktu`, `target`, dan 29 fitur |
| Nilai hilang | Sel kosong di CSV |

| Berkas | Baris | Rentang jam *t* |
|---|---|---|
| `fitur_latih_Tiantan.csv` | 27.443 | 2013-03-01 00:00 sampai 2016-05-11 18:00 |
| `fitur_uji_Tiantan.csv` | 6.896 | 2016-05-12 19:00 sampai 2017-02-27 23:00 |

## Kolom

| Kolom | Arti |
|---|---|
| `waktu` | Jam *t*, saat ramalan dibuat. Semua fitur hanya memakai data sampai jam ini |
| `target` | PM2.5 pada jam *t*+24 (µg/m³), nilai asli tanpa pengisian |
| `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3` | Polutan pada jam *t* |
| `TEMP`, `PRES`, `DEWP`, `RAIN`, `WSPM` | Cuaca pada jam *t*, satuan sama seperti `Data Mentah` |
| `PM2.5_lag1`, `_lag2`, `_lag3`, `_lag6`, `_lag12`, `_lag24`, `_lag48` | PM2.5 pada 1, 2, 3, 6, 12, 24, dan 48 jam sebelum jam *t* |
| `PM2.5_rata6j`, `_rata24j`, `_rata72j` | Rata-rata bergulir (*rolling mean*) PM2.5 pada 6, 24, dan 72 jam terakhir sampai jam *t*. Dihitung bila setidaknya separuh jendela terisi |
| `angin_sin`, `angin_cos` | Arah angin jam *t* (16 arah mata angin, tiap arah 22,5 derajat) dalam bentuk sinus dan kosinus |
| `jam_sin`, `jam_cos`, `hari_sin`, `hari_cos`, `bulan_sin`, `bulan_cos` | Jam, hari dalam pekan, dan bulan dalam bentuk sinus dan kosinus, agar jam 23 dekat dengan jam 0 |

## Aturan pemakaian

- **Hanya data sampai jam *t*.** Tidak ada interpolasi dan tidak ada nilai dari masa depan pada fitur.
- **Celah kebocoran sudah ditutup.** Baris latih yang targetnya jatuh di periode uji (24 jam terakhir sebelum batas) sudah dibuang.
- **Nilai kosong pada fitur belum diimputasi.** Tidak ada pengisian (tanpa *forward fill*, keputusan 15 Nov 2026). Pada berkas latih, 23 dari 29 fitur memiliki sel kosong, tertinggi `CO` 3,20%. Kolom `target` tidak ada yang kosong karena baris dengan target hilang sudah dibuang. Sisa nilai kosong diisi median di dalam *pipeline* pada setiap *fold*, jangan dihitung dari seluruh berkas.
- **`fitur_uji_Tiantan.csv` hanya disimpan.** Berkas ini dibuka satu kali pada evaluasi final. Jangan dipakai untuk memilih fitur, model, atau *hyperparameter*.
- **Tanpa *forward fill*.** Bila keputusan ini diubah, berkas ini dibuat ulang dengan menjalankan *notebook*.
- **Hanya Tiantan.** Stasiun uji ditetapkan Dingling. Fiturnya dibuat dengan fungsi `buat_fitur` yang sama di *notebook* saat tahap 7.

## Catatan

- Statistik pada berkas latih dihitung langsung dari berkas di folder ini.
- Berkas ini dan `Hasil/Gambar` serta `Hasil/Tabel` berasal dari eksekusi *notebook* yang sama (dijalankan ulang 15 Nov 2026 setelah keputusan tanpa *forward fill*).
