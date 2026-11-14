# Deklarasi Penggunaan Alat AI

Dokumen ini diperbarui pada setiap perubahan yang dibantu AI dan menjadi bahan lampiran laporan akhir.

| Tanggal | Alat | Bagian pekerjaan | Bentuk bantuan |
|---|---|---|---|
| 2026-11-07 | Claude | Penyusunan ringkasan panduan tugas, pembuatan struktur repositori dan kerangka *notebook* | Penyusunan dokumen konteks dan kerangka kode awal. Isi analisis dan kesimpulan tetap ditulis sendiri |
| 2026-11-07 | Claude | Pengecekan awal dataset (nilai hilang, nilai ekstrem, pergeseran antar stasiun, *naive forecast* awal) | Menjalankan kode eksplorasi untuk bahan dokumen konteks. Angka belum dipakai di laporan dan harus direproduksi di *notebook* |
| 2026-11-07 | Claude | Pengunggahan repositori dan pembaruan berkas konteks (aturan Git dan pencatatan deklarasi) | Menjalankan *commit* dan *push* serta menyusun prosedur Git. Isi analisis dan kesimpulan tetap ditulis sendiri |
| 2026-11-08 | Claude | Proposal proyek (`Proposal/Proposal Proyek ML PM25 Beijing.md`, `Proposal/Catatan Verifikasi Referensi.md`) | Menyusun draf proposal dari panduan tugas, mencari dan memeriksa metadata referensi lewat pencarian web, menyusun catatan verifikasi. Keputusan metodologi, isi akhir, dan pemahaman atas setiap klaim tetap menjadi tanggung jawab penulis |
| 2026-11-08 | Claude, skill humanizer-indonesia | Proposal proyek (`Proposal/Proposal Proyek ML PM25 Beijing.md`) | Menyunting bahasa draf: mengurangi kekakuan kalimat dan kalke, melonggarkan kepadatan kata, menulis ulang paragraf rumusan masalah. Isi, angka, rujukan, dan keputusan metodologi tidak diubah |
| 2026-11-14 | Claude | Proposal proyek (`Proposal/Proposal Proyek ML PM25 Beijing (Versi Panjang).md`, `Proposal/Ringkasan Hasil Per Tahapan.md`) | Berkas proposal sebelumnya diganti namanya menjadi versi panjang. Menyusun ringkasan inti tahap 1 dari isi versi panjang tanpa menambah klaim, angka, atau rujukan baru |
| 2026-11-14 | Claude | Proposal proyek (`Proposal/Proposal Proyek ML PM25 Beijing (Versi Panjang).md`, `Proposal/Ringkasan Hasil Per Tahapan.md`) | Mengosongkan rencana model lanjutan dan pembanding tambahan sesuai permintaan penulis; *baseline* tetap *naive forecast* |
| 2026-11-14 | Claude | Status tahap 1 (`Proposal/Ringkasan Hasil Per Tahapan.md`) | Mengubah status tahap 1 menjadi selesai sebagian sesuai permintaan penulis. Isi proposal tidak diubah |
| 2026-11-14 | Claude | Proposal proyek (`Proposal/Proposal Proyek ML PM25 Beijing (Versi Panjang).md`, `Proposal/Ringkasan Hasil Per Tahapan.md`) | Menetapkan horizon 24 jam sebagai keputusan penulis dan memindahkannya dari daftar keputusan terbuka, dengan alasan kebutuhan pengguna. Bagian lain tidak diubah |
| 2026-11-14 | Claude | Proposal proyek (`Proposal/Proposal Proyek ML PM25 Beijing (Versi Panjang).md`, `Proposal/Ringkasan Hasil Per Tahapan.md`) | Menuliskan keputusan penulis untuk skema uji di stasiun lain (latih di satu stasiun, uji di stasiun lain pada periode uji yang sama), menghapus kandidat stasiun yang tidak didukung data, dan menambah pemeriksaan galat per tahun. Dasarnya uji indikatif pada 80% data awal yang belum menjadi hasil resmi
