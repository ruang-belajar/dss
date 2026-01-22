# Additive Ratio Assessment (ARAS)

## 1. Pendahuluan

Additive Ratio Assessment (ARAS) merupakan salah satu metode **Multi-Criteria Decision Making (MCDM)** yang digunakan untuk menentukan peringkat alternatif berdasarkan tingkat kedekatannya terhadap **alternatif optimal**. Metode ini menilai setiap alternatif dengan cara membandingkan **rasio kinerja total alternatif** terhadap **nilai optimal**.

Dalam konteks **Decision Support System (DSS)**, ARAS digunakan untuk:
- Seleksi alternatif terbaik
- Evaluasi kinerja multi-kriteria
- Mendukung pengambilan keputusan yang bersifat kuantitatif dan transparan
    

---

## 2. Konsep Dasar ARAS

Prinsip utama ARAS adalah:
- Setiap alternatif dibandingkan dengan **alternatif ideal (A₀)**.
- Nilai fungsi optimalitas (optimality function) menjadi dasar pemeringkatan.
- Alternatif terbaik adalah yang memiliki **nilai utilitas tertinggi**.

Karakteristik utama:
- Menggunakan pendekatan **additive (penjumlahan terbobot)**.
- Mengakomodasi **kriteria benefit dan cost**.
- Hasil akhir berupa **ranking dan nilai utilitas relatif**.

---

## 3. Notasi dan Terminologi

- $A_i$ : Alternatif ke-i
- $C_j$ : Kriteria ke-j
- $x_{ij}$ : Nilai alternatif ke-i pada kriteria ke-j
- $w_j$ : Bobot kriteria ke-j
- $S_i$ : Nilai fungsi optimalitas alternatif ke-i
- $K_i$ : Nilai utilitas relatif alternatif ke-i

---

## 4. Langkah-Langkah Metode ARAS

### Contoh Kasus

**Masalah:** Pemilihan supplier terbaik  
**Alternatif:** A1, A2, A3

**Kriteria dan Bobot:**

|Kriteria|Jenis|Bobot|
|---|---|---|
|C1 – Kualitas|Benefit|0,4|
|C2 – Harga|Cost|0,3|
|C3 – Ketepatan Waktu|Benefit|0,3|
|**Total**||**1,0**|

**Matriks Keputusan Awal:**

|Alternatif|C1|C2|C3|
|---|---|---|---|
|A1|80|70|90|
|A2|75|60|85|
|A3|90|80|95|

---

### Langkah 1: Menentukan Alternatif Optimal (A₀)

Aturan:
- **Benefit → nilai maksimum**
- **Cost → nilai minimum**

|Alternatif|C1 (Max)|C2 (Min)|C3 (Max)|
|---|---|---|---|
|**A₀**|90|60|95|

---

### Langkah 2: Membentuk Matriks Keputusan ARAS

| Alternatif | C1  | C2  | C3  |
| ---------- | --- | --- | --- |
| A₀         | 90  | 60  | 95  |
| A1         | 80  | 70  | 90  |
| A2         | 75  | 60  | 85  |
| A3         | 90  | 80  | 95  |

---

### Langkah 3: Normalisasi Matriks Keputusan

#### Normalisasi Kriteria Benefit (C1 dan C3)

Rumus:  

$$\bar{x}_{ij} = \frac{x_{ij}}{\sum_{i=0}^{m} x_{ij}}$$

**C1 (Kualitas):**  
ΣC1 = 90 + 80 + 75 + 90 = **335**
- A₀ = 90 / 335 = 0,2687
- A1 = 80 / 335 = 0,2388
- A2 = 75 / 335 = 0,2239
- A3 = 90 / 335 = 0,2687

**C3 (Ketepatan Waktu):**  
ΣC3 = 95 + 90 + 85 + 95 = **365**
- A₀ = 95 / 365 = 0,2603
- A1 = 90 / 365 = 0,2466
- A2 = 85 / 365 = 0,2329
- A3 = 95 / 365 = 0,2603

---

#### Normalisasi Kriteria Cost (C2)

Rumus:  
$$\bar{x}_{ij} = \frac{\frac{1}{x_{ij}}}{\sum_{i=0}^{m} \frac{1}{x_{ij}}}$$

Nilai invers:
- A₀ = 1/60 = 0,01667
- A1 = 1/70 = 0,01429
- A2 = 1/60 = 0,01667
- A3 = 1/80 = 0,01250

Σ invers = **0,06013**

Normalisasi:
- A₀ = 0,01667 / 0,06013 = 0,2772
- A1 = 0,01429 / 0,06013 = 0,2376
- A2 = 0,01667 / 0,06013 = 0,2772
- A3 = 0,01250 / 0,06013 = 0,2079

---

