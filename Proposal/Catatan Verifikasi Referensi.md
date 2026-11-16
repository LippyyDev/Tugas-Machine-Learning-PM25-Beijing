# Catatan Verifikasi Referensi Proposal

Dicek pada 8 November 2026 lewat pencarian web (Crossref, halaman penerbit, PMC, agregator SCImago). Berkas ini pendamping proposal dan tidak termasuk batas 1 sampai 2 halaman.

## Referensi yang dipakai di proposal

| No | Referensi | Verifikasi metadata | Indeks dan kuartil | Akses | Peran | Status |
|---|---|---|---|---|---|---|
| [1] | Cui dkk., 2023, *Atmospheric Pollution Research* 14(9), 101833. DOI 10.1016/j.apr.2023.101833 | Penulis, judul, volume, DOI cocok di Crossref. Teks lengkap PDF dibaca 16 Nov 2026 (unggahan penulis). Terbaca: 12 stasiun Beijing 2013 sampai 2017, Transformer vs CNN-LSTM-Attention, metrik EVS, R2, MAE, MSE. Latih Jan 2013 sampai Feb 2015, prediksi Jan 2016 sampai Feb 2017 (urutan waktu, tetapi data per musim dilatih terpisah dan ada celah sekitar 10 bulan). Normalisasi min-maks tanpa keterangan apakah dihitung dari data latih saja. Tidak terbaca: strategi nilai hilang, horizon, ukuran jendela, validasi berurutan, uji stasiun lain, nama UCI. Teks abstrak dan isi tidak konsisten soal periode prediksi (2017 vs 2016 sampai Feb 2017). Layak sebagai rujukan dataset dan pembanding model, bukan rujukan skema validasi | Terindeks Scopus (daftar direktori pada halaman jurnal di researcher.life). Kuartil: Q1 menurut agregator SJR (kategori *Pollution*), tetapi satu agregator lain menyebut Q2 untuk SJR dan JCR 2023 Q2. Belum dicek langsung di scimagojr.com | [ScienceDirect], status OA belum dicek | [Penelitian Terbaru] | Sebagian |
| [2] | Hewamalage, Ackermann, Bergmeir, 2023, *Data Mining and Knowledge Discovery* 37(2), 788–832. DOI 10.1007/s10618-022-00894-5 | Cocok di halaman penerbit, katalog, dan PMC. Klaim yang dipakai (evaluasi keliru menghasilkan kesimpulan semu, kebocoran lewat partisi dan praproses) ada di abstrak dan versi arXiv | Halaman Springer mencantumkan Scopus. Kuartil Q1 menurut agregator (data 2022, diperbarui 2023), belum dicek di scimagojr.com | [Open Access] | [Penelitian Terbaru] | Sebagian |
| [3] | Hua dkk., 2024, *PLOS ONE* 19(9). DOI 10.1371/journal.pone.0306303 | Cocok di PMC dan IDEAS. Nomor artikel belum dicatat. Abstrak: ulasan dan evaluasi delapan metode imputasi pada data kualitas udara | SCImago: *PLOS ONE* Q1 (SJR 0,803, tabel tahun 2024 di scimagojr.com) | [Open Access] | [Penelitian Terbaru] | Terverifikasi |

Catatan batas klaim: pada [1] hanya tujuan, data (12 stasiun Beijing per jam), dan model yang dibandingkan yang dikutip. Hasil numeriknya tidak dikutip. Pada [3] hanya cakupan studi yang dikutip, bukan kesimpulan metode terbaik.

## Kandidat yang belum dimasukkan

| Referensi | Alasan belum dipakai |
|---|---|
| Dáger López, 2026, *Ecological Engineering & Environmental Technology* 27(10), 118–133. DOI 10.12912/27197050/231162 | Sangat relevan (kebocoran temporal, uji *leave-one-station-out*, *baseline* persistence), tetapi indeks Scopus dan kuartil belum terverifikasi. Hanya halaman ringkasan yang dibaca |
| Haile, Tian, Tian, 2026, *Communications in Statistics, Theory and Methods* 55(5), 1602–1622 | Relevan untuk imputasi dengan celah panjang dan divalidasi pada PM2.5 Beijing, tetapi DOI belum ditemukan dan indeks Scopus belum terverifikasi |
| Niu, Zhang, Ren, 2023, *Atmosphere* 14(2), 340. DOI 10.3390/atmos14020340 | Metadata cocok di Crossref, tetapi memakai 35 stasiun Beijing 2019 sampai 2022 (bukan dataset ini) dan indeks Scopus belum dicek |

