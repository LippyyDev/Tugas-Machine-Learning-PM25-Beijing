# KONTEKS PROYEK: Tugas Proyek Individu Pembelajaran Mesin (Peramalan PM2.5)

Dokumen ini adalah konteks utama untuk mengerjakan tugas dalam mode proyek. Isinya merangkum **Panduan Tugas Proyek Individu: Pembelajaran Mesin** (PDF 18 halaman) dan **slide pengantar tugas** (14 slide), lalu menerjemahkannya ke topik milik LIP. Bagian yang berasal dari panduan dosen ditandai **[Panduan]**. Bagian yang merupakan usulan atau catatan kerja, bukan instruksi dosen, ditandai **[Usulan]** dan boleh diubah.

---

## 0. Ringkasan satu layar

| Item | Isi |
|---|---|
| Mahasiswa | Muhammad Alif Qadri, NIM D082261018 |
| Mata kuliah | Pembelajaran Mesin (S2 Teknik Informatika, Unhas) |
| Topik | Peramalan konsentrasi PM2.5 |
| Dataset | Beijing Multi-Site Air Quality (UCI) |
| Jenis tugas | Regresi deret waktu |
| Tantangan wajib | (1) nilai hilang pada sensor, (2) validasi berurutan waktu, (3) uji model di stasiun lain (pergeseran distribusi) |
| Skema validasi | Uji = periode paling akhir tanpa diacak, lalu `TimeSeriesSplit` pada data latih |
| *Baseline* wajib | *Naive forecast* (nilai periode sebelumnya) |
| Model lanjutan | Minimal 2, dengan *tuning* sistematis |
| Metrik utama (arah panduan) | RMSE (galat besar merugikan; PM2.5 disebut eksplisit). MAE sebagai pendamping |
| Bobot | 100% nilai mata kuliah ini |
| Titik temu kelas | Pertemuan 13 (progres, tidak dinilai terpisah) dan Pertemuan 15 (presentasi akhir) |
| Pengumpulan akhir | Laporan PDF dan *notebook* pada Pertemuan 16 |
| Penalti terlambat | Pengurangan 10% per hari, kecuali ada alasan yang disetujui dosen sebelum tenggat |

**Prinsip utama [Panduan]:** yang dinilai bukan angka tertinggi. Model sederhana yang dievaluasi dengan benar dan dianalisis tajam bernilai lebih tinggi daripada model kompleks berskor 99% yang ternyata bocor. Slide menyebutnya: *"Boleh dibantu, wajib paham"*.

---

## 1. Tujuan pembelajaran [Panduan]

Setelah proyek ini, mahasiswa mampu:

1. Merumuskan masalah nyata sebagai tugas pembelajaran mesin dengan data, target, dan ukuran keberhasilan yang jelas.
2. Membangun *baseline* dan model lanjutan, lalu menjustifikasi pilihannya.
3. Merancang skema validasi yang bebas kebocoran data dan sesuai struktur data.
4. Memilih metrik berdasarkan biaya kesalahan di domain masalah.
5. Mendiagnosis *underfitting* atau *overfitting* dan menerapkan regularisasi yang tepat.
6. Menganalisis kesalahan model, keterbatasan, dan risiko etisnya secara kritis.

Proyek meniru alur kerja peneliti: merumuskan masalah, memahami data, merancang validasi, membangun *baseline*, mencoba model lebih kuat, lalu menganalisis kapan dan mengapa model salah.

---

## 2. Topik dan dataset LIP [Panduan]

- **Topik:** peramalan konsentrasi PM2.5
- **Dataset:** Beijing Multi-Site Air Quality (UCI)
- **Jenis tugas:** regresi deret waktu
- **Tantangan utama yang wajib dibahas di laporan:** nilai hilang pada sensor; validasi berurutan waktu; uji model di stasiun lain (pergeseran distribusi)
- **Skema validasi yang ditetapkan untuk LIP:** `TimeSeriesSplit` dengan uji = periode terakhir (tanpa acak)
- **Metrik arah panduan:** RMSE, karena galat besar sangat merugikan dan PM2.5 disebut sebagai contoh topiknya

### Ketentuan dataset [Panduan]

- Pergantian topik yang lebih relevan dengan rencana tesis boleh diajukan paling lambat akhir minggu ke-1, dengan persetujuan dosen. Dataset pengganti minimal 1.000 baris dan 5 fitur, publik atau berizin jelas, dan bukan dataset "mainan" (Iris, Titanic, MNIST).
- Topik dan dataset tidak boleh sama dengan mahasiswa lain.
- Data pribadi harus dianonimkan sesuai UU No. 27 Tahun 2022 tentang Pelindungan Data Pribadi.

### Struktur repositori

Repo: `Tugas-Machine-Learning-PM25-Beijing`. Folder: `Data` (`Data Mentah`), `Notebook`, `Proposal`, `Laporan`, `Presentasi`, `Hasil` (`Gambar`, `Tabel`), `Konteks`. Penamaan memakai huruf kapital di awal kata dengan spasi. Kerangka *notebook* ada di `Notebook/Proyek ML PM25 Beijing.ipynb`.

### Sumber dan berkas dataset

