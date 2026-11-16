# Notebook

| Berkas | Isi |
|---|---|
| `Tahap 2 EDA dan Praproses.ipynb` | Muat 12 stasiun, pisahkan 9 stasiun latih dan 3 stasiun asing, EDA, pembagian kronologis dengan satu batas waktu, validasi dari jam unik, fitur per stasiun, *baseline*, dan pemeriksaan kesesuaian desain (bagian 00 sampai 04). Akan diperluas menjadi *notebook* akhir (bagian 05 sampai 09) |

Cara menjalankan ada di `README.md` utama. *Notebook* mencari data di folder Google Drive, lalu `Data/Data Mentah` (dari akar repo atau dari folder ini), dan bila keduanya tidak ada mengunduh repo ini.

Keluarannya ditulis ke struktur yang sama dengan repo: grafik ke `Hasil/Gambar`, tabel ke `Hasil/Tabel`, fitur ke `Data/Data Olahan`. Di Google Drive, ketiga folder itu dibuat di bawah folder `Dataset PM25 Beijing`. Nama grafik dan tabel diawali `t2_` (tahap 2) atau `t4_` (tahap 4).

Berkas fitur yang dibuat: `fitur_latih.csv` (sekitar 77 MB) dan `fitur_uji.csv` (sekitar 27 MB). Keduanya tidak di-*commit* (lihat `.gitignore`). Menjalankan seluruh *notebook* memakan sekitar 3 menit pada 2 inti CPU. *Notebook* ini disimpan tanpa keluaran sel, jadi keluaran muncul setelah dijalankan.
