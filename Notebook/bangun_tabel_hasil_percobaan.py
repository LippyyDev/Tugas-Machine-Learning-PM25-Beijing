"""Menggabungkan semua hasil percobaan Tahap 5 (bagian 05.1, 05.5, 05.7 notebook) menjadi satu tabel berurutan.

Membaca CSV di Hasil/Tabel (keluaran notebook), tidak menjalankan model. Menulis:
  Hasil/Tabel/t5_tabel_semua_eksperimen.csv
  Laporan/Tabel Hasil Percobaan Tahap 5.md
Semua angka berasal dari CSV tersebut. MSE per fold = RMSE per fold kuadrat (tepat, karena RMSE = akar MSE di fold yang sama).
"""
import os, re
import numpy as np, pandas as pd

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.join(AKAR, "Hasil", "Tabel")
F1 = "F1 (29 fitur awal)"
NAN = float("nan")
rec = {}     # kunci -> dict

def tambah(kunci, nama, fitur, sumber, rmse, mae=None, mae_ms=None):
    rmse = np.asarray(rmse, float)
    if kunci in rec:
        r = rec[kunci]
        assert np.allclose(r["rmse"], rmse, atol=0.011), (kunci, r["rmse"], rmse)
        r["sumber"].append(sumber)
        if mae is not None and r["mae"] is None:       # utamakan versi yang punya MAE per fold dan 4 desimal
            r["mae"], r["rmse"] = np.asarray(mae, float), rmse
        if mae_ms is not None and r["mae_ms"] is None:
            r["mae_ms"] = mae_ms
        return
    rec[kunci] = {"nama": nama, "fitur": fitur, "sumber": [sumber], "rmse": rmse,
                  "mae": None if mae is None else np.asarray(mae, float), "mae_ms": mae_ms}

# 05.1: naive dan enam konfigurasi (RMSE per fold dibulatkan 2 desimal di berkasnya, MAE hanya rata-rata dan sd)
pf1 = pd.read_csv(os.path.join(T, "t5_tabel_rmse_per_fold.csv"), index_col=0)
ml = pd.read_csv(os.path.join(T, "t5_tabel_model_lanjutan.csv"), index_col=0)
peta1 = {"Naive forecast": (("Naive",), "*Naive forecast*"),
         "Ridge (alpha=1)": (("Ridge", 1.0, NAN, F1), "Ridge (alpha=1)"),
         "Elastic Net (alpha=1)": (("EN", 1.0, 0.5, F1), "Elastic Net (alpha=1, l1_ratio=0,5)"),
         "Elastic Net (alpha=0,1)": (("EN", 0.1, 0.5, F1), "Elastic Net (alpha=0,1, l1_ratio=0,5)"),
         "Elastic Net (alpha=0,01)": (("EN", 0.01, 0.5, F1), "Elastic Net (alpha=0,01, l1_ratio=0,5)"),
         "Gradient boosting": (("GB", F1), "Gradient boosting (200 iterasi, kedalaman 4)"),
         "Gradient boosting (early stopping bawaan)": (("GB-ES", F1), "Gradient boosting (*early stopping* bawaan)")}
for kol, (kunci, nama) in peta1.items():
    tambah(kunci, nama, F1 if kunci[0] != "Naive" else "n/a", "05.1", pf1[kol].to_numpy(),
           mae_ms=(ml.loc[kol, "MAE rata-rata"], ml.loc[kol, "MAE sd"]))

# 05.7: tuning model linear
t7 = pd.read_csv(os.path.join(T, "t5_tabel_tuning_linear_per_fold.csv"))
def fmt(x):
    return ("%g" % x).replace(".", ",")
for nama, g in t7.groupby("model", sort=False):
    g = g.sort_values("fold"); a, l1 = g["alpha"].iloc[0], g["l1_ratio"].iloc[0]
    if g["keluarga"].iloc[0] == "Ridge":
        kunci, teks = ("Ridge", float(a), NAN, F1), f"Ridge (alpha={fmt(a)})"
    else:
        kunci, teks = ("EN", float(a), float(l1), F1), f"Elastic Net (alpha={fmt(a)}, l1_ratio={fmt(l1)})"
    tambah(kunci, teks, F1, "05.7", g["RMSE"], g["MAE"])

# 05.5: 53 eksperimen (ablasi fitur, keluarga model, rata-rata, transformasi target, putaran 2)
e5 = pd.read_csv(os.path.join(T, "t5_tabel_eksperimen_per_fold.csv"))
setara = {f"Ridge | {F1}": ("Ridge", 1.0, NAN, F1), f"Elastic Net (alpha=0,1) | {F1}": ("EN", 0.1, 0.5, F1),
          f"Gradient boosting | {F1}": ("GB", F1)}
