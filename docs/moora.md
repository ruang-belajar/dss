# **Metode Multi-Objective Optimization by Ratio Analysis (MOORA)**

## 1. Pendahuluan

Dalam Sistem Pendukung Keputusan (SPK), sering dijumpai permasalahan pemilihan alternatif terbaik yang melibatkan **lebih dari satu kriteria**, di mana sebagian kriteria bersifat _benefit_ dan sebagian lainnya _cost_. Untuk menyelesaikan permasalahan tersebut digunakan metode **Multi-Criteria Decision Making (MCDM)**, salah satunya adalah **Multi-Objective Optimization by Ratio Analysis (MOORA)**.

Metode MOORA dikenal karena **kesederhanaan konsep, stabilitas hasil, dan efisiensi komputasi**, sehingga banyak digunakan dalam pengambilan keputusan praktis di berbagai sektor.

---

## 2. Konsep Dasar Metode MOORA

**MOORA (Multi-Objective Optimization by Ratio Analysis)** adalah metode pengambilan keputusan multikriteria yang bertujuan untuk mengoptimalkan beberapa tujuan (objectives) secara simultan dengan menggunakan **rasio normalisasi nilai kriteria**.

Prinsip utama MOORA adalah:

- Setiap alternatif dinilai terhadap seluruh kriteria
    
- Nilai kriteria dinormalisasi untuk menghilangkan perbedaan skala
    
- Kriteria _benefit_ dimaksimalkan dan kriteria _cost_ diminimalkan
    
- Alternatif terbaik ditentukan berdasarkan nilai optimasi total
    

---

## 3. Sejarah dan Pengembangan MOORA

Metode MOORA diperkenalkan oleh **Willem K. M. Brauers dan Edmundas Kazimieras Zavadskas** pada tahun **2006**. Metode ini dikembangkan sebagai pendekatan optimasi multi-objektif yang **lebih sederhana dan lebih stabil** dibandingkan beberapa metode MCDM lainnya.

Seiring perkembangan, MOORA banyak dikombinasikan dengan metode lain seperti **AHP, Entropy, dan Fuzzy Logic** untuk meningkatkan akurasi bobot kriteria dan menangani ketidakpastian data.

---

## 4. Langkah-Langkah Metode MOORA

**Contoh Kasus:** Sebuah organisasi ingin memilih **alternatif terbaik** dari 3 kandidat berdasarkan 3 kriteria.

**Alternatif:** *A1, A2, A3*

**Kriteria**

|Kode|Kriteria|Jenis|
|---|---|---|
|C1|Kualitas|Benefit|
|C2|Biaya|Cost|
|C3|Pengalaman|Benefit|

---

### Langkah 1 – Menyusun Matriks Keputusan

Nilai awal masing-masing alternatif terhadap kriteria:

|Alternatif|C1 (Benefit)|C2 (Cost)|C3 (Benefit)|
|---|---|---|---|
|A1|80|5|4|
|A2|70|4|5|
|A3|90|6|3|

Matriks keputusan:

$$X =  
\begin{bmatrix}  
80 & 5 & 4 \\ 
70 & 4 & 5 \\
90 & 6 & 3  
\end{bmatrix}  
$$

---

### Langkah 2 – Normalisasi Matriks Keputusan

Normalisasi dilakukan dengan rumus MOORA:

$$
x^*_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}  
$$

**Hitung penyebut setiap kriteria**

- C1: $\sqrt{80^2 + 70^2 + 90^2} = \sqrt{19400} = 139.29$
    
- C2: $\sqrt{5^2 + 4^2 + 6^2} = \sqrt{77} = 8.77$
    
- C3: $\sqrt{4^2 + 5^2 + 3^2} = \sqrt{50} = 7.07$
    

**Matriks Normalisasi**

|Alternatif|C1|C2|C3|
|---|---|---|---|
|A1|0.574|0.570|0.566|
|A2|0.503|0.456|0.707|
|A3|0.646|0.684|0.424|

---

### Langkah 3 – Menghitung Nilai Optimasi MOORA

Rumus nilai optimasi:

$$Y_i = \sum (\text{Benefit}) - \sum (\text{Cost})$$

**Hitung untuk setiap alternatif**

- **A1**: $Y_1 = (0.574 + 0.566) - 0.570 = 0.570$
- **A2:** $Y_2 = (0.503 + 0.707) - 0.456 = 0.754$
- **A3:** $Y_3 = (0.646 + 0.424) - 0.684 = 0.386$

---

### Langkah 4 – Perangkingan Alternatif

| Alternatif | Nilai (Y_i) | Peringkat   |
| ---------- | ----------- | ----------- |
| A2         | 0.754       | 1 (Terbaik) |
| A1         | 0.570       | 2           |
| A3         | 0.386       | 3           |

---

### **Interpretasi**

- **A2** merupakan alternatif terbaik karena memiliki nilai optimasi tertinggi.
- MOORA berhasil:
    - Memaksimalkan kriteria _benefit_
    - Meminimalkan kriteria _cost_
- Hasil perhitungan bersifat **objektif dan transparan**, sehingga sangat sesuai untuk:
    - Sistem rekomendasi
    - Sistem seleksi
    - Sistem perankingan alternatif

---

## 5. Aplikasi Metode MOORA dalam SPK

Metode MOORA banyak digunakan dalam berbagai konteks Sistem Pendukung Keputusan, antara lain:
- Pemilihan supplier atau vendor terbaik
- Seleksi penerima bantuan sosial
- Pemilihan karyawan atau siswa berprestasi
- Pemilihan proyek atau investasi
- Rekomendasi produk (kendaraan, rumah, perangkat IT)
- Penilaian kinerja organisasi atau unit kerja

---

## 6. Kelebihan dan Kelemahan Metode MOORA

### 6.1 Kelebihan

- Struktur perhitungan sederhana dan mudah dipahami
- Komputasi efisien untuk jumlah alternatif besar
- Mampu menangani kriteria _benefit_ dan _cost_ secara simultan
- Cocok untuk implementasi SPK berbasis komputer

### 6.2 Kelemahan

- Sensitif terhadap bobot kriteria jika bobot tidak ditentukan secara sistematis
- Tidak mempertimbangkan hubungan antar kriteria
- Kurang fleksibel dalam menangani ketidakpastian tanpa pendekatan fuzzy


---

## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [Template MOORA (Google Sheet)](https://docs.google.com/spreadsheets/d/1NkbBqeTo-EEXvHVuItHrrCk0RgtNvrs-NLyLmELJsIg/edit?usp=sharing)
 
Modifikasi sheet sesuai kebutuhan

---

## 📚 Referensi

1. Brauers, W. K. M., & Zavadskas, E. K. (2006). _The MOORA method and its application to privatization in a transition economy_. Control and Cybernetics, 35(2), 445–469.
2. Brauers, W. K. M., & Zavadskas, E. K. (2010). _Project management by MULTIMOORA as an instrument for transition economies_. Technological and Economic Development of Economy, 16(1), 5–24.
3. Hwang, C. L., & Yoon, K. (1981). _Multiple Attribute Decision Making: Methods and Applications_. Springer.
4. Sif UIN Suska Riau. _Chapter MOORA – Multi-Criteria Decision Making_.
5. Razooqee, M. N., & Ashour, M. A. H. (2016). _Application of MOORA Method in Multi-Objective Optimization_. Journal of Engineering and Applied Sciences.
    