### Langkah 4: Matriks Normalisasi Terbobot

Rumus:  
$$v_{ij} = \bar{x}_{ij} \times w_j$$

|Alternatif|C1 (0,4)|C2 (0,3)|C3 (0,3)|
|---|---|---|---|
|A₀|0,1075|0,0832|0,0781|
|A1|0,0955|0,0713|0,0740|
|A2|0,0896|0,0832|0,0699|
|A3|0,1075|0,0624|0,0781|

---

### Langkah 5: Menghitung Fungsi Optimalitas (Si)

Rumus:  

$$S_i = \sum v_{ij}$$

|Alternatif|Si|
|---|---|
|A₀|**0,2688**|
|A1|0,2408|
|A2|0,2427|
|A3|0,2480|

---

### Langkah 6: Menghitung Nilai Utilitas Relatif (Ki)

Rumus:  

$$K_i = \frac{S_i}{S_0}$$

| Alternatif | Ki        |
| ---------- | --------- |
| A1         | 0,896     |
| A2         | 0,903     |
| A3         | **0,923** |

---

### Langkah 7: Perangkingan Alternatif

| Peringkat | Alternatif | Ki    |
| --------- | ---------- | ----- |
| 1         | **A3**     | 0,923 |
| 2         | A2         | 0,903 |
| 3         | A1         | 0,896 |

---

### Kesimpulan
- Alternatif **A3** merupakan pilihan terbaik berdasarkan metode ARAS.
- Nilai utilitas menunjukkan tingkat kedekatan setiap alternatif terhadap alternatif optimal.
- ARAS memberikan hasil yang **kuantitatif, transparan, dan mudah diinterpretasikan** dalam DSS.
    
---

## 5. Kelebihan dan Keterbatasan ARAS

### Kelebihan:
- Konsep sederhana dan mudah dipahami
- Memiliki alternatif optimal sebagai pembanding langsung
- Cocok untuk DSS berbasis kuantitatif
- Hasil berupa nilai utilitas relatif yang informatif

### Keterbatasan:
- Sensitif terhadap penentuan alternatif optimal
- Sangat bergantung pada bobot kriteria
- Tidak mempertimbangkan jarak solusi seperti TOPSIS
    
---

## 6. Perbandingan Singkat dengan Metode Lain

|Metode|Pendekatan|Output|
|---|---|---|
|SAW|Penjumlahan terbobot|Skor|
|WP|Perkalian terbobot|Skor relatif|
|TOPSIS|Jarak solusi ideal|Closeness coefficient|
|**ARAS**|Rasio terhadap alternatif optimal|Nilai utilitas|

---

## 7. Implementasi ARAS dalam DSS

ARAS sering digunakan dalam DSS untuk:
- Seleksi karyawan
- Penentuan supplier
- Pemilihan lokasi
- Evaluasi kinerja proyek
- Sistem rekomendasi berbasis multi-kriteria

---

## 8. Ringkasan
- ARAS adalah metode MCDM berbasis rasio aditif.
- Menggunakan alternatif optimal sebagai benchmark.
- Menghasilkan nilai utilitas yang mudah diinterpretasikan.
- Sangat sesuai untuk DSS yang memerlukan transparansi keputusan.

---

## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [Template ARAS (Google Sheet)](https://docs.google.com/spreadsheets/d/1IxVEt4VBbn8jTkM_8XWpzntV-38NTyMeH5dMZHqB4nI/edit?usp=sharing)
 
Modifikasi sheet sesuai kebutuhan

---

## 💼 Diskusi & Tugas

Buat perhitungan pengambilan keputusan menggunakan ARAS, menggunakan data pada latihan sebelumnya:

1. [Soal 1 - CPI](cpi.md#soal-1--seleksi-penerima-beasiswa)
2. [Soal 2 - CPI](cpi.md#soal-2--pemilihan-supplier)
3. [Soal 3 - SAW](saw.md#soal-3----pemilihan-lokasi-cabang-restoran-baru)

---

## Referensi
1. Zavadskas, E. K., & Turskis, Z. (2010). _A new additive ratio assessment (ARAS) method in multicriteria decision-making_. **Technological and Economic Development of Economy**, 16(2), 159–172.
2. Zavadskas, E. K., Turskis, Z., & Antucheviciene, J. (2015). _Multiple Criteria Decision Making (MCDM) Methods in Economics_. Springer.
3. Hwang, C. L., & Yoon, K. (1981). _Multiple Attribute Decision Making: Methods and Applications_. Springer.
4. Triantaphyllou, E. (2000). _Multi-Criteria Decision Making Methods: A Comparative Study_. Springer.
5. Kaliszewski, I. (2006). _Soft Computing for Complex Multiple Criteria Decision Making_. Springer.
    
