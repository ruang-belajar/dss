# Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)

## 1. Pendahuluan

Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) adalah salah satu metode _Multi Criteria Decision Making_ (MCDM) yang digunakan secara luas dalam Sistem Pendukung Keputusan (Decision Support System/DSS). Metode ini diperkenalkan oleh Hwang dan Yoon (1981) dengan prinsip dasar bahwa alternatif terbaik adalah alternatif yang memiliki jarak terdekat dengan solusi ideal positif dan jarak terjauh dari solusi ideal negatif.

TOPSIS banyak digunakan dalam konteks pengambilan keputusan semi-terstruktur, seperti seleksi, pemeringkatan, dan evaluasi alternatif berdasarkan banyak kriteria.

---

## 2. Konsep Dasar TOPSIS

TOPSIS didasarkan pada beberapa konsep utama:

1. **Alternatif**: objek atau pilihan yang akan dievaluasi.
    
2. **Kriteria**: faktor atau atribut penilaian (benefit atau cost).
    
3. **Bobot Kriteria**: tingkat kepentingan relatif setiap kriteria.
    
4. **Solusi Ideal Positif (A⁺)**: nilai terbaik dari setiap kriteria.
    
5. **Solusi Ideal Negatif (A⁻)**: nilai terburuk dari setiap kriteria.
    
6. **Jarak Euclidean**: ukuran kedekatan alternatif terhadap solusi ideal.
    

---

## 3. Asumsi dan Karakteristik TOPSIS

- Nilai kriteria bersifat numerik dan dapat dibandingkan.
    
- Bobot kriteria telah ditentukan sebelumnya.
    
- Setiap kriteria diasumsikan bersifat monoton (semakin besar semakin baik, atau sebaliknya).
    
- Tidak memperhitungkan hubungan antar kriteria.
    

---

## 4. Langkah-langkah Metode TOPSIS

### Langkah 1: Menyusun Matriks Keputusan

Matriks keputusan X berukuran m × n, dengan:

- m = jumlah alternatif
    
- n = jumlah kriteria
    

xᵢⱼ = nilai alternatif ke-i pada kriteria ke-j

---

### Langkah 2: Normalisasi Matriks Keputusan

Normalisasi dilakukan dengan metode vektor:
$$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

Tujuan normalisasi adalah menghilangkan perbedaan skala antar kriteria.

---

### Langkah 3: Matriks Normalisasi Terbobot

$$y_{ij} = w_j \cdot r_{ij}$$

Dimana:

- wⱼ = bobot kriteria ke-j
    
- ∑ wⱼ = 1
    

---

### Langkah 4: Menentukan Solusi Ideal Positif dan Negatif

Untuk setiap kriteria:

- **Benefit**:
    
    - A⁺ = max(vᵢⱼ)
        
    - A⁻ = min(vᵢⱼ)
        
- **Cost**:
    
    - A⁺ = min(vᵢⱼ)
        
    - A⁻ = max(vᵢⱼ)
        

---

### Langkah 5: Menghitung Jarak ke Solusi Ideal

**Jarak ke Ideal Positif:** 

  $D_i^+ = \sqrt{\sum_{j=1}^{n} (y_{ij} - y_j^+)^2}$
    
**Jarak ke Ideal Negatif:** 

  $D_i^- = \sqrt{\sum_{j=1}^{n} (y_{ij} - y_j^-)^2}$

---

### Langkah 6: Menghitung Nilai Preferensi

$$V_i = \frac{D_i^-}{D_i^- + D_i^+}$$

Nilai $V_i$ berada di rentang 0 hingga 1. **Semakin mendekati 1, semakin baik alternatif tersebut.**

---

### Langkah 7: Perangkingan Alternatif

Alternatif dengan nilai Cᵢ terbesar merupakan alternatif terbaik.

---

## 5. Interpretasi Hasil dalam DSS

Dalam konteks Sistem Pendukung Keputusan:

- Nilai preferensi digunakan sebagai dasar rekomendasi.
    
- TOPSIS sangat cocok untuk modul _ranking engine_.
    
- Hasil dapat divisualisasikan dalam bentuk tabel, grafik, atau dashboard DSS.
    

---

## 6. Kelebihan dan Keterbatasan TOPSIS

### Kelebihan:

- Konsep intuitif dan mudah dipahami.
    
- Mempertimbangkan solusi ideal terbaik dan terburuk sekaligus.
    
- Komputasi relatif sederhana.
    
- Cocok untuk jumlah alternatif yang cukup besar.
    

### Keterbatasan:

- Sangat bergantung pada bobot kriteria.
    
- Tidak mempertimbangkan ketidakpastian data.
    
- Sensitif terhadap metode normalisasi.
    

---

## 7. Perbandingan Singkat dengan Metode Lain

|Metode|Karakteristik Utama|Perbedaan dengan TOPSIS|
|---|---|---|
|SAW|Penjumlahan terbobot|Tidak menggunakan solusi ideal|
|WP|Perkalian terbobot|Menggunakan rasio, bukan jarak|
|CPI|Indeks komposit|Fokus pada indeks relatif|
|MPE|Fungsi eksponensial|Sensitif terhadap perbedaan nilai|
|AHP|Perbandingan berpasangan|Fokus pada penentuan bobot|

---

## 8. Contoh Penerapan TOPSIS

TOPSIS dapat diterapkan pada:

- Seleksi karyawan atau mahasiswa
    
- Pemilihan supplier
    
- Penentuan prioritas proyek
    
- Evaluasi risiko
    
- Rekomendasi produk atau layanan
    

---

## 9. Ringkasan

TOPSIS merupakan metode MCDM yang efektif dan populer dalam Sistem Pendukung Keputusan. Dengan pendekatan solusi ideal, TOPSIS mampu memberikan hasil perangkingan yang rasional, sistematis, dan mudah diinterpretasikan oleh pengambil keputusan.

---

## 📚 Referensi Singkat

- Hwang, C. L., & Yoon, K. (1981). _Multiple Attribute Decision Making: Methods and Applications_. Springer.
    
- Triantaphyllou, E. (2000). _Multi-Criteria Decision Making Methods_. Springer.