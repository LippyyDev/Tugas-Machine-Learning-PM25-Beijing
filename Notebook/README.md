# Notebook

| Berkas | Isi |
|---|---|
| `Tahap 2 EDA dan Praproses.ipynb` | Muat 12 stasiun, pisahkan 9 stasiun latih dan 3 stasiun uji, EDA, pembagian kronologis dengan satu batas waktu, validasi dari jam unik, fitur per stasiun, *baseline*, pemeriksaan kesesuaian desain (bagian 00 sampai 04), dan perbandingan model lanjutan dengan *cross-validation* (bagian 05, termasuk eksperimen lanjutan 05.5 dan *tuning* model linear 05.7, data uji tidak dibuka). Akan diperluas menjadi *notebook* akhir (bagian 06 sampai 09) |
| `bangun_tabel_hasil_percobaan.py` | Menggabungkan CSV hasil bagian 05 di `Hasil/Tabel/` menjadi `t5_tabel_semua_eksperimen.csv` dan `Laporan/Tabel Hasil Percobaan Tahap 5.md` (tidak menjalankan model). Jalankan dari akar repo: `python Notebook/bangun_tabel_hasil_percobaan.py` |

Cara menjalankan ada di `README.md` utama. *Notebook* mencari data di folder Google Drive, lalu `Data/Data Mentah` (dari akar repo atau dari folder ini), dan bila keduanya tidak ada mengunduh repo ini.

Keluarannya ditulis ke struktur yang sama dengan repo: grafik ke `Hasil/Gambar`, tabel ke `Hasil/Tabel`, fitur ke `Data/Data Olahan`. Di Google Drive, ketiga folder itu dibuat di bawah folder `Dataset PM25 Beijing`. Nama grafik dan tabel diawali `t2_` (tahap 2), `t4_` (tahap 4), atau `t5_` (tahap 5).

Berkas fitur yang dibuat: `fitur_latih.csv` (sekitar 77 MB) dan `fitur_uji.csv` (sekitar 27 MB). Keduanya tidak di-*commit* (lihat `.gitignore`). Menjalankan seluruh *notebook* memakan sekitar 3 menit pada 2 inti CPU (bagian 05.5 membaca hasil tersimpan, mengulang semua eksperimennya dengan variabel lingkungan `CARI_ULANG=1` memakan sekitar 45 menit tambahan). *Notebook* ini disimpan tanpa keluaran sel, jadi keluaran muncul setelah dijalankan.