- Tautan sumber (dari panduan): https://archive.ics.uci.edu/dataset/501
- Berkas yang dipakai: 12 CSV di `Data/Data Mentah/` (dilacak Git, tanpa zip), satu per stasiun, dengan nama yang sudah disederhanakan:

| Nama berkas | Nama asli |
|---|---|
| `Aotizhongxin.csv` | `PRSA_Data_Aotizhongxin_20130301-20170228.csv` |
| `Changping.csv` | `PRSA_Data_Changping_20130301-20170228.csv` |
| `Dingling.csv` | `PRSA_Data_Dingling_20130301-20170228.csv` |
| `Dongsi.csv` | `PRSA_Data_Dongsi_20130301-20170228.csv` |
| `Guanyuan.csv` | `PRSA_Data_Guanyuan_20130301-20170228.csv` |
| `Gucheng.csv` | `PRSA_Data_Gucheng_20130301-20170228.csv` |
| `Huairou.csv` | `PRSA_Data_Huairou_20130301-20170228.csv` |
| `Nongzhanguan.csv` | `PRSA_Data_Nongzhanguan_20130301-20170228.csv` |
| `Shunyi.csv` | `PRSA_Data_Shunyi_20130301-20170228.csv` |
| `Tiantan.csv` | `PRSA_Data_Tiantan_20130301-20170228.csv` |
| `Wanliu.csv` | `PRSA_Data_Wanliu_20130301-20170228.csv` |
| `Wanshouxigong.csv` | `PRSA_Data_Wanshouxigong_20130301-20170228.csv` |

Catatan: zip asli dari LIP juga memuat `data.csv` dan `test.csv`. Keduanya berisi data harga saham (kolom Open, High, Low, Close, Volume), **bukan bagian dataset ini**, dan tidak dipakai.

Pemuatan seluruh stasiun (path relatif terhadap akar repositori):

```python
import pandas as pd, glob
df = pd.concat([pd.read_csv(f) for f in sorted(glob.glob("Data/Data Mentah/*.csv"))], ignore_index=True)
df["datetime"] = pd.to_datetime(df[["year", "month", "day", "hour"]])
df = df.sort_values(["station", "datetime"]).reset_index(drop=True)
```

### Profil dataset [hasil pengecekan awal pada berkas LIP, 7 Nov 2026]

**Struktur**
- 420.768 baris × 18 kolom: 12 stasiun × 35.064 jam, dari 2013-03-01 00:00 sampai 2017-02-28 23:00.
- Jam lengkap pada setiap stasiun, tidak ada duplikat (stasiun, waktu). Nilai hilang berbentuk `NA` di CSV (terbaca `NaN`).
- Kolom: `No`, `year`, `month`, `day`, `hour`, `PM2.5`, `PM10`, `SO2`, `NO2`, `CO`, `O3`, `TEMP`, `PRES`, `DEWP`, `RAIN`, `wd` (arah angin, 16 kategori), `WSPM`, `station`. Hanya `wd` yang kategorikal.

**Nilai hilang (tantangan 1)**
- PM2.5 hilang 2,08% secara keseluruhan. Per stasiun: terendah Wanliu 1,09%, tertinggi Huairou 2,72%.
- Kolom lain: CO 4,92%, O3 3,16%, NO2 2,88%, SO2 2,14%, PM10 1,53%, `wd` 0,43%, kolom cuaca sekitar 0,1%.
- Pola celah (contoh Aotizhongxin): 209 celah beruntun pada PM2.5, median 1 jam, tetapi 4 celah lebih dari 24 jam dan terpanjang 343 jam. Celah pendek dan panjang perlu strategi berbeda, dan strategi harus kausal (lihat 10.1 nomor 3).

**Nilai ekstrem**
- PM2.5: rata-rata 79,8, simpangan baku 80,8, minimum 2, maksimum 999. Hanya 1 baris bernilai tepat 999 (stasiun Wanshouxigong), 3 baris bernilai 900 atau lebih, dan 933 baris di atas 500. Pada PM10, nilai 999 muncul 3 kali. Belum diketahui apakah 999 adalah batas alat ukur atau nilai asli. Perlu diputuskan apakah ini episode nyata atau galat sensor, karena memengaruhi RMSE.

**Pergeseran waktu dan stasiun (tantangan 2 dan 3)**
- Batas 80% kronologis jatuh sekitar 2016-05-12. Rata-rata PM2.5 latih 80,2 dan uji 78,3. Periode uji hanya sekitar 9,5 bulan sehingga tidak mencakup satu siklus musim penuh.
- Rata-rata PM2.5 per stasiun berkisar 66,0 (Dingling) sampai 86,2 (Dongsi). Dingling (66,0) dan Huairou (69,6) paling berbeda dan menjadi kandidat uji "stasiun lain". Korelasi PM2.5 antar stasiun: median 0,89, minimum 0,78.

**Indikasi kebocoran dan *baseline* (hasil cepat, belum rapi)**
- Korelasi PM2.5 dengan PM10 pada jam yang sama = 0,88. Polutan lain pada jam yang sama hanya boleh dipakai sebagai *lag*.
- RMSE *naive forecast* pada 20% periode terakhir, per stasiun (minimum, median, maksimum): horizon 1 jam 16,3, 19,4, 23,4; horizon 24 jam 73,2, 89,9, 97,9. Pada horizon 24 jam, *naive* mendekati simpangan baku data sehingga hampir tidak informatif. Pada 1 jam, *naive* sangat kuat. Horizon yang dipilih menentukan seberapa bermakna perbandingan dengan *baseline*.

