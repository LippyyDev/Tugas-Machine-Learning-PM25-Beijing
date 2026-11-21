# Data Olahan

Folder ini sengaja kosong sampai `Notebook/Tahap 2 EDA dan Praproses.ipynb` dijalankan. Dua berkas hasil pilot Tiantan dihapus 16 Nov 2026 karena desain evaluasi berubah menjadi 9 stasiun latih dan 3 stasiun uji. Berkas baru tidak di-*commit* (sekitar 77 MB dan 27 MB, diabaikan lewat `.gitignore`), jadi buat ulang dengan menjalankan *notebook* dari awal. Jangan diedit manual.

## Berkas yang dibuat *notebook*

| Berkas | Isi | Baris (uji coba 16 Nov 2026) |
|---|---|---|
| `fitur_latih.csv` | 9 stasiun latih, jam *t* dengan target (jam *t*+24) sebelum 2016-05-12 19:00 | 246.798 |
| `fitur_uji.csv` | 12 stasiun, jam *t* sejak 2016-05-12 19:00, dengan kolom `kelompok_uji` | 82.151 (61.686 stasiun latih, 20.465 stasiun uji) |

Baris 3 stasiun uji sebelum batas waktu tidak disimpan (tidak dipakai). Tiga stasiun uji: Dingling, Wanliu, dan Shunyi (keputusan penulis 16 Nov 2026, ditetapkan di *notebook* 02.2 dan dicek terhadap aturan urutan jarak ke-1, ke-6, dan ke-12).

## Kolom

| Kolom | Arti |
|---|---|
| `waktu` | Jam *t*, saat prediksi dibuat. Semua fitur hanya memakai data sampai jam ini |
| `stasiun` | Nama stasiun, untuk pelaporan. **Bukan fitur** |
| `kelompok_uji` | Hanya di `fitur_uji.csv`: `stasiun_latih` atau `stasiun_uji`. **Bukan fitur** |
| `target` | PM2.5 pada jam *t*+24 di stasiun yang sama (µg/m³), nilai asli tanpa pengisian |
| `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3` | Polutan pada jam *t* |
| `TEMP`, `PRES`, `DEWP`, `RAIN`, `WSPM` | Cuaca pada jam *t*, satuan sama seperti `Data Mentah` |
| `PM2.5_lag1`, `_lag2`, `_lag3`, `_lag6`, `_lag12`, `_lag24`, `_lag48` | PM2.5 pada 1, 2, 3, 6, 12, 24, dan 48 jam sebelum jam *t*, di stasiun yang sama |
| `PM2.5_rata6j`, `_rata24j`, `_rata72j` | *Rolling mean* PM2.5 pada 6, 24, dan 72 jam terakhir sampai jam *t*. Dihitung bila setidaknya separuh jendela terisi |
| `angin_sin`, `angin_cos` | Arah angin jam *t* (16 arah mata angin, tiap arah 22,5 derajat) dalam bentuk sinus dan kosinus |
| `jam_sin`, `jam_cos`, `hari_sin`, `hari_cos`, `bulan_sin`, `bulan_cos` | Jam, hari dalam pekan, dan bulan dalam bentuk sinus dan kosinus, agar jam 23 dekat dengan jam 0 |

Ada 29 fitur. Fitur untuk model adalah semua kolom selain `waktu`, `stasiun`, `kelompok_uji`, dan `target`. Nilai hilang berupa sel kosong di CSV.

## Aturan pemakaian

- **Hanya data sampai jam *t*, dihitung per stasiun.** Tidak ada interpolasi, tidak ada nilai dari masa depan, dan *lag* tidak pernah mengambil nilai dari stasiun lain. *Notebook* 04.7 memeriksanya dengan memotong deret di tengah dan membandingkan fitur.
- **Celah kebocoran sudah ditutup.** Baris latih yang targetnya jatuh di periode uji (24 jam terakhir sebelum batas) tidak ikut berkas latih.
- **Stasiun uji hanya ada di `fitur_uji.csv`.** Tidak ada barisnya di `fitur_latih.csv`.
- **Nilai kosong pada fitur belum diimputasi** (tanpa *forward fill*, keputusan 15 Nov 2026, dasarnya dihitung ulang di *notebook* 04.6). Sisa nilai kosong diisi median di dalam *pipeline* pada setiap *fold*, jangan dihitung dari seluruh berkas.
- **`fitur_uji.csv` hanya disimpan.** Berkas ini dibuka satu kali pada evaluasi final lewat `buka_data_uji` (*notebook* 03.3). Jangan dipakai untuk memilih fitur, model, atau *hyperparameter*.
- **Validasi** memakai *fold* dari jam unik (`TimeSeriesSplit`, `gap=24`), bukan dari baris gabungan stasiun.
