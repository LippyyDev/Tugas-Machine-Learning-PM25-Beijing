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
    assert len(x) == 5, r["nama"]          # kriteria masuk: ada nilai di kelima fold
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

# Tingkat kesulitan (rubrik [Usulan], hanya dari struktur konfigurasi, tidak memakai hasil RMSE)
def skor_kesulitan(nama, fitur):
    if nama.startswith("*Naive"):
        return 0, {"model": 0, "komposisi": 0, "fitur": 0, "tuning": 0, "target": 0}
    pohon = any(k in nama for k in ["Random forest", "Extra Trees", "HGB", "Gradient boosting", "boosting"])
    n_model = nama.count(" + ") + 1 if " + " in nama else (2 if ("Rata-rata" in nama or "lalu" in nama) else 1)
    bagian = {"model": 3 if pohon else 1,
              "komposisi": 0 if n_model == 1 else (1 if n_model == 2 else 2),
              "fitur": {"F1": 0, "F2": 1, "F3": 2}[fitur[:2]],
              "tuning": 2 if any(k in nama for k in ["terpilih", "terbaik", "{"]) else 0,
              "target": 1 if "target " in nama else 0}
    return sum(bagian.values()), bagian
def tingkat(sk):
    return "1 Mudah" if sk <= 1 else ("2 Sedang" if sk <= 3 else ("3 Sulit" if sk <= 6 else "4 Sangat sulit"))
sk = [skor_kesulitan(n, f) for n, f in zip(df["Konfigurasi"], df["Fitur"])]
df["Skor kesulitan"] = [a for a, _ in sk]
df["Tingkat kesulitan"] = [tingkat(a) for a, _ in sk]
df_penuh = df.copy()          # untuk ringkasan per tingkat, dihitung sebelum tingkat 4 dikeluarkan
N_DIKELUARKAN = int((df["Tingkat kesulitan"] != "1 Mudah").sum())
df = df[df["Tingkat kesulitan"] == "1 Mudah"].reset_index(drop=True)      # permintaan penulis 22 Nov 2026: hanya tingkat Mudah
df["Peringkat"] = df.index + 1
df.round(4).to_csv(os.path.join(T, "t5_tabel_semua_eksperimen.csv"), index=False)

def c(x, n=2):
    return ("%.*f" % (n, x)).replace(".", ",")
def tabel_md(kolom, baris_fn, judul_kolom):
    out = ["| " + " | ".join(judul_kolom) + " |", "|" + "|".join(["---"] * len(judul_kolom)) + "|"]
    for _, r in df.iterrows():
        out.append("| " + " | ".join(baris_fn(r)) + " |")
    return "\n".join(out)

def beri_peran(r):
    k = r["Konfigurasi"] + ("" if pd.isna(r["Fitur"]) else "")
    if r["Konfigurasi"] == "Ridge (alpha=1000)" and r["Fitur"].startswith("F1 (29"): return "**Ridge (alpha=1000), model utama**"
    if r["Konfigurasi"] == "Elastic Net (alpha=1, l1_ratio=0,9)" and r["Fitur"].startswith("F1 (29"): return "**Elastic Net (alpha=1, l1_ratio=0,9), pembanding**"
    return r["Konfigurasi"]

A = tabel_md(None, lambda r: [str(r["Peringkat"]), beri_peran(r), "" if pd.isna(r["Fitur"]) else r["Fitur"], c(r["RMSE rata-rata"]), c(r["RMSE sd"]),
                              c(r["MAE rata-rata"]), c(r["Perbaikan vs naive (%)"], 1), f'{r["Fold lebih baik dari naive"]} dari 5'],
             ["No", "Konfigurasi", "Fitur", "RMSE", "sd RMSE", "MAE", "Perbaikan vs *naive* (%)", "*Fold* lebih baik dari *naive*"])

