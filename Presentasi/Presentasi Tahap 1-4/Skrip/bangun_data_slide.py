"""Menghitung data yang ditampilkan di slide Presentasi Tahap 1-4.

Aturan:
- Hanya data latih: baris dengan waktu sebelum BATAS (2016-05-12 19:00).
  Data uji (BATAS dan sesudahnya) tidak dibaca ke perhitungan apa pun.
- Statistik EDA memakai 9 stasiun latih (Dingling, Wanliu, Shunyi adalah stasiun uji).
- Angka yang juga ada di notebook (median, rata-rata, bulan dan jam tertinggi) dicetak
  ulang di akhir supaya bisa dicocokkan dengan keluaran notebook.

Cara menjalankan dari akar repositori:
    python -I "Presentasi/Presentasi Tahap 1-4/Skrip/bangun_data_slide.py"
Keluaran: Presentasi/Presentasi Tahap 1-4/Skrip/data_slide.json
"""
import json
import pathlib

import numpy as np
import pandas as pd

AKAR = pathlib.Path(__file__).resolve().parents[3]
DATA = AKAR / "Data" / "Data Mentah"
KELUAR = pathlib.Path(__file__).resolve().parent / "data_slide.json"

BATAS = pd.Timestamp("2016-05-12 19:00")
STASIUN_UJI = {"Dingling", "Wanliu", "Shunyi"}
STASIUN_CONTOH = "Tiantan"
# Contoh 14 hari (336 jam) dari data latih Tiantan, dipilih karena rata-rata dan RMSE
# naive-nya dekat dengan angka seluruh data latih (bukan karena tampak dramatis).
CONTOH_MULAI = pd.Timestamp("2013-11-11 00:00")
CONTOH_JAM = 336


def muat(nama):
    d = pd.read_csv(DATA / f"{nama}.csv")
    d["waktu"] = pd.to_datetime(d[["year", "month", "day", "hour"]])
    d = d[d["waktu"] < BATAS].sort_values("waktu").reset_index(drop=True)
    assert d["waktu"].max() < BATAS
    return d


nama_stasiun = sorted(p.stem for p in DATA.glob("*.csv"))
latih = [s for s in nama_stasiun if s not in STASIUN_UJI]
assert len(nama_stasiun) == 12 and len(latih) == 9

data = {s: muat(s) for s in latih}
gabung = pd.concat([d.assign(stasiun=s) for s, d in data.items()], ignore_index=True)
pm = gabung["PM2.5"].dropna()

# 1. Ringkasan sebaran (cocokkan dengan notebook 02.3 dan 02.4)
ringkas = {
    "n_pm25": int(pm.size),
    "median": float(pm.median()),
    "rata_rata": round(float(pm.mean()), 1),
    "skew": round(float(pm.skew()), 2),
}

# 2. Histogram PM2.5 (lebar 20, ekor dipotong di 400)
tepi = list(range(0, 400, 20)) + [400]
cnt, _ = np.histogram(pm.clip(upper=399.999), bins=tepi)
hist = {"tepi": tepi, "jumlah": [int(c) for c in cnt], "lebih_dari_400": int((pm >= 400).sum())}

# 3. Pola bulan dan jam (rata-rata PM2.5, 9 stasiun latih)
per_bulan = gabung.groupby("month")["PM2.5"].mean().round(0).astype(int).tolist()
per_jam_f = gabung.groupby("hour")["PM2.5"].mean()
per_jam = per_jam_f.round(0).astype(int).tolist()

# 4. Contoh 14 hari Tiantan (data latih)
t = data[STASIUN_CONTOH].set_index("waktu")["PM2.5"]
contoh = t[CONTOH_MULAI : CONTOH_MULAI + pd.Timedelta(hours=CONTOH_JAM - 1)]
assert len(contoh) == CONTOH_JAM and not contoh.isna().any() and contoh.index.max() < BATAS

# 5. Porsi galat besar pada naive forecast (jam t+24 diprediksi dengan jam t), seluruh data latih
galat = []
for s, d in data.items():
    x = d.set_index("waktu")["PM2.5"]
    y_t = x
    y_f = x.shift(-24, freq="h")  # nilai jam t+24 diletakkan pada indeks jam t
    pasang = pd.concat([y_t.rename("a"), y_f.rename("b")], axis=1, join="inner").dropna()
    galat.append((pasang["b"] - pasang["a"]).to_numpy())
galat = np.concatenate(galat)
mutlak = np.abs(galat)
urut = np.sort(mutlak)[::-1]
k = int(np.ceil(0.05 * urut.size))
porsi = {
    "n_pasang": int(galat.size),
    "top5_porsi_kuadrat": round(float((urut[:k] ** 2).sum() / (urut ** 2).sum()) * 100, 1),
    "top5_porsi_mutlak": round(float(urut[:k].sum() / urut.sum()) * 100, 1),
    "rmse": round(float(np.sqrt((galat ** 2).mean())), 1),
    "mae": round(float(mutlak.mean()), 1),
}

# 6. Rata-rata harian Tiantan sepanjang data latih (latar slide judul)
harian = t.resample("D").mean()
harian = harian.iloc[: int((BATAS - harian.index[0]).days)]
judul = [None if np.isnan(v) else round(float(v), 1) for v in harian.to_numpy()]

keluar = {
    "batas_uji": str(BATAS),
    "stasiun_latih": latih,
    "ringkas": ringkas,
    "hist": hist,
    "per_bulan": per_bulan,
    "per_jam": per_jam,
    "contoh": {
        "stasiun": STASIUN_CONTOH,
        "mulai": str(CONTOH_MULAI),
        "jam": CONTOH_JAM,
        "pm25": [int(v) for v in contoh.to_numpy()],
    },
    "porsi_galat": porsi,
    "judul_harian": {"mulai": str(harian.index[0].date()), "pm25": judul},
}
KELUAR.write_text(json.dumps(keluar, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

print("Cocokkan dengan notebook:")
print("  ringkas      :", ringkas)
print("  bulan tinggi :", int(np.argmax(per_bulan)) + 1, max(per_bulan), "| bulan rendah:", int(np.argmin(per_bulan)) + 1, min(per_bulan))
print("  jam tinggi   :", int(per_jam_f.idxmax()), round(float(per_jam_f.max())), "| jam rendah:", int(per_jam_f.idxmin()), round(float(per_jam_f.min())))
print("  contoh 14 hari: rata-rata", round(float(contoh.mean()), 1), "| RMSE naive", round(float(np.sqrt(((contoh.values[24:] - contoh.values[:-24]) ** 2).mean())), 1))
print("  porsi galat  :", porsi)
print("  hist >=400   :", hist["lebih_dari_400"], "| hari di judul:", len(judul), "| tanggal akhir:", str((harian.index[-1]).date()))
print("Tersimpan:", KELUAR)