Semua angka di atas adalah profil awal dan harus direproduksi di *notebook* (bagian 02) sebelum dikutip di laporan.

---

## 3. Peta jalan: tujuh tahap, dua pertemuan kelas [Panduan]

**Babak 1, Fondasi (tahap 1 sampai 4, selesai sebelum Pertemuan 13):**
1. Rumusan masalah
2. Eksplorasi dan praproses
3. Skema validasi
4. *Baseline*

→ **Pertemuan 13: Progres.** Dosen dan teman sekelas menangkap kebocoran data atau skema validasi yang keliru sebelum model rumit dibangun. Slide: *kebocoran data dan skema validasi yang keliru paling murah diperbaiki di sini.*

**Babak 2, Pengembangan dan pertanggungjawaban (tahap 5 sampai 7):**
5. Model lanjutan dan *tuning*
6. Evaluasi dan diagnosis
7. Analisis kesalahan dan etika

→ Laporan + *notebook* (dikumpulkan Pertemuan 16) → **Pertemuan 15: Presentasi.**

Umpan balik Pertemuan 13 wajib ditindaklanjuti (ada panah "tindak lanjuti umpan balik" dari Pertemuan 13 ke Babak 2) dan dijelaskan di laporan akhir.

### Struktur *notebook* yang disarankan [Panduan]

Dosen akan menjalankan ulang dari sel pertama sampai terakhir, jadi urutan harus rapi dan *seed* acak ditetapkan di awal.

| No | Isi |
|---|---|
| 00 | Pengaturan: *import* pustaka, `SEED = 42`, versi pustaka yang dipakai |
| 01 | Rumusan masalah: sel *markdown* berisi konteks, target, dan metrik utama |
| 02 | Muat data dan EDA: statistik deskriptif, distribusi target, nilai hilang, grafik |
| 03 | Pembagian data: pisahkan data uji, simpan, jangan disentuh lagi |
| 04 | *Pipeline* praproses dan *baseline*: hasil *cross-validation* |
| 05 | Model lanjutan dan *tuning*: minimal dua model, tabel perbandingan |
| 06 | Diagnosis: *learning curve*, bias dan varians |
| 07 | Evaluasi final: satu kali pada data uji |
| 08 | Interpretasi dan analisis kesalahan |
| 09 | Kesimpulan, keterbatasan, risiko etis |

---

## 4. Panduan tahap demi tahap [Panduan]

Kode di panduan memakai contoh klasifikasi biner dengan kolom target bernama `target`. Nama kolom, metrik, dan skema validasi harus disesuaikan. Panduan menyatakan semua potongan kode diuji dengan scikit-learn 1.9 dan imbalanced-learn 0.14.

### Tahap 1: Rumusan masalah dan pilihan metrik

Jawab tiga pertanyaan **secara tertulis sebelum membuka data**:
1. Siapa yang memakai hasil model?
2. Keputusan apa yang mereka ambil berdasarkan prediksi?
3. Kesalahan jenis mana yang lebih merugikan? (Jawaban ini menentukan metrik utama.)

**Template satu kalimat:**
> "Model ini membantu [pengguna] untuk [keputusan] dengan memprediksi [target] dari [fitur]. Kesalahan paling mahal adalah [FP / FN / galat besar], sehingga metrik utama adalah [metrik]."

**Tabel pemilihan metrik:**

| Situasi di masalah | Metrik utama | Contoh topik |
|---|---|---|
| Kasus positif yang terlewat sangat mahal (FN mahal) | Recall, F2 | Kardiovaskular, readmisi diabetes |
| Alarm palsu sangat mahal (FP mahal) | Presisi | Intervensi berbiaya tinggi |
| Kelas positif sangat langka | PR-AUC (*average precision*) | *Fraud*, *churn* |
| Kelas relatif seimbang, butuh ringkasan lintas ambang | ROC-AUC, F1 | Sentimen |
| Lebih dari dua kelas | Macro-F1 + *confusion matrix* | Putus studi |
| Regresi, galat dijelaskan dalam satuan asli | MAE | Peminjaman sepeda |
| **Regresi, galat besar sangat merugikan** | **RMSE** | **PM2.5**, harga rumah (RMSE log) |
| Tanpa label | *Silhouette* + interpretasi | Segmentasi pelanggan |

Pengingat dari slide: akurasi 99% bisa berarti *recall* 0% bila *fraud* hanya 1% data. Akurasi hampir tidak pernah menjadi metrik utama yang baik pada data tak seimbang.

### Tahap 2: Eksplorasi dan praproses

- Tujuan EDA: menemukan apa yang memengaruhi keputusan berikutnya, yaitu ketakseimbangan target, kolom yang banyak kosong, nilai tidak masuk akal, dan fitur yang baru tersedia setelah kejadian yang diprediksi (fitur ini **harus dibuang** karena membocorkan jawaban).
- **Aturan terpenting:** semua langkah praproses yang "belajar" dari data (imputasi, *scaling*, *encoding*, seleksi fitur, *resampling*) harus berada **di dalam *pipeline*** sehingga hanya belajar dari data latih pada setiap *fold*.
- Pola salah (data uji ikut "terlihat"): seluruh dataset → *scaling* / imputasi / SMOTE pada semua baris → baru dibagi latih dan uji → skor terlalu optimistis.
- Pola benar: seluruh dataset → bagi dulu (latih 80%, uji 20% disisihkan) → *pipeline* per *fold*: praproses lalu model → data uji dipakai sekali di akhir.