for nama, g in e5.groupby("eksperimen", sort=False):
    g = g.sort_values("fold")
    model, fitur = [s.strip() for s in nama.rsplit(" | ", 1)]
    model = re.sub(r"(\{[^}]*\})", lambda m: "`" + m.group(1) + "`", model).replace("alpha=0,1)", "alpha=0,1, l1_ratio=0,5)")
    sumber = "05.5 (langkah " + g["kelompok"].iloc[0] + ")"
    tambah(setara.get(nama, ("05.5", nama)), model, fitur, sumber, g["RMSE"], g["MAE"])

# Tabel gabungan
naive = rec[("Naive",)]["rmse"]
acuan = rec[("Ridge", 1.0, NAN, F1)]["rmse"] if False else None
for k in rec:                                         # kunci dengan NaN tidak cocok sebagai kunci dict, cari manual
    if k[0] == "Ridge" and k[1] == 1.0:
        acuan = rec[k]["rmse"]
assert acuan is not None
baris = []
for kunci, r in rec.items():
    x = r["rmse"]; d = x - acuan
    mae_m, mae_s = (r["mae"].mean(), r["mae"].std(ddof=1)) if r["mae"] is not None else r["mae_ms"]
    baris.append({"Konfigurasi": r["nama"], "Fitur": r["fitur"], "Sumber": ", ".join(dict.fromkeys(r["sumber"])),
                  "RMSE rata-rata": x.mean(), "RMSE sd": x.std(ddof=1), "MSE rata-rata": (x ** 2).mean(),
                  "MAE rata-rata": mae_m, "MAE sd": mae_s,
                  "Perbaikan vs naive (%)": 100 * (naive.mean() - x.mean()) / naive.mean(),
                  "Fold lebih baik dari naive": int((x < naive).sum()),
                  "Selisih vs Ridge alpha=1": d.mean(), "sd selisih vs Ridge": d.std(ddof=1),
                  "Fold lebih baik dari Ridge alpha=1": int((d < 0).sum()),
                  **{f"RMSE fold {i+1}": x[i] for i in range(5)}})
df = pd.DataFrame(baris).sort_values(["RMSE rata-rata", "RMSE sd"]).reset_index(drop=True)
df.insert(0, "Peringkat", df.index + 1)
df.round(4).to_csv(os.path.join(T, "t5_tabel_semua_eksperimen.csv"), index=False)

def c(x, n=2):
    return ("%.*f" % (n, x)).replace(".", ",")
def tabel_md(kolom, baris_fn, judul_kolom):
    out = ["| " + " | ".join(judul_kolom) + " |", "|" + "|".join(["---"] * len(judul_kolom)) + "|"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(baris_fn(r)) + " |")
    return "\n".join(out)

A = tabel_md(None, lambda r: [str(r["Peringkat"]), r["Konfigurasi"], r["Fitur"], c(r["RMSE rata-rata"]), c(r["RMSE sd"]),
                              c(r["MSE rata-rata"], 0), c(r["MAE rata-rata"]), c(r["MAE sd"]),
                              c(r["Perbaikan vs naive (%)"], 1), f'{r["Fold lebih baik dari naive"]} dari 5',
                              f'{c(r["Selisih vs Ridge alpha=1"])} ({c(r["sd selisih vs Ridge"])})',
                              f'{r["Fold lebih baik dari Ridge alpha=1"]} dari 5', r["Sumber"]],
             ["No", "Konfigurasi", "Fitur", "RMSE", "sd RMSE", "MSE", "MAE", "sd MAE", "Perbaikan vs *naive* (%)",
              "*Fold* lebih baik dari *naive*", "Selisih RMSE vs Ridge `alpha=1` (sd selisih)", "*Fold* lebih baik dari Ridge", "Sumber"])
B = tabel_md(None, lambda r: [str(r["Peringkat"]), r["Konfigurasi"]] + [c(r[f"RMSE fold {i}"], 1) for i in range(1, 6)],
             ["No", "Konfigurasi", "*Fold* 1", "*Fold* 2", "*Fold* 3", "*Fold* 4", "*Fold* 5"])

# Lampiran: konfigurasi tuning acak (hanya rata-rata dan sd yang tersimpan)
t3 = pd.read_csv(os.path.join(T, "t5_tabel_tuning.csv"))
t6 = pd.read_csv(os.path.join(T, "t5_tabel_tuning_putaran2.csv"))
hp = ["min_samples_leaf", "max_leaf_nodes", "max_features", "max_depth", "learning_rate", "l2_regularization", "iterasi_terbaik", "max_samples"]
lamp = []
for _, r in t3.iterrows():
    lamp.append((r["model"], r["himpunan"][:2], "3 tuning", r, r["RMSE rata-rata"], r["RMSE sd"]))
for _, r in t6.iterrows():
    lamp.append(("Random forest" if r["model"] == "RF" else "Extra Trees", "F3", "6 putaran 2", r, r["RMSE rata-rata"], r["RMSE sd"]))