Dikeluarkan karena tidak memenuhi syarat: Albelali dan Ahmed (arXiv 2512.06932, Des 2025) berstatus *preprint* tanpa bukti terbit di jurnal atau konferensi terindeks.

## Yang harus dicek manual oleh LIP

1. ~~Kuartil [1] dan [2] langsung di scimagojr.com~~ Sudah dicek 16 Nov 2026 lewat halaman SCImago, hasil di bagian paling bawah berkas ini.
2. ~~Teks lengkap [1]~~ Sudah dibaca 16 Nov 2026 (lihat bagian paling bawah). Hasil numerik [1] tetap tidak dikutip.
3. Kebutuhan laporan akhir: minimal 5 referensi, 3 di antaranya artikel 5 tahun terakhir. Proposal kini memuat 5 (ditambah [4] dan [5] pada 16 Nov 2026), sisanya dapat diambil dari kandidat di atas setelah diverifikasi, ditambah teori dasar berlabel [Teori Dasar] jika perlu.

## Literatur untuk skema validasi dan kebocoran data (dicek 15 November 2026)

Tujuan: mencari dukungan literatur untuk keputusan di bagian 03 notebook (pemisahan kronologis, `TimeSeriesSplit` dengan `gap=24`, praproses di dalam *pipeline* per *fold*, data uji dibuka satu kali). Hasil pencarian dibaca lewat halaman PMC, penerbit, arXiv, dan dokumentasi *scikit-learn*. Tidak ada angka dari literatur yang dipakai.

| No | Referensi | Verifikasi metadata | Indeks dan kuartil | Akses | Peran | Status |
|---|---|---|---|---|---|---|
| [2] (diperbarui) | Hewamalage, Ackermann, Bergmeir, 2023, *Data Mining and Knowledge Discovery* 37(2), 788–832. DOI 10.1007/s10618-022-00894-5 | Halaman PDF penerbit dan PMC (PMC9718476) cocok. Bagian kesimpulan versi arXiv 2203.10716 menyatakan kebocoran data perlu dihindari secara eksplisit pada evaluasi *rolling origin* dan pada praproses seperti penghalusan, dekomposisi, dan normalisasi | Kuartil belum dicek langsung di scimagojr.com. Agregator (Editage) menyebut Q1, agregator lain (Peeref) menyebut CiteScore Q1 dan JCR 2023 Q2. Tidak seragam | [Open Access] | [Penelitian Terbaru] | Sebagian (kuartil) |
| [4] | Kapoor, Narayanan, 2023, *Patterns* 4(9), 100804. DOI 10.1016/j.patter.2023.100804 | Cocok di PMC (PMC10499856), arsip NSF PAR, dan arXiv 2207.07048. Isi yang dibaca: taksonomi delapan jenis kebocoran, ulasan yang menemukan kebocoran pada sedikitnya 294 makalah di 17 bidang, dan usulan *model info sheet* | Agregator (resurchify, mengutip SCImago) menyebut Q1 kategori *Decision Sciences (miscellaneous)*, SJR 1,527, data 2025. Peeref menyebut CiteScore Q2. Belum dicek langsung di scimagojr.com | [Open Access] (CC BY) | [Penelitian Terbaru] | Sebagian (kuartil) |
| [5] | Lones, 2024, "Avoiding common machine learning pitfalls", *Patterns* 5(10), 101046. DOI 10.1016/j.patter.2024.101046 | Cocok di PDF PMC dan halaman arXiv 2108.02497 (tautan DOI terkait). Jenis artikel: *tutorial*, bukan studi empiris. Bagian tentang ketergantungan temporal pada deret waktu dan penggunaan data uji yang tepat dibaca dari versi arXiv (nomor versi tidak dipastikan), bukan dari versi *Patterns* | Sama dengan [4] (jurnal yang sama), belum dicek langsung | [Open Access] (CC BY NC) | [Penelitian Terbaru] | Sebagian (kuartil belum dicek langsung; isi versi terbit PMC dibaca 16 Nov 2026: butir temporal, kebocoran statistik skala dan imputasi, serta data uji dipakai sekali tercantum. Teks tidak memuat istilah gap, horizon, purging, atau embargo, jadi aturan gap sama dengan horizon tetap tanpa sumber di sini) |
| [Dokumentasi] | *scikit-learn*, dokumentasi `TimeSeriesSplit` (`gap`) | Halaman resmi dibuka 15 Nov 2026. `gap` didefinisikan sebagai jumlah sampel yang dikeluarkan dari ujung tiap himpunan latih sebelum himpunan uji. Ada sejak versi 0.24 | Bukan artikel berindeks | Terbuka | [Teori Dasar] | Terverifikasi |