**Kode 1 dari panduan (pembagian data dan *pipeline* praproses, contoh klasifikasi):**

```python
import numpy as np, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

SEED = 42
df = pd.read_csv("data.csv")
X = df.drop(columns=["target"])        # buang juga kolom ID dan fitur yang bocor
y = df["target"]

# Data uji disisihkan SEKARANG, sebelum eksplorasi lebih jauh
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=SEED)

prep = ColumnTransformer([
    ("num", Pipeline([("imp", SimpleImputer(strategy="median")),
                      ("sc", StandardScaler())]),
     make_column_selector(dtype_include="number")),
    ("cat", Pipeline([("imp", SimpleImputer(strategy="most_frequent")),
                      ("oh", OneHotEncoder(handle_unknown="ignore",
                                           sparse_output=False))]),
     make_column_selector(dtype_exclude="number")),
])
```

Catatan untuk LIP: pada deret waktu, `train_test_split(..., stratify=y)` **tidak dipakai**. Pembagian dilakukan menurut waktu (lihat Tahap 3).

### Tahap 3: Skema validasi ("aturan ujian model")

- Data uji (20%) disisihkan dan dipakai **sekali** di akhir.
- Semua keputusan lain (memilih model, mengatur *hyperparameter*, membandingkan praproses) dibuat dengan *k-fold cross-validation* pada data latih.
- Hasil dilaporkan sebagai **rata-rata ± simpangan baku** dari k *fold*, agar terlihat stabilitas model.
- Memilih varian yang salah adalah salah satu sumber kebocoran paling halus.

**Varian skema sesuai struktur data:**

| Struktur data | Skema | Berlaku untuk |
|---|---|---|
| Baris independen, kelas tak seimbang | `StratifiedKFold` | Klasifikasi biasa |
| Satu subjek punya banyak baris | `GroupShuffleSplit` + `GroupKFold` | Data pasien |
| **Data berurutan waktu** | **Uji = periode terakhir + `TimeSeriesSplit`** | **LIP (dan satu mahasiswa lain)** |
| Regresi biasa | `KFold(shuffle=True)` | Harga rumah |
| Tanpa label | Stabilitas klaster pada beberapa *seed* dan sub-sampel | Segmentasi |

Untuk deret waktu: data **tidak boleh diacak**. `TimeSeriesSplit` memakai jendela latih yang melebar dan validasi selalu di masa depan. Model hanya boleh belajar dari masa lalu untuk memprediksi masa depan.

**Kode 2 dari panduan, bagian (c) deret waktu:**

```python
from sklearn.model_selection import TimeSeriesSplit

# (c) Deret waktu: urutkan dulu menurut waktu, lalu potong tanpa diacak
df = df.sort_values("datetime")
batas = int(len(df) * 0.8)
train_df, test_df = df.iloc[:batas], df.iloc[batas:]
cv = TimeSeriesSplit(n_splits=5)
```

### Tahap 4: *Baseline*

- *Baseline* adalah titik acuan. Tanpanya, sebuah angka tidak bermakna.
- Pakai model sederhana, cepat dilatih, dan mudah dijelaskan: regresi logistik atau linear.
- **Untuk deret waktu, *baseline* wajibnya adalah *naive forecast* (nilai periode sebelumnya).**
- Hasil *baseline* dipaparkan di Pertemuan 13.

**Kode 3 dari panduan (*baseline* dengan CV, contoh klasifikasi):**

```python
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression

baseline = Pipeline([("prep", prep),
                     ("model", LogisticRegression(max_iter=1000))])

metrik = ["f1", "recall", "average_precision"]
hasil = cross_validate(baseline, X_train, y_train, cv=cv, scoring=metrik)
for m in metrik:
    s = hasil[f"test_{m}"]
    print(f"{m:>18}: {s.mean():.3f} ± {s.std():.3f}")
```

**Tabel hasil yang terus ditambah (inti bagian Hasil laporan):**

| Model | Praproses khusus | Metrik utama (CV, rata-rata ± sd) | Metrik pendukung | Catatan |
|---|---|---|---|---|
| *Naive forecast* (*baseline*) | n/a | 0,___ ± 0,___ | … | … |
| Model lanjutan 1 | … | 0,___ ± 0,___ | … | … |
| Model lanjutan 2 (*tuned*) | … | 0,___ ± 0,___ | … | … |

### Tahap 5: Model lanjutan dan *tuning*

- Minimal **dua** model lanjutan dengan alasan kuat untuk data. Pada data tabular, model berbasis pohon (*random forest*, *gradient boosting*) biasanya kandidat terkuat.
- *Tuning* dilakukan dengan *cross-validation* pada data latih. Data uji tetap tidak disentuh.
- Resampling (jika relevan) harus di dalam `imblearn.pipeline.Pipeline`. (Untuk regresi PM2.5, SMOTE tidak relevan.)

