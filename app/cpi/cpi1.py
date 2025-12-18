import csv

# ===============================
# Baca Bobot dari CSV
# ===============================
bobot = []
kriteria = []

with open("bobot.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        kriteria.append(row["kriteria"])
        bobot.append(float(row["bobot"]))

# ===============================
# Baca Data Alternatif dari CSV
# ===============================
alternatif = []
data = []

with open("data_alternatif.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        alternatif.append(row["alternatif"])
        nilai = [float(row[k]) for k in kriteria]
        data.append(nilai)

# ===============================
# Hitung Nilai Minimum Tiap Kriteria
# ===============================
min_kriteria = [min(kolom) for kolom in zip(*data)]

# ===============================
# Normalisasi CPI
# ===============================
normalisasi = []
for i in range(len(data)):
    row = []
    for j in range(len(kriteria)):
        nilai_normal = data[i][j] / min_kriteria[j]
        row.append(nilai_normal)
    normalisasi.append(row)

# ===============================
# Hitung Nilai CPI
# ===============================
nilai_cpi = []
for i in range(len(normalisasi)):
    total = 0
    for j in range(len(bobot)):
        total += normalisasi[i][j] * bobot[j]
    nilai_cpi.append(total)

# ===============================
# Tampilkan Hasil
# ===============================
print("Hasil Perhitungan CPI")
print("---------------------")
for i in range(len(alternatif)):
    print(f"{alternatif[i]} : {nilai_cpi[i]:.4f}")

# ===============================
# Ranking Alternatif
# ===============================
ranking = sorted(
    zip(alternatif, nilai_cpi),
    key=lambda x: x[1],
    reverse=True
)

print("\nRanking Alternatif")
print("------------------")
for i, (alt, nilai) in enumerate(ranking, start=1):
    print(f"Peringkat {i} : {alt} (CPI = {nilai:.4f})")
