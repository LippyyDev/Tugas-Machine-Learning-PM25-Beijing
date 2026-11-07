# Data Mentah

Data kualitas udara per jam dari 12 stasiun pemantau di Beijing, Maret 2013 sampai Februari 2017. Sumber: [Beijing Multi-Site Air Quality (UCI)](https://archive.ics.uci.edu/dataset/501).

Isi berkas tidak diubah. Hanya nama berkasnya yang disingkat, misalnya `PRSA_Data_Tiantan_20130301-20170228.csv` menjadi `Tiantan.csv`.

## Ringkasan

| Item | Isi |
|---|---|
| Jumlah berkas | 12 CSV, satu per stasiun |
| Baris per berkas | 35.064 (data per jam, tanpa jam yang terlewat) |
| Total baris | 420.768 |
| Jumlah kolom | 18 |
| Rentang waktu | 2013-03-01 00:00 sampai 2017-02-28 23:00 |
| Nilai hilang | Ditulis `NA` |
| Target proyek | `PM2.5` |

## Kolom

| Kolom | Arti | Satuan |
|---|---|---|
| `No` | Nomor urut baris per stasiun (1 sampai 35064) | - |
| `year`, `month`, `day`, `hour` | Waktu pengamatan (`hour` 0 sampai 23) | - |
| `PM2.5` | Konsentrasi partikel halus, **target** | µg/m³ |
| `PM10` | Konsentrasi partikel kasar | µg/m³ |
| `SO2`, `NO2`, `CO`, `O3` | Konsentrasi gas polutan | µg/m³ |
| `TEMP` | Suhu udara | °C |
| `PRES` | Tekanan udara | hPa |
| `DEWP` | Suhu titik embun | °C |
| `RAIN` | Curah hujan | mm |
| `wd` | Arah angin (16 arah mata angin, misalnya `N`, `NNE`, `SW`) | - |
| `WSPM` | Kecepatan angin | m/s |
| `station` | Nama stasiun | - |

## Stasiun dan nilai hilang pada PM2.5

| Stasiun | PM2.5 hilang | Persen |
|---|---|---|
| Aotizhongxin | 925 | 2,64 |
| Changping | 774 | 2,21 |
| Dingling | 779 | 2,22 |
| Dongsi | 750 | 2,14 |
| Guanyuan | 616 | 1,76 |
| Gucheng | 646 | 1,84 |
| Huairou | 953 | 2,72 |
| Nongzhanguan | 628 | 1,79 |
| Shunyi | 913 | 2,60 |
| Tiantan | 677 | 1,93 |
| Wanliu | 382 | 1,09 |
| Wanshouxigong | 696 | 1,98 |

Gabungan 12 stasiun: `PM2.5` hilang 2,08%. Kolom dengan nilai hilang terbanyak adalah `CO` (4,92%), disusul `O3` (3,16%) dan `NO2` (2,88%). Kolom waktu dan `station` tidak ada yang hilang.

## Catatan

- `PM2.5` dan `PM10` sama-sama bernilai maksimum 999. Nilai 999 muncul 1 kali pada `PM2.5` (Wanshouxigong) dan 3 kali pada `PM10` (Changping, Guanyuan, Shunyi). Perlu dicek saat eksplorasi data apakah itu batas alat ukur atau nilai asli.
- Data sudah urut waktu, jadi pembagian latih dan uji harus berurutan, tidak diacak.
- Statistik di atas dihitung langsung dari berkas di folder ini.