**Kode 4 dari panduan (contoh: *gradient boosting* dengan pencarian *hyperparameter*):**

```python
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import RandomizedSearchCV

pipe_gb = Pipeline([("prep", prep),
                    ("model", HistGradientBoostingClassifier(random_state=SEED))])
ruang = {
    "model__learning_rate": [0.03, 0.1, 0.3],
    "model__max_depth": [3, 6, None],
    "model__l2_regularization": [0.0, 0.1, 1.0],   # regularisasi L2
}
search = RandomizedSearchCV(pipe_gb, ruang, n_iter=15, cv=cv,
                            scoring="average_precision", random_state=SEED)
search.fit(X_train, y_train)
print(search.best_params_, round(search.best_score_, 3))
```

### Tahap 6: Evaluasi dan diagnosis

- Skor saja tidak cukup. Alat utama: ***learning curve*** (skor latih dan validasi sebagai fungsi jumlah data latih).

| Pola | Ciri kurva | Tindakan |
|---|---|---|
| *Underfitting* | Kedua kurva rendah dan bertemu; tambah data tidak membantu | Model lebih kompleks, fitur lebih baik |
| *Overfitting* | Celah lebar yang tidak menutup; model menghafal data latih | Regularisasi, data lebih banyak |
| Seimbang | Kedua kurva tinggi, celah kecil | Lanjut ke evaluasi final |

- Setelah model final dipilih berdasarkan CV, **baru** data uji dibuka. **Satu kali.**
- Jika skor uji jauh lebih buruk dari skor CV, **jangan menyetel ulang berdasarkan data uji**. Laporkan dan analisis selisihnya.

**Kode 5 dari panduan (*learning curve* dan evaluasi final, contoh klasifikasi):**

```python
from sklearn.model_selection import LearningCurveDisplay

final = search.best_estimator_      # sudah dilatih ulang pada seluruh data latih

LearningCurveDisplay.from_estimator(
    final, X_train, y_train, cv=cv, scoring="average_precision",
    train_sizes=np.linspace(0.1, 1.0, 5))

# ---- Hanya dijalankan SEKALI, setelah semua keputusan diambil ----
y_pred = final.predict(X_test)
```

### Tahap 7: Analisis kesalahan, interpretasi, dan etika

**Analisis kesalahan (tiga langkah dari slide):**
1. Pisahkan prediksi yang salah, bandingkan profilnya dengan yang benar.
2. Cari kelompok, rentang nilai, atau jenis teks tempat kesalahan menumpuk.
3. Cek fitur terpenting (*permutation importance* atau SHAP): masuk akal secara domain?

**Kode 6 dari panduan (kepentingan fitur dan analisis kesalahan):**

```python
from sklearn.inspection import permutation_importance

imp = permutation_importance(final, X_test, y_test, scoring="average_precision",
                             n_repeats=10, random_state=SEED)
penting = pd.Series(imp.importances_mean, index=X_test.columns)
print(penting.sort_values(ascending=False).head(10))

analisis = X_test.assign(aktual=y_test, prediksi=y_pred)
salah = analisis[analisis["aktual"] != analisis["prediksi"]]
benar = analisis[analisis["aktual"] == analisis["prediksi"]]
```

**Empat pertanyaan etis yang WAJIB dijawab di laporan:**
1. Apakah kinerja model berbeda untuk kelompok yang berbeda (jenis kelamin, usia, wilayah)? Hitung metrik utama per kelompok.
2. Siapa yang dirugikan jika model salah, dan seberapa besar kerugiannya?
3. Adakah fitur sensitif atau proksi diskriminasi?
4. Bagaimana model seharusnya dipakai: otomatis, atau alat bantu bagi manusia yang tetap memutuskan?

### Catatan panduan khusus untuk regresi dan deret waktu

**Regresi:** ganti `StratifiedKFold` dengan `KFold(shuffle=True)` (untuk regresi biasa) dan *scoring* dengan `"neg_mean_absolute_error"` atau `"neg_root_mean_squared_error"`. Plot residual terhadap prediksi.

**Deret waktu:** bangun fitur *lag* dan kalender (jam, hari, musim) **hanya dari masa lalu**. Bandingkan setiap model dengan *naive forecast*. Laporkan galat per jam atau per musim.

---

## 5. Luaran dan struktur laporan [Panduan]

| Luaran | Format | Isi |
|---|---|---|
| Proposal | PDF, 1 sampai 2 halaman | Rumusan masalah, sumber dataset, metrik utama yang direncanakan beserta alasannya |
| *Notebook* | `.ipynb` atau tautan Colab/GitHub | Kode lengkap dan berkomentar, mengikuti struktur di Bagian 3, dapat dijalankan ulang dari awal |
| Laporan akhir | PDF, 8 sampai 12 halaman | Format artikel ilmiah (struktur di bawah) |
| Presentasi | 10 menit + 5 menit tanya jawab | Maksimal 10 slide, dibawakan di Pertemuan 15 |