### Yang didukung dan tidak didukung literatur ini

Didukung:
- Kebocoran lewat praproses (normalisasi, penghalusan) harus dicegah pada evaluasi deret waktu ([2]). Ini sejalan dengan imputer dan *scaler* yang dipasang di dalam *pipeline* per *fold*.
- Kebocoran data adalah kegagalan metodologi yang luas dan menghasilkan hasil terlalu optimistis ([4]).
- Fungsi parameter `gap` pada `TimeSeriesSplit` (dokumentasi).

Tidak didukung oleh sumber yang berhasil dibaca:
- Aturan `gap` sama dengan horizon peramalan. Pernyataan itu hanya saya temukan di dokumentasi sebuah paket perangkat lunak pihak ketiga (`temporalcv`), yang bukan sumber *peer review*, dan paket itu mengutip Bergmeir dan Benítez (2012) tanpa saya periksa. Jadi pembenaran `gap=24` di notebook tetap berupa penalaran (target = PM2.5 jam t+24) ditambah `assert` yang memeriksa jaraknya, bukan kutipan literatur.
- Aturan "data uji dibuka satu kali" sebagai kutipan langsung. Judul bagian tentang data uji ada di daftar isi [5], tetapi isi bagian itu belum saya baca dari versi terbit.

### Kandidat yang tidak dipakai

| Referensi | Alasan |
|---|---|
| Cerqueira, Torgo, Mozetic, 2020, *Machine Learning* (DOI 10.1007/S10994-020-05910-7) | Abstrak menyatakan validasi silang berblok dapat dipakai pada deret waktu stasioner. PM2.5 bermusim, jadi klaim itu tidak otomatis berlaku, dan hasil untuk deret tidak stasioner belum dibaca. Tahun 2020 di luar syarat 5 tahun, jadi hanya bisa dipakai sebagai [Teori Dasar] bila dosen menyetujui. Volume dan halaman belum dicatat |
| Bergmeir dan Benítez, 2012, *Information Sciences* 191, 192–213 | Hanya terlihat lewat dokumentasi paket pihak ketiga. Belum diverifikasi lewat penerbit. Tahun 2012, hanya layak sebagai [Teori Dasar] |
| Albelali dan Ahmed, arXiv 2512.06932 | *Preprint*, tetap dikeluarkan (alasan sama dengan catatan di atas) |

### Tambahan yang harus dicek manual oleh LIP

1. ~~Kuartil [4] dan [5] (*Patterns*) di scimagojr.com~~ Sudah dicek 16 Nov 2026, hasil di bagian paling bawah berkas ini. Kuartil SJR dan CiteScore bisa berbeda, jadi sebutkan satu sumber dan tahun cek di laporan.
2. ~~Isi bagian temporal dan data uji pada versi *Patterns* [5]~~ Sudah dibaca dari PDF versi terbit (PMC11573893), lihat bagian paling bawah.
3. Jumlah referensi laporan akhir: dengan [4] dan [5] terverifikasi metadata, daftar sekarang 5 butir (1 sampai 5) ditambah dokumentasi *scikit-learn*, dan kuartil [1], [2], [4], [5] sudah dicek di SCImago (lihat bagian bawah). Yang tersisa: teks lengkap [1] dan isi versi terbit [5].

## Pengecekan kuartil langsung di SCImago (16 November 2026)

Sumber: halaman jurnal di scimagojr.com (SCImago Journal Rank, berbasis data Scopus), data SJR 2025, dicek 16 Nov 2026. Saya membaca hasil pencarian atas halaman SCImago, bukan membuka daftar sumber Scopus langsung.

