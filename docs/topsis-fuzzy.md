Berikut penjelasan **Fuzzy TOPSIS** yang disusun secara konseptual, metodologis, dan aplikatif dalam konteks **Sistem Pendukung Keputusan (Decision Support System/DSS)**.

---

## 1. Pengertian Fuzzy TOPSIS

**Fuzzy TOPSIS** adalah pengembangan dari metode TOPSIS klasik yang mengintegrasikan **logika fuzzy** untuk menangani:

- Ketidakpastian (_uncertainty_)
    
- Ambiguitas
    
- Penilaian subjektif pengambil keputusan
    

Fuzzy TOPSIS sangat relevan ketika nilai kriteria **tidak dapat dinyatakan secara pasti** atau lebih realistis dinilai menggunakan istilah linguistik, seperti _rendah, sedang, tinggi_.

---

## 2. Latar Belakang Penggunaan Fuzzy TOPSIS

TOPSIS klasik mengasumsikan bahwa:

- Nilai kriteria bersifat pasti (crisp)
    
- Data numerik tersedia dan akurat
    

Dalam praktik DSS, sering dijumpai kondisi:

- Penilaian berbasis persepsi pakar
    
- Data kualitatif dominan
    
- Ketidakpastian lingkungan keputusan
    

Fuzzy TOPSIS dikembangkan untuk mengatasi keterbatasan tersebut.

---

## 3. Konsep Dasar Logika Fuzzy dalam Fuzzy TOPSIS

### a. Variabel Linguistik

Penilaian dinyatakan dalam istilah linguistik, misalnya:

- Sangat Rendah
    
- Rendah
    
- Sedang
    
- Tinggi
    
- Sangat Tinggi
    

### b. Bilangan Fuzzy

Istilah linguistik direpresentasikan sebagai **bilangan fuzzy**, umumnya:

- **Triangular Fuzzy Number (TFN)**: (l, m, u)
    
- **Trapezoidal Fuzzy Number**
    

Contoh:

- “Tinggi” = (0,6; 0,8; 1,0)
    

---

## 4. Prinsip Dasar Fuzzy TOPSIS

Prinsip dasarnya sama dengan TOPSIS klasik:

- Alternatif terbaik adalah yang **paling dekat dengan fuzzy ideal positif**
    
- dan **paling jauh dari fuzzy ideal negatif**
    

Perbedaannya terletak pada:

- Representasi data
    
- Operasi matematika fuzzy
    
- Perhitungan jarak fuzzy
    

---

## 5. Langkah-langkah Umum Fuzzy TOPSIS

### Langkah 1: Menentukan Alternatif dan Kriteria

- Identifikasi alternatif keputusan
    
- Tentukan kriteria (benefit atau cost)
    

---

### Langkah 2: Menentukan Skala Linguistik dan Bilangan Fuzzy

Contoh skala linguistik (TFN):

|Linguistik|TFN (l, m, u)|
|---|---|
|Sangat Rendah|(0,0, 0,2)|
|Rendah|(0,2, 0,4)|
|Sedang|(0,4, 0,6)|
|Tinggi|(0,6, 0,8)|
|Sangat Tinggi|(0,8, 1,0)|

---

### Langkah 3: Membentuk Matriks Keputusan Fuzzy

Nilai kriteria untuk setiap alternatif dinyatakan dalam bilangan fuzzy.

---

### Langkah 4: Normalisasi Matriks Keputusan Fuzzy

Normalisasi dilakukan sesuai jenis kriteria:

- **Benefit**: nilai fuzzy dibagi dengan nilai maksimum fuzzy
    
- **Cost**: nilai minimum fuzzy dibagi dengan nilai fuzzy
    

---

### Langkah 5: Pembobotan Fuzzy

Bobot kriteria juga dinyatakan dalam bilangan fuzzy dan dikalikan dengan matriks normalisasi.

---

### Langkah 6: Menentukan Fuzzy Ideal Positif dan Negatif

- **FPIS (Fuzzy Positive Ideal Solution)**
    
- **FNIS (Fuzzy Negative Ideal Solution)**
    

---

### Langkah 7: Menghitung Jarak Fuzzy

Menghitung jarak setiap alternatif terhadap FPIS dan FNIS, biasanya menggunakan:

- Metode vertex
    
- Euclidean distance fuzzy
    

---

### Langkah 8: Menghitung Koefisien Kedekatan

[  
CC_i = \frac{D_i^-}{D_i^+ + D_i^-}  
]

---

### Langkah 9: Perangkingan Alternatif

Alternatif dengan nilai **CCᵢ terbesar** menjadi pilihan terbaik.

---

## 6. Perbedaan TOPSIS Klasik dan Fuzzy TOPSIS

|Aspek|TOPSIS Klasik|Fuzzy TOPSIS|
|---|---|---|
|Data|Numerik pasti|Linguistik & tidak pasti|
|Ketidakpastian|Tidak ditangani|Ditangani|
|Bobot|Crisp|Fuzzy|
|Kompleksitas|Rendah|Lebih tinggi|
|Interpretasi|Sederhana|Lebih realistis|

---

## 7. Kelebihan dan Keterbatasan Fuzzy TOPSIS

### Kelebihan

- Mampu menangani ketidakpastian dan subjektivitas
    
- Lebih realistis dalam pengambilan keputusan
    
- Cocok untuk evaluasi berbasis pakar
    

### Keterbatasan

- Perhitungan lebih kompleks
    
- Memerlukan pemahaman logika fuzzy
    
- Hasil bergantung pada definisi bilangan fuzzy
    

---

## 8. Aplikasi Fuzzy TOPSIS dalam DSS

Fuzzy TOPSIS banyak digunakan untuk:

- Seleksi supplier
    
- Evaluasi risiko
    
- Penilaian kinerja
    
- Pemilihan teknologi
    
- Penentuan prioritas proyek
    

---

## 9. Referensi

1. Chen, C. T. (2000). Extensions of the TOPSIS for group decision-making under fuzzy environment. _Fuzzy Sets and Systems_, 114(1), 1–9.
    
2. Hwang, C. L., & Yoon, K. (1981). _Multiple Attribute Decision Making: Methods and Applications_. Springer.
    
3. Zadeh, L. A. (1965). Fuzzy sets. _Information and Control_, 8(3), 338–353.
    
4. Kahraman, C. (Ed.). (2008). _Fuzzy Multi-Criteria Decision Making: Theory and Applications_. Springer.
    

---

## 10. Kesimpulan

Fuzzy TOPSIS merupakan pengembangan TOPSIS yang signifikan untuk mendukung keputusan dalam kondisi **tidak pasti dan subjektif**. Dengan mengintegrasikan logika fuzzy, metode ini meningkatkan **realisme dan fleksibilitas** DSS, terutama pada masalah keputusan kompleks yang melibatkan penilaian manusia.

Jika Anda menginginkan, saya dapat menyusun:

- **Contoh perhitungan Fuzzy TOPSIS sederhana**
    
- **Perbandingan hasil TOPSIS vs Fuzzy TOPSIS**
    
- **Template tabel siap pakai untuk perkuliahan**
    

Silakan tentukan kebutuhan lanjutan Anda.