**Struktur laporan akhir:**
1. Abstrak (maksimal 200 kata)
2. Pendahuluan: konteks, rumusan masalah, kontribusi
3. Tinjauan pustaka singkat: **minimal 5 referensi, 3 di antaranya artikel jurnal atau konferensi 5 tahun terakhir**
4. Data dan metodologi: dataset, praproses, skema validasi, model
5. Hasil: tabel perbandingan model, *learning curve*, metrik pada data uji
6. Pembahasan: diagnosis bias dan varians, analisis kesalahan, interpretasi
7. Etika dan keterbatasan
8. Kesimpulan dan saran
9. Daftar pustaka (gaya APA atau IEEE, **konsisten**)
10. Lampiran: **deklarasi penggunaan alat AI**

**Penamaan berkas:** `D082261018_Muhammad Alif Qadri_ProyekML.pdf` dan `D082261018_Muhammad Alif Qadri_ProyekML.ipynb` (format `NIM_Nama_ProyekML`).

Pembaca laporan harus bisa memahami apa yang dilakukan, mengapa, dan seberapa yakin pada hasilnya, **tanpa membuka *notebook***.

---

## 6. Jadwal dan dua pertemuan kelas [Panduan]

Enam minggu berjalan (lima minggu pengerjaan ditambah minggu presentasi):

| Minggu | Kegiatan | Luaran |
|---|---|---|
| 1 | Konfirmasi topik dan dataset | Proposal |
| 2 | EDA, praproses, skema validasi | n/a |
| 3 | **Pertemuan 13: Progres** | *Notebook* sementara + slide progres |
| 4 | Model lanjutan, *tuning*, tindak lanjut umpan balik | n/a |
| 5 | Evaluasi akhir, analisis, etika | Laporan + *notebook* |
| 6 | **Pertemuan 15: Presentasi** (10 menit + 5 menit tanya jawab) | Slide presentasi |

Tenggat tanggal mengikuti pengumuman dosen. Keterlambatan dikenai pengurangan 10% per hari.

### Persiapan Pertemuan 13 (progres)

Anggap sebagai pemeriksaan fondasi. **Maksimal 5 slide** berisi:
1. Rumusan masalah dan metrik utama
2. Temuan penting dari eksplorasi data
3. Skema validasi beserta cara mencegah kebocoran
4. Hasil *baseline*
5. Rencana model lanjutan

Sampaikan juga **kendala** yang dihadapi, karena itu yang paling berguna dibahas. Tidak dinilai terpisah, tetapi umpan balik wajib ditindaklanjuti dan dijelaskan di laporan akhir.

### Persiapan Pertemuan 15 (presentasi akhir)

Alur yang disarankan: masalah dan mengapa penting → data dan skema validasi → perbandingan *baseline* dan model lanjutan → diagnosis dan hasil pada data uji → analisis kesalahan → risiko etis dan kesimpulan. Siap menjelaskan setiap keputusan metodologi dan setiap bagian kode yang ditanyakan.

---

## 7. Rubrik penilaian (total 100) [Panduan]

Separuh nilai ada di metodologi: skema validasi, evaluasi, dan analisis.

| Komponen | Bobot | Sangat baik (A) | Cukup (B sampai C) | Kurang (D sampai E) |
|---|---|---|---|---|
| Proposal dan rumusan masalah | 10% | Masalah nyata; target dan metrik dijustifikasi dengan biaya kesalahan | Masalah jelas, justifikasi metrik umum | Masalah kabur atau tanpa metrik |
| Eksplorasi dan praproses | 10% | EDA bermakna; praproses di dalam *pipeline* | EDA standar; sebagian praproses di luar *pipeline* | EDA minim; praproses bocor |
| **Skema validasi** | **20%** | Sesuai struktur data, bebas kebocoran, data uji dipakai sekali | Benar tetapi kurang dijustifikasi | Ada kebocoran atau tanpa data uji terpisah |
| Pemodelan | 15% | *Baseline* + 2 model lanjutan, *tuning* sistematis | Model lengkap, *tuning* seadanya | Tanpa *baseline* atau hanya satu model |
| **Evaluasi dan diagnosis** | **15%** | Metrik tepat dengan ketidakpastian (± sd), *learning curve*, diagnosis bias dan varians | Metrik tepat tanpa diagnosis | Hanya akurasi pada data tak seimbang |
| **Analisis kesalahan, interpretasi, etika** | **15%** | Pola kesalahan dan risiko etis dianalisis tajam, dengan mitigasi | Ada analisis tetapi dangkal | Tidak ada analisis |
| Laporan dan *notebook* | 10% | Rapi, berargumen, referensi memadai, *notebook* dapat dijalankan ulang | Lengkap tetapi kurang rapi | Tidak lengkap atau *notebook* gagal dijalankan |
| Presentasi dan tanya jawab | 5% | Jelas, tepat waktu, menguasai jawaban | Cukup jelas | Tidak menguasai materi |

Tiga komponen tebal (20 + 15 + 15 = 50%) adalah komponen metodologi evaluasi dan analisis.

---

## 8. Integritas akademik dan penggunaan AI [Panduan]

Proyek dikerjakan sendiri. Prinsip: **boleh dibantu, wajib paham.**

| Boleh | Wajib | Dilarang |
|---|---|---|
| Diskusi konsep dengan teman sekelas | Deklarasi penggunaan AI di lampiran: alat apa, untuk bagian apa | Berbagi kode atau laporan antarmahasiswa |
| Memakai kode tutorial, Kaggle, atau GitHub dengan **mencantumkan sumber** (di *notebook*) | Mampu menjelaskan setiap baris kode dan klaim saat tanya jawab | Plagiarisme, serta data atau hasil yang direkayasa |
| Alat AI untuk membantu kode dan bahasa | Analisis, interpretasi, dan kesimpulan adalah pemikiran sendiri | **Konsekuensi: nilai nol untuk komponen terkait** (dan diproses sesuai aturan akademik universitas) |

