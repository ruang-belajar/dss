# Contoh Kasus HRD — Seleksi Karyawan untuk Promosi (Penyelesaian dengan Metode SAW)

**Situasi:**  
Departemen HRD akan memilih **1 karyawan** untuk dipromosikan menjadi Team Lead dari 4 kandidat (A, B, C, D). Keputusan berdasarkan 5 kriteria yang bersifat kombinasi _benefit_ dan _cost_.

---

## 1. Kriteria & Bobot

- **C1 — Performance (skor 0–100)** — _Benefit_ — **w₁ = 0.35**
    
- **C2 — Experience (tahun)** — _Benefit_ — **w₂ = 0.20**
    
- **C3 — Leadership (penilaian 1–10)** — _Benefit_ — **w₃ = 0.20**
    
- **C4 — Certifications (jumlah sertifikat relevan)** — _Benefit_ — **w₄ = 0.10**
    
- **C5 — Salary Expectation (juta/bulan)** — _Cost_ — **w₅ = 0.15**
    

Total bobot = 0.35 + 0.20 + 0.20 + 0.10 + 0.15 = **1.00**

---

## 2. Matriks Keputusan (nilai asli)

| Kandidat | Performance (C1) | Experience (C2) | Leadership (C3) | Certifications (C4) | Salary Exp (C5) |     |
| :------: | ---------------- | --------------- | --------------- | ------------------- | --------------- | --- |
|    A     | 85               | 6               | 8               | 3                   | 7               |     |
|    B     | 78               | 8               | 7               | 4                   | 6               |     |
|    C     | 92               | 4               | 9               | 2                   | 9               |     |
|    D     | 80               | 10              | 8               | 3                   | 6               |     |

Catatan: C1, C2, C3, C4 = **benefit** (lebih besar lebih baik); C5 = **cost** (lebih kecil lebih baik).

---

## 3. Normalisasi (metode SAW)

Rumus:

- Untuk **benefit**: $r_{ij} = \dfrac{x_{ij}}{\max(x_j)}$
    
- Untuk **cost**: $r_{ij} = \dfrac{\min(x_j)}{x_{ij}}$
    

Nilai ekstrem:

- max(C1) = 92 (C)
    
- max(C2) = 10 (D)
    
- max(C3) = 9 (C)
    
- max(C4) = 4 (B)
    
- min(C5) = 6 (B & D)
    

### Normalisasi (hitung digit-demi-digit)

(Kita tampilkan hingga 12 desimal lalu akan ringkas ke 6 desimal untuk tabel)

**Kandidat A**

- r₁₁ = 85 / 92 = 0.923913043478
    
- r₁₂ = 6 / 10 = 0.600000000000
    
- r₁₃ = 8 / 9 = 0.888888888889
    
- r₁₄ = 3 / 4 = 0.750000000000
    
- r₁₅ = 6 / 7 = 0.857142857143
    

**Kandidat B**

- r₂₁ = 78 / 92 = 0.847826086957
    
- r₂₂ = 8 / 10 = 0.800000000000
    
- r₂₃ = 7 / 9 = 0.777777777778
    
- r₂₄ = 4 / 4 = 1.000000000000
    
- r₂₅ = 6 / 6 = 1.000000000000
    

**Kandidat C**

- r₃₁ = 92 / 92 = 1.000000000000
    
- r₃₂ = 4 / 10 = 0.400000000000
    
- r₃₃ = 9 / 9 = 1.000000000000
    
- r₃₄ = 2 / 4 = 0.500000000000
    
- r₃₅ = 6 / 9 = 0.666666666667
    

**Kandidat D**

- r₄₁ = 80 / 92 = 0.869565217391
    
- r₄₂ = 10 / 10 = 1.000000000000
    
- r₄₃ = 8 / 9 = 0.888888888889
    
- r₄₄ = 3 / 4 = 0.750000000000
    
- r₄₅ = 6 / 6 = 1.000000000000
    

Ringkasan (bulat ke 6 desimal untuk keterbacaan):

|Kandidat|r(C1)|r(C2)|r(C3)|r(C4)|r(C5)|
|:-:|:-:|:-:|:-:|:-:|:-:|
|A|0.923913|0.600000|0.888889|0.750000|0.857143|
|B|0.847826|0.800000|0.777778|1.000000|1.000000|
|C|1.000000|0.400000|1.000000|0.500000|0.666667|
|D|0.869565|1.000000|0.888889|0.750000|1.000000|

