# Tugas Machine Learning: Peramalan PM2.5 Beijing

Proyek individu mata kuliah Pembelajaran Mesin, S2 Teknik Informatika, Universitas Hasanuddin.

- **Mahasiswa:** Muhammad Alif Qadri (D082261018)
- **Topik:** peramalan konsentrasi PM2.5
- **Dataset:** [Beijing Multi-Site Air Quality (UCI)](https://archive.ics.uci.edu/dataset/501), 12 stasiun, data per jam, Maret 2013 sampai Februari 2017
- **Jenis tugas:** regresi deret waktu
- **Tantangan wajib:** nilai hilang pada sensor, validasi berurutan waktu, uji model di stasiun lain (pergeseran distribusi)

## Struktur folder

| Folder | Isi |
|---|---|
| `Data` | `Data Mentah`: 12 CSV, satu per stasiun (`Aotizhongxin.csv`, `Changping.csv`, dan seterusnya). `Data Olahan`: fitur hasil tahap 2 (`fitur_latih_Tiantan.csv`, `fitur_uji_Tiantan.csv`) |
| `Notebook` | *Notebook* utama (struktur bagian 00 sampai 09 sesuai panduan) dan *notebook* tahap 2 (EDA dan praproses) |
| `Proposal` | Proposal PDF 1 sampai 2 halaman |
| `Laporan` | Laporan akhir PDF 8 sampai 12 halaman, deklarasi penggunaan AI, dan ringkasan hasil per tahapan |
| `Presentasi` | Slide progres (Pertemuan 13) dan slide akhir (Pertemuan 15) |
| `Hasil` | Gambar dan tabel keluaran (`Gambar`, `Tabel`) |
| `Konteks` | Ringkasan panduan tugas, panduan dosen (PDF), dan catatan kerja |

## Cara menjalankan

1. Pasang Python 3.10 atau lebih baru dengan `numpy`, `pandas`, `scikit-learn`, `matplotlib`, dan `jupyter`.
2. Buka `Notebook/Tahap 2 EDA dan Praproses.ipynb`.
3. Pilih *Restart & Run All*.

`SEED = 42` ditetapkan di sel pertama, dan versi pustaka dicetak di sana.

*Notebook* tahap 2 membaca data dari folder Google Drive pemilik jika ada, lalu dari `Data/Data Mentah` (bisa dijalankan dari akar repo atau dari folder `Notebook`), dan jika keduanya tidak ada mengunduh repositori ini secara otomatis. Keluarannya langsung ditulis ke `Hasil/Gambar`, `Hasil/Tabel`, dan `Data/Data Olahan`. Hasil ringkasnya ada di `Laporan/Ringkasan Hasil Per Tahapan.md`.

## Catatan

Berkas yang dikumpulkan nanti diberi nama sesuai ketentuan dosen (`NIM_Nama_ProyekML`).
