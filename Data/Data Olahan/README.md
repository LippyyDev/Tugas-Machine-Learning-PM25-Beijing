# Data Olahan

Folder ini sengaja kosong sejak 16 Nov 2026. Dua berkas hasil pilot Tiantan (`fitur_latih_Tiantan.csv` dan `fitur_uji_Tiantan.csv`) dihapus karena desain evaluasi berubah menjadi 9 stasiun latih dan 3 stasiun ditahan, jadi fitur harus dibuat ulang dengan menjalankan `Notebook/Tahap 2 EDA dan Praproses.ipynb` dari awal.

Berkas di sini hanya hasil olahan dari `Data/Data Mentah`. Jangan diedit manual.

## Aturan yang tetap berlaku untuk berkas yang dibuat ulang

- **Hanya data sampai jam *t*.** Tidak ada interpolasi dan tidak ada nilai dari masa depan pada fitur.
- **Tanpa *forward fill*** (keputusan 15 Nov 2026). Nilai kosong pada fitur diisi median di dalam *pipeline* pada setiap *fold*, jangan dihitung dari seluruh berkas.
- **Baris latih yang targetnya jatuh di periode uji dibuang** (celah 24 jam sebelum batas).
- **Berkas uji hanya disimpan.** Dibuka satu kali pada evaluasi final, tidak dipakai untuk memilih fitur, model, atau *hyperparameter*.
- **Batas latih dan uji** 2016-05-12 19:00 menurut waktu jam *t*, sama untuk semua stasiun.

Deskripsi kolom (`waktu`, `target`, fitur polutan, cuaca, *lag*, rata-rata bergulir, dan fitur siklik) ada di riwayat git pada versi README sebelum commit ini, dan akan ditulis ulang setelah berkas dibuat ulang.