**Bacaan pendukung dari panduan:**
- Géron, A. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly (bab proyek *end to end*).
- Hastie, T., Tibshirani, R., & Friedman, J. *The Elements of Statistical Learning*. Springer (teori bias dan varians, validasi silang).
- Dokumentasi scikit-learn: *Cross-validation*, *Pipelines and composite estimators*, *Common pitfalls and recommended practices*.

---

## 9. Daftar periksa sebelum mengumpulkan [Panduan]

**Data dan validasi**
- [ ] Data uji dipisahkan di awal dan hanya dipakai sekali untuk model final.
- [ ] Semua imputasi, *scaling*, *encoding*, dan *resampling* ada di dalam *pipeline*.
- [ ] Tidak ada fitur yang baru tersedia setelah kejadian yang diprediksi.
- [ ] Skema validasi sesuai struktur data (berurutan waktu) dan alasannya dijelaskan.

**Model dan evaluasi**
- [ ] Ada satu *baseline* dan minimal dua model lanjutan.
- [ ] Metrik utama dijustifikasi dengan biaya kesalahan; akurasi bukan satu-satunya metrik.
- [ ] Hasil CV dilaporkan sebagai rata-rata ± simpangan baku.
- [ ] Ada *learning curve* dan diagnosis bias dan varians.

**Analisis dan etika**
- [ ] Ada analisis pola kesalahan, bukan hanya angka.
- [ ] Ada interpretasi fitur penting yang dikaitkan dengan pengetahuan domain.
- [ ] Empat pertanyaan etis di Tahap 7 dijawab.
- [ ] Umpan balik dari Pertemuan 13 sudah ditindaklanjuti dan dijelaskan.

**Berkas**
- [ ] *Notebook* berjalan dari awal sampai akhir tanpa error (*Restart & Run All*).
- [ ] `SEED` ditetapkan dan versi pustaka dicatat.
- [ ] Laporan 8 sampai 12 halaman, minimal 5 referensi, dengan deklarasi penggunaan AI.
- [ ] Nama berkas mengikuti format `NIM_Nama_ProyekML`.

---

## 10. Penerjemahan ke topik PM2.5 [Usulan, bukan instruksi dosen]

Bagian ini adalah catatan kerja. Semua butir di sini perlu diputuskan LIP sendiri dan, bila perlu, dikonfirmasi ke dosen.

### 10.1 Keputusan terbuka (harus diputuskan di Tahap 1 sampai 3)

| No | Keputusan | Mengapa penting |
|---|---|---|
| 1 | **Horizon peramalan** (misalnya 1 jam, 6 jam, atau 24 jam ke depan) | Menentukan fitur mana yang sah. Panduan tidak menetapkannya. Profil awal menunjukkan *naive* sangat kuat pada 1 jam (RMSE median sekitar 19) dan hampir tidak informatif pada 24 jam (sekitar 90), sehingga pilihan horizon mengubah makna perbandingan dengan *baseline*. **Prioritas pertama untuk diputuskan.** |
| 2 | **Daftar fitur yang diizinkan** | Polutan lain (PM10, NO2, CO, dan seterusnya) pada waktu yang sama dengan target berkorelasi kuat dan baru "tersedia" bersamaan dengan target. Hanya boleh dipakai dalam bentuk *lag* yang sesuai horizon. Ini sumber kebocoran paling halus dan masuk ke komponen 20%. |
| 3 | **Penanganan nilai hilang yang kausal** | Interpolasi linear memakai nilai masa depan, jadi bocor. Alternatif aman: *forward fill*, atau imputer yang dipelajari dari *fold* latih di dalam *pipeline*. Pilihan harus dijustifikasi. |
| 4 | **Makna "uji di stasiun lain"** | Opsi A: latih di satu stasiun, uji di stasiun lain. Opsi B: latih gabungan beberapa stasiun, uji pada stasiun yang tidak ikut dilatih. Opsi C: keduanya, sebagai analisis pergeseran distribusi di Tahap 7. Sebaiknya dikonfirmasi ke dosen. |
| 5 | **Stasiun utama** untuk pengembangan model | Biasanya satu stasiun dipakai untuk latih dan validasi, stasiun lain khusus untuk uji ketahanan. Kandidat uji "stasiun lain" yang paling berbeda: Dingling dan Huairou. |
| 6 | **Perlakuan nilai ekstrem PM2.5** (1 baris bernilai 999, 3 baris di atas 900, 933 baris di atas 500) | Dibuang, dibatasi, atau dipertahankan sebagai episode nyata. Harus dijustifikasi karena memengaruhi RMSE. |
| 7 | **Ukuran periode uji** | Panduan: 20% terakhir secara kronologis. |

### 10.2 Padanan komponen panduan ke topik PM2.5

