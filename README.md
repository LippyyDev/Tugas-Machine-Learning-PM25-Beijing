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
| `Data` | `Data Mentah`: 12 CSV, satu per stasiun (`Aotizhongxin.csv`, `Changping.csv`, dan seterusnya) |
| `Notebook` | *Notebook* utama (struktur bagian 00 sampai 09 sesuai panduan) |
| `Proposal` | Proposal PDF 1 sampai 2 halaman |
| `Laporan` | Laporan akhir PDF 8 sampai 12 halaman dan deklarasi penggunaan AI |
| `Presentasi` | Slide progres (Pertemuan 13) dan slide akhir (Pertemuan 15) |
| `Hasil` | Gambar dan tabel keluaran (`Gambar`, `Tabel`) |
| `Konteks` | Ringkasan panduan tugas, panduan dosen (PDF), dan catatan kerja |

## Cara menjalankan

1. Pasang Python 3.10 atau lebih baru dengan `numpy`, `pandas`, `scikit-learn`, `matplotlib`, dan `jupyter`.
2. Buka `Notebook/Proyek ML PM25 Beijing.ipynb`.
3. Pilih *Restart & Run All*. Sel pemuatan data membaca ke-12 CSV di `Data/Data Mentah`.

`SEED = 42` ditetapkan di sel pertama, dan versi pustaka dicetak di sana.

## Catatan

Berkas yang dikumpulkan nanti diberi nama sesuai ketentuan dosen (`NIM_Nama_ProyekML`).
