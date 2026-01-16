## 1. Pengertian Dynamic TOPSIS

**Dynamic TOPSIS** adalah pengembangan metode TOPSIS klasik yang dirancang untuk **masalah pengambilan keputusan yang bersifat dinamis**, yaitu kondisi di mana:
- Nilai kriteria berubah dari waktu ke waktu
- Bobot kriteria dapat berubah mengikuti konteks
- Alternatif dapat dievaluasi secara periodik

Berbeda dengan TOPSIS klasik yang bersifat **statis (single-shot decision)**, Dynamic TOPSIS mempertimbangkan **dimensi waktu (time dimension)** dalam proses evaluasi dan perangkingan.

---

## 2. Latar Belakang Pengembangan

TOPSIS klasik memiliki asumsi utama:
- Data dan bobot bersifat tetap
- Evaluasi dilakukan satu kali

Dalam praktik DSS modern, sering dijumpai:
- Kinerja alternatif fluktuatif (misalnya kinerja supplier per bulan)
- Perubahan prioritas manajemen
- Lingkungan keputusan yang tidak stabil

Dynamic TOPSIS dikembangkan untuk menjawab kebutuhan tersebut.

---

## 3. Konsep Dasar Dynamic TOPSIS

Konsep inti Dynamic TOPSIS adalah:

> _Alternatif terbaik adalah alternatif yang secara konsisten paling dekat dengan solusi ideal sepanjang horizon waktu tertentu._

Dengan demikian, penilaian tidak hanya berbasis satu titik waktu, tetapi **agregasi performa lintas waktu**.

---

## 4. Elemen Kunci Dynamic TOPSIS

### 1. Dimensi Waktu (t)
- Evaluasi dilakukan pada beberapa periode waktu (t₁, t₂, …, tₖ)
- Setiap periode memiliki matriks keputusan sendiri

---

### 2. Bobot Waktu (Time Weight)
- Setiap periode dapat diberi bobot berbeda
- Periode terbaru sering diberi bobot lebih besar (_time preference_)

---

### 3. Perubahan Bobot Kriteria
- Bobot kriteria dapat:
    - Tetap sepanjang waktu
    - Berubah setiap periode
- Penyesuaian bobot mencerminkan dinamika preferensi pengambil keputusan

---

## 5. Pendekatan Implementasi Dynamic TOPSIS

Terdapat beberapa pendekatan umum:

---

### Pendekatan 1: TOPSIS Per Periode + Agregasi

1. Hitung TOPSIS untuk setiap periode waktu
    
2. Diperoleh nilai preferensi Cᵢ(t)
    
3. Agregasi nilai preferensi menggunakan:
    
    - Rata-rata berbobot waktu
        
    - Exponential smoothing
        
    - Moving average
        

[  
C_i^{final} = \sum_{t=1}^{T} \alpha_t \cdot C_i(t)  
]

---

### Pendekatan 2: Matriks Keputusan Dinamis

1. Gabungkan data lintas waktu menjadi satu matriks besar
    
2. Normalisasi mempertimbangkan dimensi waktu
    
3. Hitung solusi ideal global
    

Pendekatan ini lebih kompleks dan jarang digunakan dalam praktik pendidikan.

---

## 6. Perhitungan Dasar (Ilustratif)

Jika nilai preferensi alternatif A pada 3 periode adalah:

- C(A, t₁) = 0,62
    
- C(A, t₂) = 0,71
    
- C(A, t₃) = 0,80
    

Dengan bobot waktu:

- α₁ = 0,2
    
- α₂ = 0,3
    
- α₃ = 0,5
    

Maka:

$$C_A^{final} = (0,2)(0,62) + (0,3)(0,71) + (0,5)(0,80) = 0,74$$

---

## 7. Perbandingan TOPSIS Klasik dan Dynamic TOPSIS

| Aspek          | TOPSIS Klasik  | Dynamic TOPSIS   |
| -------------- | -------------- | ---------------- |
| Dimensi waktu  | Tidak ada      | Ada              |
| Data           | Statis         | Dinamis          |
| Bobot kriteria | Tetap          | Dapat berubah    |
| Output         | Satu peringkat | Tren & peringkat |
| Kompleksitas   | Rendah         | Menengah–tinggi  |

---

## 8. Kelebihan dan Keterbatasan Dynamic TOPSIS

### Kelebihan

- Lebih realistis untuk sistem nyata
    
- Mampu menangkap tren kinerja
    
- Cocok untuk DSS berbasis monitoring
    

### Keterbatasan

- Kompleksitas perhitungan meningkat
    
- Penentuan bobot waktu bersifat subjektif
    
- Interpretasi hasil lebih kompleks
    

---

## 9. Aplikasi Dynamic TOPSIS dalam DSS

Dynamic TOPSIS banyak digunakan untuk:

- Evaluasi kinerja supplier berkelanjutan
    
- Monitoring risiko
    
- Penilaian kinerja organisasi
    
- Prioritisasi proyek jangka menengah–panjang
    

---

## 10. Referensi

1. Shih, H. S., Shyur, H. J., & Lee, E. S. (2007). An extension of TOPSIS for group decision making. _Mathematical and Computer Modelling_, 45(7–8), 801–813.
    
2. Zavadskas, E. K., Turskis, Z., & Vilutienė, T. (2010). Multiple criteria analysis of foundation alternatives using TOPSIS method. _Technological and Economic Development of Economy_, 16(2), 241–257.
    
3. Triantaphyllou, E. (2000). _Multi-Criteria Decision Making Methods_. Springer.
    
4. Xu, Z. (2004). On compatibility of interval fuzzy preference relations. _Fuzzy Optimization and Decision Making_, 3(3), 217–225.
    