lamp.sort(key=lambda z: (z[4], z[5]))
def hps(r):
    return ", ".join(f"{k}={('%g' % r[k])}" for k in hp if k in r.index and pd.notna(r[k]))
L = ["| No | Model | Fitur | Hiperparameter | RMSE | sd RMSE | Langkah |", "|---|---|---|---|---|---|---|"]
for i, (m, f, s, r, a, b) in enumerate(lamp, 1):
    L.append(f"| {i} | {'HGB' if m == 'HGB' else ('Random forest' if m == 'RF' else m)} | {f} | `{hps(r)}` | {c(a)} | {c(b)} | 05.5 ({s}) |")
LAMP = "\n".join(L)

md = f"""# Tabel Hasil Percobaan Tahap 5

Semua percobaan model lanjutan pada validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` di data latih 9 stasiun, diurutkan dari RMSE rata-rata terendah (terbaik) ke tertinggi (terburuk). **Data uji tidak dibuka.** Angka berasal dari eksekusi `Notebook/Tahap 2 EDA dan Praproses.ipynb` (bagian 05.1, 05.5, dan 05.7) dan digabung oleh `Notebook/bangun_tabel_hasil_percobaan.py` dari CSV di `Hasil/Tabel/`. Berkas CSV gabungan: `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.

## Cara membaca

* **RMSE** adalah rata-rata RMSE dari 5 *fold* (µg/m³, makin kecil makin baik). **sd RMSE** adalah simpangan baku RMSE antar 5 *fold* (n minus 1), yaitu sebaran kesulitan antar periode, bukan ketidakpastian rata-rata.
* **MSE** adalah rata-rata dari RMSE kuadrat di tiap *fold* (jadi bukan kuadrat dari RMSE rata-rata). **MAE** dan **sd MAE** dihitung dengan cara yang sama seperti RMSE.
* **Perbaikan vs *naive*** memakai RMSE *naive forecast* 86,82. **Selisih vs Ridge `alpha=1`** dihitung berpasangan per *fold* (negatif berarti lebih baik dari Ridge), dengan simpangan baku selisih di dalam kurung.
* **Periode validasi tiap *fold*:** *fold* 1 2013-09-11 sampai 2014-03-25, *fold* 2 sampai 2014-10-05, *fold* 3 sampai 2015-04-18, *fold* 4 sampai 2015-10-30, *fold* 5 sampai 2016-05-11. *Fold* 1, 3, dan 5 lebih sulit (RMSE *naive* 101,7; 103,6; 108,8).
* **Fitur:** F1 adalah 29 fitur awal, F2 menambah 11 fitur cuaca dinamis dan 6 fitur statistik, F3 menambah 4 fitur **lintas stasiun** (rata-rata stasiun latih lain pada jam yang sama). F3 mengubah aturan di bagian 01 dan keputusan memakainya ada pada penulis.

## Peringatan

1. Selisih antar hampir semua konfigurasi jauh di bawah sd RMSE antar *fold* (sekitar 19), jadi urutan di tabel **tidak berarti** bahwa peringkat yang berdekatan berbeda nyata.
2. Skor terbaik dipilih dari puluhan konfigurasi pada lima *fold* yang sama, sehingga optimistis dan bukan kinerja akhir. Kinerja akhir hanya dari data uji, satu kali.
3. Langkah 3 sampai 6 di bagian 05.5 ditentukan setelah melihat hasil langkah sebelumnya. Grid 05.7 ditetapkan sebelum dijalankan.
4. Baris yang sama di beberapa bagian (misalnya Ridge `alpha=1`) digabung, kolom Sumber menunjukkan asalnya. Nilai per *fold* di bagian 05.1 dibulatkan dua desimal di berkasnya.

## Tabel 1. Ringkasan, urut dari terbaik ke terburuk ({len(df)} konfigurasi)

{A}

## Tabel 2. RMSE tiap *fold*, urutan sama dengan Tabel 1

{B}

## Lampiran. Konfigurasi *tuning* acak ({len(lamp)} konfigurasi, urut dari terbaik ke terburuk)

Hanya rata-rata dan simpangan baku RMSE yang tersimpan (nilai per *fold* hanya ada untuk konfigurasi terbaik tiap kelompok, yang sudah masuk Tabel 1 dan 2), jadi MSE dan MAE tidak tersedia untuk lampiran ini. Seluruhnya F2 atau F3, bukan F1.

{LAMP}
"""
open(os.path.join(AKAR, "Laporan", "Tabel Hasil Percobaan Tahap 5.md"), "w", encoding="utf-8").write(md)
print("baris tabel utama:", len(df), "| lampiran:", len(lamp))
print(df[["Peringkat", "Konfigurasi", "Fitur", "RMSE rata-rata", "RMSE sd", "MSE rata-rata", "MAE rata-rata"]].head(5).round(2).to_string())
print(df[["Peringkat", "Konfigurasi", "RMSE rata-rata"]].tail(4).round(2).to_string())