---

## 4. Menghitung Skor Preferensi (V_i)

Rumus:  
$$V_i = \sum_{j=1}^{5} w_j \cdot r_{ij}$$  
dengan bobot $w = [0{,}35,;0{,}20,;0{,}20,;0{,}10,;0{,}15]$.

### Perhitungan rinci (digit-demi-digit)

**Kandidat A**

- 0.35 × 0.923913043478 = 0.323369565217
    
- 0.20 × 0.600000000000 = 0.120000000000
    
- 0.20 × 0.888888888889 = 0.177777777778
    
- 0.10 × 0.750000000000 = 0.075000000000
    
- 0.15 × 0.857142857143 = 0.128571428571  
    Jumlah $V_A$ = 0.323369565217 + 0.120000000000 + 0.177777777778 + 0.075000000000 + 0.128571428571 = **0.824718771566**
    

**Kandidat B**

- 0.35 × 0.847826086957 = 0.296739130434
    
- 0.20 × 0.800000000000 = 0.160000000000
    
- 0.20 × 0.777777777778 = 0.155555555556
    
- 0.10 × 1.000000000000 = 0.100000000000
    
- 0.15 × 1.000000000000 = 0.150000000000  
    Jumlah (V_B) = 0.296739130434 + 0.160000000000 + 0.155555555556 + 0.100000000000 + 0.150000000000 = **0.862294685990**
    

**Kandidat C**

- 0.35 × 1.000000000000 = 0.350000000000
    
- 0.20 × 0.400000000000 = 0.080000000000
    
- 0.20 × 1.000000000000 = 0.200000000000
    
- 0.10 × 0.500000000000 = 0.050000000000
    
- 0.15 × 0.666666666667 = 0.100000000000  
    Jumlah $V_C$ = 0.350000000000 + 0.080000000000 + 0.200000000000 + 0.050000000000 + 0.100000000000 = **0.780000000000**
    

**Kandidat D**

- 0.35 × 0.869565217391 = 0.304347826087
    
- 0.20 × 1.000000000000 = 0.200000000000
    
- 0.20 × 0.888888888889 = 0.177777777778
    
- 0.10 × 0.750000000000 = 0.075000000000
    
- 0.15 × 1.000000000000 = 0.150000000000  
    Jumlah $V_D$ = 0.304347826087 + 0.200000000000 + 0.177777777778 + 0.075000000000 + 0.150000000000 = **0.907125603865**
    

(Ringkas ke 6 desimal:)

| Kandidat | Skor (V_i) |
| :------: | :--------: |
|    A     |  0.824719  |
|    B     |  0.862295  |
|    C     |  0.780000  |
|    D     |  0.907126  |

---

## 5. Peringkat & Keputusan

Urutan dari hasil tertinggi → terendah:

1. **Kandidat D** — 0.907126 → **Direkomendasikan untuk promosi (Terbaik)**
    
2. **Kandidat B** — 0.862295
    
3. **Kandidat A** — 0.824719
    
4. **Kandidat C** — 0.780000
    

**Interpretasi singkat:** Kandidat D unggul karena kombinasi pengalaman paling tinggi (10 tahun), leadership baik, serta ekspektasi gaji yang kompetitif (cost rendah). Kandidat C memiliki performance dan leadership terbaik tetapi terhambat karena ekspektasi gaji tinggi dan pengalaman relatif rendah.

---

## 6. Catatan Praktis untuk HRD

- **Sensitivitas bobot:** Hasil SAW sensitif terhadap bobot. Jika HR lebih menekankan leadership atau performance, peringkat bisa berubah. Lakukan analisis sensitivitas (ubah bobot ±10–20%) untuk melihat kestabilan keputusan.
    
- **Validasi kualitatif:** SAW memberi rekomendasi kuantitatif; lakukan wawancara akhir / referensi sebelum keputusan final.
    
- **Normalisasi & skala nilai:** Pastikan skala penilaian (mis. performance 0–100) seragam agar normalisasi adil.
    
- **Dokumentasi:** Simpan matriks dan perhitungan untuk audit kompetensi promosi.
    