| Jurnal | Referensi | SJR 2025 dan kuartil terbaik | Kuartil pada tahun terbit | Catatan |
|---|---|---|---|---|
| *Patterns* | [4] (2023), [5] (2024) | 2,066, Q1 | Decision Sciences (miscellaneous): 2023 Q1, 2024 Q1. Kategori 2025: Multidisciplinary Q1 | SJR 2024 1,527 sama dengan angka agregator sebelumnya. Q1 pada tahun terbit kedua artikel |
| *Data Mining and Knowledge Discovery* | [2] (2023) | 1,200, Q1 | Tiga kategori (Computer Networks and Communications, Computer Science Applications, Information Systems): 2023 semuanya Q1 | Q1 pada tahun terbit |
| *Atmospheric Pollution Research* | [1] (2023) | 1,041, Q1 | Tergantung kategori. 2023: Pollution Q1, Atmospheric Science Q2, Waste Management and Disposal Q2 | Ini penyebab agregator menyebut Q1 atau Q2. Tulis kategori yang dipakai di laporan |
| *PLOS ONE* | [3] (2024) | SJR 0,803, Q1 | Sudah dicek sebelumnya (catatan di atas), tidak diulang | |

Yang masih belum dicek: indeksasi pada daftar sumber Scopus langsung, teks lengkap [1], dan isi bagian temporal serta data uji pada versi terbit [5].

## Pembacaan teks lengkap kelima PDF unggahan penulis (16 November 2026)

Kelima berkas dibaca dari PDF yang diunggah penulis (teks diekstrak lalu dicari per klaim). Metadata cocok dengan yang tercatat di atas. Yang dinilai hanya klaim yang benar-benar dipakai proyek, bukan seluruh isi makalah.

| No | Klaim yang dipakai proyek | Terbaca di PDF | Status klaim |
|---|---|---|---|
| [1] Cui dkk. 2023, *Atmos. Pollut. Res.* 14, 101833 | *Dataset* 12 stasiun Beijing per jam, model Transformer dan CNN-LSTM-Attention | Cocok (halaman 1 sampai 2). Pembagian data latih Jan 2013 sampai Feb 2015 dan prediksi Jan 2016 sampai Feb 2017. Tidak terbaca: nilai hilang, horizon, validasi berurutan, uji stasiun lain, nama UCI. Abstrak dan isi tidak konsisten soal periode prediksi | Terverifikasi untuk tujuan, data, dan model. Bukan rujukan skema validasi |
| [2] Hewamalage dkk. 2023, *DMKD* 37(2), 788 sampai 832 | Evaluasi keliru menghasilkan kesimpulan semu, kebocoran lewat partisi dan praproses | Bagian 3.5 dan kesimpulan: kebocoran pada deret waktu lebih mudah terjadi, termasuk lewat penghalusan, dekomposisi, dan normalisasi atas seluruh deret sebelum pembagian. Ada eksperimen *random walk* yang menunjukkan hasil menjadi terlalu baik bila bocor. Penyebutan `gap` atau horizon sebagai jarak pemisah tidak saya temukan | Terverifikasi. Mendukung praproses di dalam *pipeline* per *fold*, tidak mendukung aturan `gap` = horizon |
| [3] Hua dkk. 2024, *PLOS ONE* 19(9), e0306303 | Ulasan dan evaluasi delapan metode imputasi pada data kualitas udara | Abstrak: delapan metode (mean, median, kNNI, MICE, SAITS, BRITS, MRNN, Transformer) pada beberapa *dataset* kota di dunia. Kesimpulan: SAITS galat terendah, BRITS kedua. Penulis mengakui hanya menguji data hilang acak. *Dataset* Beijing berasal dari rujukan lain (Du dkk., SAITS), tidak disebut sebagai UCI. Tidak membahas kebocoran atau validasi berurutan | Terverifikasi untuk cakupan studi. Jangan dikutip untuk kebocoran atau untuk memilih metode imputasi pada proyek ini |
| [4] Kapoor dan Narayanan 2023, *Patterns* 4, 100804 | Kebocoran data meluas dan menghasilkan hasil terlalu optimistis | Cocok: sedikitnya 294 makalah di 17 bidang, taksonomi delapan jenis kebocoran, usulan *model info sheet*, studi kasus prediksi perang saudara. Bukan khusus deret waktu | Terverifikasi |
| [5] Lones 2024, *Patterns* 5, 101046 | Ketergantungan temporal, kebocoran statistik skala dan imputasi, data uji dipakai sekali | Cocok dengan PDF versi terbit (PMC11573893, 11 Okt 2024, *tutorial*). Tidak memuat istilah gap, horizon, purging, atau embargo | Terverifikasi untuk tiga klaim itu |

Sisa yang belum terverifikasi: indeksasi pada daftar sumber Scopus langsung (kuartil dicek lewat SCImago, bukan daftar Scopus), dan aturan `gap` sama dengan horizon yang tetap tanpa sumber *peer review*.
