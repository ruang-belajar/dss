# Weighted MOORA


**Weighted MOORA** adalah pengembangan dari metode [MOORA](moora.md) **(Multi-Objective Optimization by Ratio Analysis)** yang **memasukkan bobot kriteria** untuk merepresentasikan **tingkat kepentingan relatif** masing-masing kriteria dalam pengambilan keputusan.

Secara konseptual:
- Nilai setiap kriteria **dinormalisasi** terlebih dahulu menggunakan normalisasi vektor MOORA.
- Hasil normalisasi kemudian **dikalikan dengan bobot kriteria**.
- Nilai akhir alternatif diperoleh dari **penjumlahan kriteria benefit** dikurangi **penjumlahan kriteria cost** yang telah berbobot.

Keunggulan utama Weighted MOORA adalah:
- Lebih **realistis** dibanding MOORA klasik ketika kepentingan kriteria tidak sama.
- Tetap **sederhana dan efisien secara komputasi**.
- Fleksibel untuk dikombinasikan dengan metode penentuan bobot seperti **AHP, Entropy, atau ROC**.

Dalam konteks **Sistem Pendukung Keputusan**, Weighted MOORA digunakan ketika pengambil keputusan ingin mempertahankan kesederhanaan MOORA, tetapi tetap **mengakomodasi preferensi dan prioritas kriteria secara eksplisit**.
## Langkah-langkah Metode Weighted MOORA

**Contoh Kasus:** Sebuah institusi ingin memilih **alternatif terbaik** dari 3 alternatif berdasarkan 3 kriteria yang **memiliki tingkat kepentingan berbeda**.

### 1. Menentukan Alternatif dan Kriteria

**Alternatif**: *A1, A2, A3*

**Kriteria dan Bobot**

| Kode      | Kriteria   | Jenis   | Bobot    |
| --------- | ---------- | ------- | -------- |
| C1        | Kualitas   | Benefit | 0.40     |
| C2        | Biaya      | Cost    | 0.35     |
| C3        | Pengalaman | Benefit | 0.25     |
| **Total** |            |         | **1.00** |

---

### 2. Matriks Keputusan

|Alternatif|C1|C2|C3|
|---|---|---|---|
|A1|80|5|4|
|A2|70|4|5|
|A3|90|6|3|

---

### 3. Normalisasi Matriks Keputusan

Rumus normalisasi MOORA:

$$x^*_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

**Penyebut setiap kriteria**

- C1: $\sqrt{80^2 + 70^2 + 90^2} = 139.29$
    
- C2: $\sqrt{5^2 + 4^2 + 6^2} = 8.77$
    
- C3: $\sqrt{4^2 + 5^2 + 3^2} = 7.07$
    

---

### **Matriks Normalisasi**

|Alternatif|C1|C2|C3|
|---|---|---|---|
|A1|0.574|0.570|0.566|
|A2|0.503|0.456|0.707|
|A3|0.646|0.684|0.424|

---

### 4. Normalisasi Berbobot (Weighted Normalization)

Setiap nilai normalisasi dikalikan dengan bobot kriteria:

$$x^{**}_{ij} = w_j \cdot x^*_{ij}$$

 **Matriks Normalisasi Berbobot**

|Alternatif|C1 (0.40)|C2 (0.35)|C3 (0.25)|
|---|---|---|---|
|A1|0.230|0.200|0.142|
|A2|0.201|0.160|0.177|
|A3|0.258|0.239|0.106|

---

### 5. Menghitung Nilai Optimasi Weighted MOORA

Rumus:

$$Y_i = \sum (\text{Benefit}) - \sum (\text{Cost})$$

**Perhitungan**
* ***A1**: $Y_1 = (0.230 + 0.142) - 0.200 = 0.172$

- **A2**: $Y_2 = (0.201 + 0.177) - 0.160 = 0.218$

- **A3**: $Y_3 = (0.258 + 0.106) - 0.239 = 0.125$

---

### 6. Perangkingan Alternatif

|Alternatif|Nilai (Y_i)|Peringkat|
|---|---|---|
|**A2**|**0.218**|**1 (Terbaik)**|
|A1|0.172|2|
|A3|0.125|3|

---

### 7. Interpretasi Hasil

- **A2** menjadi alternatif terbaik karena:
    - Biaya relatif rendah (kriteria cost berbobot besar)
    - Pengalaman tinggi (benefit)
- Penggunaan bobot:
    - Menggeser hasil dibanding MOORA tanpa bobot
    - Mencerminkan preferensi pengambil keputusan secara eksplisit