| Panduan | Untuk PM2.5 |
|---|---|
| Pembagian data | Urutkan menurut waktu, 80% awal untuk latih, 20% akhir untuk uji, tanpa acak |
| CV | `TimeSeriesSplit(n_splits=5)` pada 80% awal |
| *Scoring* | `neg_root_mean_squared_error` (utama), `neg_mean_absolute_error` (pendukung) |
| *Baseline* | *Naive forecast* (nilai PM2.5 pada periode sebelumnya, sesuai horizon). Opsional pembanding tambahan: regresi linear dengan fitur *lag* |
| Model lanjutan | Kandidat: *random forest*, *gradient boosting* (misalnya `HistGradientBoostingRegressor`) dengan fitur *lag* dan kalender. Pilihan final harus punya alasan kuat |
| Fitur | *Lag* PM2.5, rata-rata bergulir (hanya dari masa lalu), fitur kalender (jam, hari, bulan atau musim), cuaca (TEMP, PRES, DEWP, RAIN, WSPM, arah angin) |
| *Learning curve* | Perlu hati-hati: gunakan CV yang menghormati urutan waktu |
| *Permutation importance* | Fitur *lag* saling berkorelasi, jadi interpretasinya perlu hati-hati dan sebaiknya dikelompokkan |
| Galat per kelompok | Per jam, per musim, per stasiun, dan per rentang konsentrasi (episode polusi tinggi vs rendah) |

### 10.3 Pertanyaan etis dalam konteks PM2.5

Data ini tidak berisi atribut pribadi, jadi pertanyaan 1 sampai 4 perlu dimaknai ulang:
1. **Kinerja antar kelompok:** antar stasiun (wilayah), musim, dan jam. Apakah galat lebih besar di stasiun tertentu atau saat konsentrasi tinggi?
2. **Siapa yang dirugikan:** warga yang bergantung pada peringatan polusi (misalnya keputusan memakai masker, berolahraga di luar, atau kelompok rentan). Ramalan terlalu rendah saat polusi tinggi (*underestimation*) berpotensi lebih merugikan daripada terlalu tinggi. Ini bisa dikaitkan ke pilihan metrik dan evaluasi di rentang tinggi.
3. **Fitur sensitif atau proksi:** identitas stasiun bisa menjadi proksi wilayah atau tingkat sosial ekonomi. Perlu dibahas.
4. **Cara pemakaian:** alat bantu peringatan dini dengan manusia yang tetap memutuskan, bukan otomatis.

### 10.4 Titik rawan yang perlu dicek di setiap tahap

- [ ] *Scaling* dan imputasi tidak dihitung dari data uji.
- [ ] Tidak ada fitur yang memakai nilai masa depan (termasuk *rolling mean* yang tidak berpusat di masa lalu, interpolasi, dan *target encoding* yang bocor).
- [ ] Setiap *fold* `TimeSeriesSplit` memvalidasi periode yang lebih baru daripada data latihnya.
- [ ] Perbandingan dengan *naive forecast* selalu disertakan, sehingga skor model punya acuan.
- [ ] Skor uji dibuka satu kali. Jika jauh lebih buruk dari CV, dianalisis (kemungkinan: perubahan musim atau tahun, pergeseran distribusi), bukan disetel ulang.

---

## 11. Aturan kerja Claude di proyek ini [Usulan]

Aturan kerja bersama Claude:

1. **Tidak ada angka karangan.** Semua angka berasal dari hasil eksekusi yang nyata. Jika belum dijalankan, Claude menyatakannya belum diuji.
2. **Data uji tidak disentuh** sebelum LIP menyatakan semua keputusan sudah final. Claude tidak boleh menyarankan penyetelan ulang berdasarkan skor uji.
3. **Pertanyaan kritis lebih dulu daripada persetujuan.** Claude harus menandai potensi kebocoran, klaim tanpa dasar, dan pilihan metodologi yang lemah, serta merujuk pada literatur atau dokumentasi bila relevan.
4. **Sumber dicantumkan.** Kode dari tutorial, Kaggle, atau GitHub harus ditulis sumbernya di *notebook*.
5. Mengikuti struktur *notebook* 00 sampai 09 dan menetapkan `SEED = 42` serta mencatat versi pustaka.

### Gaya respons yang diinginkan LIP

- Bahasa Indonesia baku, sesuai PUEBI.
- Istilah asing ditulis dengan huruf miring (*italic*).
- Tidak memakai tanda pisah em-dash.
- Tidak memakai tanda hubung sebagai pemisah kalimat. Tanda hubung hanya untuk kata ulang atau kata majemuk baku.
- Respons kritis dan berbasis data empiris. Tidak *sycophantic* dan tidak memvalidasi klaim tanpa bukti dari literatur.

---

## 12. Status pengerjaan (perbarui sepanjang proyek)

| Tahap | Status | Catatan |
|---|---|---|
| 1. Rumusan masalah dan metrik | Belum | |
| 2. EDA dan praproses | Belum | |
| 3. Skema validasi | Belum | |
| 4. *Baseline* | Belum | |
| Pertemuan 13 (progres) | Belum | Maksimal 5 slide |
| 5. Model lanjutan dan *tuning* | Belum | |
| 6. Evaluasi dan diagnosis | Belum | |
| 7. Analisis kesalahan dan etika | Belum | |
| Laporan + *notebook* | Belum | |
| Pertemuan 15 (presentasi) | Belum | Maksimal 10 slide, 10 + 5 menit |