rt = df_penuh[df_penuh["Konfigurasi"] != "*Naive forecast*"].groupby("Tingkat kesulitan").agg(n=("Konfigurasi", "size"), terbaik=("RMSE rata-rata", "min"), median=("RMSE rata-rata", "median"), terburuk=("RMSE rata-rata", "max"))
RT = "| Tingkat | Jumlah konfigurasi | RMSE terbaik | RMSE median | RMSE terburuk |\n|---|---|---|---|---|\n" + "\n".join(
    f"| {i} | {int(r['n'])} | {c(r['terbaik'])} | {c(r['median'])} | {c(r['terburuk'])} |" for i, r in rt.iterrows())
mudah = df_penuh[(df_penuh["Tingkat kesulitan"] == "1 Mudah") & (df_penuh["Konfigurasi"] != "*Naive forecast*")]["RMSE rata-rata"].min()
sulit = df_penuh[df_penuh["Tingkat kesulitan"] == "4 Sangat sulit"]["RMSE rata-rata"].min()

md = f"""# Tabel Hasil Percobaan Tahap 5

Percobaan model lanjutan pada validasi silang `TimeSeriesSplit(n_splits=5, gap=24)` di data latih 9 stasiun, urut dari RMSE rata-rata terendah. Tabel hanya memuat konfigurasi yang dilatih langsung pada 9 stasiun dengan *fold*, baris validasi, dan praproses per *fold* yang sama dengan *naive forecast*, dan hanya tingkat kesulitan 1 (Mudah) atas permintaan penulis (22 Nov 2026). **Data uji tidak dibuka.** Dua model yang dipakai di *notebook* Tahap 5 ditebalkan.

## Tabel ({len(df)} konfigurasi)

{A}

## Cara membaca

* **RMSE** dan **MAE** adalah rata-rata 5 *fold* (µg/m³, makin kecil makin baik). **sd RMSE** adalah simpangan baku antar *fold*, yaitu sebaran kesulitan antar periode. Perbaikan dihitung terhadap RMSE *naive forecast* 86,82.
* Selisih antar hampir semua konfigurasi jauh di bawah sd RMSE (sekitar 19), jadi urutan **tidak berarti** peringkat yang berdekatan berbeda nyata.
* Skor dipilih dari puluhan konfigurasi pada lima *fold* yang sama, sehingga optimistis dan bukan kinerja akhir. Kinerja akhir hanya dari data uji, satu kali.
* Tingkat kesulitan memakai rubrik **[Usulan]** dari struktur konfigurasi saja, tanpa melihat RMSE (lihat kolom skor di `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`). Tingkat 1 berarti *naive* atau model linear (Ridge, Elastic Net) dengan F1 atau F1 ditambah satu kelompok fitur, tanpa penggabungan model, *tuning* acak, atau transformasi target.

## Yang tidak ditampilkan

Konfigurasi tingkat 2 sampai 4 ({N_DIKELUARKAN} konfigurasi) dikeluarkan dari tabel. Ringkasannya, dihitung sebelum dikeluarkan:

{RT}

RMSE terbaik tingkat 1 (selain *naive*) adalah {c(mudah)}, sedangkan tingkat 4 terbaik {c(sulit)}. Selisih sekitar {c(mudah - sulit)} ({c(100 * (mudah - sulit) / mudah, 1)}%) jauh di bawah sd antar *fold*, jadi model yang lebih sulit tidak sepadan dengan beban implementasi dan penjelasannya. Nilai per *fold* semuanya ada di `Hasil/Tabel/t5_tabel_eksperimen_per_fold.csv`, dan tabel lengkap tiap *fold* untuk yang tampil ada di `Hasil/Tabel/t5_tabel_semua_eksperimen.csv`.
"""
open(os.path.join(AKAR, "Laporan", "Tabel Hasil Percobaan Tahap 5.md"), "w", encoding="utf-8").write(md)
print("baris tabel:", len(df))
print(df[["Peringkat", "Konfigurasi", "Fitur", "RMSE rata-rata", "RMSE sd", "MSE rata-rata", "MAE rata-rata"]].head(5).round(2).to_string())
print(df[["Peringkat", "Konfigurasi", "RMSE rata-rata"]].tail(4).round(2).to_string())
