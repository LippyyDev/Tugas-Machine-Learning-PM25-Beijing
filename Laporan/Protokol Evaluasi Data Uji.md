# Protokol Evaluasi Data Uji

Status: **[Usulan] menunggu persetujuan LIP.** Direvisi 16 Nov 2026 mengikuti desain 9 stasiun latih dan 3 stasiun asing (lihat `Konteks/Konteks Proyek ML PM25.md` bagian 10.1 butir 4 dan 5). Isi yang bertanda [Panduan] bersumber dari panduan dosen (lihat `Konteks/Konteks Proyek ML PM25.md`, Tahap 6 dan daftar periksa). Selain itu, semua butir adalah usulan Claude dan belum menjadi aturan sampai disetujui.

Tujuan: membuat pembukaan data uji terjadi satu kali dengan aturan yang sudah ditulis sebelum skor uji terlihat, sehingga hasil uji tidak ikut menentukan model.

## Apa yang dijaga

| Butir | Isi | Sumber |
|---|---|---|
| Data uji | 20% periode terakhir (mulai 2016-05-12 19:00, batas sama untuk semua stasiun) dari 12 stasiun: 9 stasiun latih dan 3 stasiun asing (Dingling, Wanliu, Shunyi, ditetapkan LIP 16 Nov 2026 dengan dasar aturan di *notebook* 02.2). Berkas fitur uji hasil pilot Tiantan sudah dihapus (16 Nov 2026). Desain ini memakai satu berkas `fitur_uji.csv` dengan kolom `kelompok_uji`, dibuat saat *notebook* dijalankan lagi | Pembagian 80/20 dan satu kali buka: [Panduan]. Desain 9/3: keputusan LIP 16 Nov 2026, belum dikonfirmasi dosen |
| Satu kali buka | Setelah model final dipilih dari validasi silang, data uji dibuka satu kali | [Panduan] |
| Skor uji jauh lebih buruk dari skor validasi | Jangan menyetel ulang. Laporkan dan analisis selisihnya | [Panduan] |

## Aturan yang diusulkan [Usulan]

1. **Pembekuan sebelum buka.** Kode model final, daftar fitur, hiperparameter, dan praproses di-*commit* lebih dulu. *Hash* *commit* itu dicatat di log (kolom `alasan`) saat pembukaan.
2. **Aturan pemilihan model (ditulis sekarang, sebelum ada model kandidat selain *baseline*).**
   * Dasar pemilihan hanya rata-rata RMSE validasi silang 5 *fold* (`TimeSeriesSplit(n_splits=5, gap=24)`) pada data latih 9 stasiun (*fold* dari stempel waktu unik, `gap` 24 jam per jam).
   * Bila selisih rata-rata RMSE dua model lebih kecil dari satu simpangan baku antar *fold* (pada *baseline* pilot Tiantan 19,73 sampai 25,19, dihitung ulang untuk 9 stasiun), keduanya dianggap tidak terbedakan, dan yang lebih sederhana dipilih. Ambang satu simpangan baku adalah usulan, bukan aturan baku.
   * Model final harus lebih baik dari *naive forecast* di validasi. Bila tidak, laporkan apa adanya, jangan ganti metrik.
3. **Metrik yang dilaporkan.** RMSE sebagai metrik utama dan MAE sebagai pendamping (arah panduan, lihat berkas konteks). Dilaporkan terpisah untuk 9 stasiun latih dan 3 stasiun asing (per stasiun dan rata-rata), beserta *naive forecast* pada periode uji yang sama.
4. **Satu kali buka lewat `buka_data_uji()`** di *notebook* bagian 03.3. Prediksi uji disimpan ke berkas pada pembukaan pertama. Analisis kesalahan (Tahap 7) memakai prediksi tersimpan itu, bukan membuka berkas uji lagi.
5. **Bila skor uji buruk.** Skor pertama dilaporkan. Boleh ditambahkan analisis penyebab (misalnya pergeseran musim atau distribusi), tetapi tanpa melatih ulang untuk memperbaiki skor.
6. **Pembukaan 3 stasiun asing** memakai model yang sama, tanpa dilatih ulang pada stasiun itu, dan dicatat di log sebagai berkas terpisah. Stasiun asing tidak boleh dipakai untuk latih, *tuning*, imputasi, *scaling*, atau pemilihan fitur, dan harus ditetapkan serta dikunci sebelum periode uji dibuka.
7. **Keterbukaan.** Dua hal sudah tercatat di `Laporan/Ringkasan Hasil Per Tahapan.md`: statistik ringkas periode uji pernah terlihat (profil awal 7 Nov dan ringkasan berkas fitur uji 15 Nov), dan tidak dipakai untuk keputusan apa pun.

## Yang bisa dan tidak bisa dibuktikan oleh penjaga

Bisa:
* Pembukaan pertama tercatat dengan waktu, *hash* berkas, dan *hash* konfigurasi.
* Konfigurasi berbeda dari yang tercatat membuat `buka_data_uji()` menolak membaca.
* Membaca ulang dengan konfigurasi sama tetap diizinkan, agar *notebook* bisa dijalankan ulang dari awal sesuai panduan.

Tidak bisa:
* Mencegah orang yang menghapus baris log, mengubah fungsi, atau membaca berkas CSV langsung dengan cara lain.
* Membuktikan bahwa konfigurasi dipilih dari validasi dan bukan dari skor uji. Itu hanya bisa dilihat dari riwayat *commit* (konfigurasi harus sudah di-*commit* sebelum baris log pertama) dan dari kejujuran penulis.
* Membuktikan bahwa tidak ada yang pernah melihat data uji sebelum penjaga dipasang. Lihat butir 7 di atas.

## Daftar periksa sebelum membuka data uji

- [ ] Konfigurasi model final sudah di-*commit*, dan *hash commit* dicatat.
- [ ] Aturan pemilihan (butir 2) diterapkan pada tabel validasi, tanpa mengubah aturan setelah melihat hasil.
- [ ] Persetujuan LIP atas protokol ini sudah ada.
- [ ] Tiga stasiun asing sudah ditetapkan dengan aturan tertulis, dan tidak ada datanya yang dipakai untuk latih atau *tuning*.
- [ ] `Hasil/Tabel/log_pembukaan_data_uji.csv` belum ada atau belum memuat berkas yang sama.
- [ ] Sebelum menutup: log di-*commit* bersama prediksi uji dan skor pertama.
