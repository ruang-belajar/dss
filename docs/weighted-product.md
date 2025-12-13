# METODE WEIGHTED PRODUCT (WP)

## 1. Pendahuluan

Metode **Weighted Product (WP)** adalah salah satu metode pengambilan keputusan multikriteria (*Multi-Criteria Decision Making* / MCDM) yang menggunakan **perkalian** sebagai dasar agregasi penilaian alternatif.  
Dibandingkan metode penjumlahan (misalnya SAW), WP lebih sensitif terhadap nilai ekstrem karena semua kriteria **dikalikan** dengan bobot berpangkat.

WP sering digunakan pada DSS karena:
- Perhitungan cepat dan sederhana    
- Cocok untuk data skala rasio    
- Mampu menangani perbandingan relatif antar alternatif    

---

## 2. Konsep Dasar Metode Weighted Product

Pada metode WP, setiap nilai alternatif pada kriteria akan dipangkatkan dengan **bobot kriteria $w_j$**.  
Kemudian nilai-nilai tersebut dikalikan untuk menghasilkan nilai preferensi.

### 2.1 Normalisasi Bobot

Bobot harus dinormalkan sehingga:

$$\sum w_j = 1$$ 
Jika bobot belum dinormalisasi:
$$w_j' = \frac{w_j}{\sum w_j}$$

---

## 3. Rumus Dasar Weighted Product

Nilai preferensi suatu alternatif $A_i$ dihitung sebagai:
$$S_i = \prod_{j=1}^{n} x_{ij}^{w_j}$$

Di mana:

- $S_i$: skor alternatif
    
- $x_{ij}$: nilai alternatif $i$ pada kriteria $j$
    
- $w_j$: bobot kriteria
    
### Jika kriteria bersifat COST

Untuk _cost_, bobot dibuat negatif:
$$w_j = -w_j$$

Hal ini membuat nilai kecil lebih diutamakan.

---

## 4. Normalisasi Preferensi

Setelah mendapatkan nilai $S_i$, WP melakukan normalisasi:
$$V_i = \frac{S_i}{\sum_{i=1}^{m} S_i}$$

Di mana:

- $V_i$: nilai akhir alternatif
    
- Alternatif terbaik adalah yang memiliki **nilai V terbesar**
    

---

## 5. Langkah-langkah Perhitungan WP dalam DSS

1. **Menentukan alternatif (A1, A2, A3, …)**
    
2. **Menentukan kriteria (C1, C2, C3, …)**
    
3. **Menentukan bobot tiap kriteria dan normalisasinya**
    
4. **Mengumpulkan data nilai setiap alternatif terhadap kriteria**
    
5. **Melakukan perhitungan WP:**
    - Menaikkan setiap nilai $x_{ij}$ dengan pangkat $w_j$
    - Mengalikan semua hasil untuk mendapatkan $S_i$
        
6. **Melakukan normalisasi menjadi $V_i$**
    
7. **Menentukan alternatif terbaik berdasarkan nilai V tertinggi**
    
---

## 6. Contoh Kasus (Sederhana)

**Pemilihan Laptop untuk kebutuhan perusahaan.**

### Kriteria:

- C1: Harga (Cost) — bobot 4
    
- C2: RAM (Benefit) — bobot 3
    
- C3: Baterai (Benefit) — bobot 3  
    Total bobot = 10 → bobot normalisasi:
    
- w1 = 0.4 (cost → jadi -0.4)
    
- w2 = 0.3
    
- w3 = 0.3

### Alternatif dan Nilai

| Alternatif | Harga (juta) | RAM (GB) | Baterai (jam) |
| ---------- | ------------ | -------- | ------------- |
| A1         | 10           | 8        | 6             |
| A2         | 12           | 16       | 7             |
| A3         | 9            | 8        | 5             |

### Perhitungan nilai S

Contoh perhitungan A1:

$$S_1 = (10^{-0.4}) \times (8^{0.3}) \times (6^{0.3})$$

Hitung S2 dan S3 dengan cara sama.

### Normalisasi
$$V_i = \frac{S_i}{S_1 + S_2 + S_3}$$

Alternatif dengan nilai **V tertinggi** = terpilih.

---

## 7. Kelebihan dan Kekurangan Metode WP

**Kelebihan**
- Perhitungan cepat, sederhana    
- Cocok untuk data rasio    
- Memperhitungkan perbandingan relatif antar alternatif    
- Lebih sensitif terhadap nilai yang sangat baik atau sangat buruk
    
**Kekurangan**
- Tidak cocok untuk data skala ordinal (misalnya skala sangat setuju–sangat tidak setuju)  
- Sensitif terhadap perubahan kecil pada bobot    
- Memerlukan data yang tidak bernilai 0 (karena operasi perkalian)
    
---

## 8. Penerapan WP dalam Sistem Pendukung Keputusan

Metode WP banyak digunakan untuk DSS seperti:
- Seleksi karyawan    
- Pemilihan supplier    
- Rekomendasi produk    
- Evaluasi risiko    
- Optimasi pemilihan proyek    
- Prioritas perawatan mesin    

Dalam DSS digital, WP mudah diimplementasikan karena operasi dasar hanya perkalian dan perpangkatan.

---

## 9. Perbandingan SAW, WP dan MPE

| **Fitur/Kriteria**      | **Simple Additive Weighting (SAW)**                                                                                   | **Perbandingan Eksponensial (Variasi)**                                                                                                                                    | **Weighted Product (WP)**                                                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Konsep Dasar**        | **Penjumlahan Terbobot.** Menentukan nilai total dengan menjumlahkan hasil kali nilai kriteria dan bobotnya (linear). | **Pembobotan Eksponensial/Fuzzy.** Menggunakan fungsi eksponensial untuk mendefinisikan bobot atau mengukur utilitas/preferensi, seringkali untuk menekankan dampak bobot. | **Perkalian Terbobot.** Menentukan nilai preferensi dengan mengalikan nilai kriteria yang telah dipangkatkan dengan bobotnya (non-linear). |
| **Normalisasi Data**    | **Wajib** (untuk menyamakan skala dan unit). Biasanya menggunakan normalisasi Min-Max atau Vektor.                    | **Wajib** (tergantung metode spesifik yang digunakan).                                                                                                                     | **Wajib** (untuk menyamakan skala dan unit).                                                                                               |
| **Formula Inti**        | $V_i = \sum_{j=1}^n w_j \cdot r_{ij}$                                                                                 | Mengandung fungsi eksponensial $e^{...}$ dalam pembobotan atau fungsi utilitas. _Contoh umum:_ $U_i = e^{f(x)}$                                                            | $S_i = \prod_{j=1}^n x_{ij}^{w_j}$                                                                                                         |
| **Sifat Operasi**       | **Linier dan Aditif.** Nilai total adalah penjumlahan.                                                                | **Non-Linier.** Karena menggunakan fungsi eksponensial.                                                                                                                    | **Non-Linier dan Multiplikatif.** Nilai total adalah perkalian.                                                                            |
| **Kompensasi Kriteria** | **Tinggi.** Kekurangan dapat diimbangi oleh kelebihan kriteria lain.                                                  | **Sedang hingga Rendah.** Tergantung fungsi eksponensialnya, ini bisa menekankan atau meredam perbedaan.                                                                   | **Rendah.** Performa buruk (nilai kriteria rendah) pada satu kriteria cenderung sangat memengaruhi nilai akhir.                            |
| **Sensitivitas Bobot**  | Cukup sensitif terhadap perubahan bobot.                                                                              | Sensitivitas tinggi, karena perubahan bobot di tingkat eksponen dapat mengubah hasil secara drastis.                                                                       | Sangat sensitif, karena bobot bertindak sebagai eksponen.                                                                                  |
| **Interpretasi Hasil**  | Mudah diinterpretasikan. Hasil akhir adalah nilai total utilitas.                                                     | Cenderung lebih kompleks. Hasil dapat diinterpretasikan sebagai tingkat utilitas atau preferensi non-linier.                                                               | Relatif mudah. Hasil akhir adalah nilai preferensi relatif.                                                                                |
| **Kelebihan Utama**     | Mudah dipahami, cepat, dan cocok untuk masalah keputusan sederhana.                                                   | Mampu merepresentasikan preferensi yang sangat tajam atau non-linier.                                                                                                      | Perhitungan ringkas. Baik dalam menangani kriteria yang saling bertentangan (trade-off).                                                   |
| **Kekurangan Utama**    | Nilai yang dinormalisasi rentan terhadap perubahan jumlah alternatif.                                                 | Kompleksitas matematis lebih tinggi. Implementasi dan validasi mungkin sulit.                                                                                              | Performa kriteria bernilai nol atau mendekati nol akan menghasilkan nilai preferensi nol atau sangat kecil.                                |

### Analogi untuk Memahami Perbedaan

- **SAW** seperti menjumlahkan nilai ujian setelah dinormalisasi. Sederhana dan langsung.
- **WP** seperti membuat indeks performa dengan perkalian (mirip geometric mean berbobot). Penekanan pada proporsi.
- **MPE** seperti “melipatgandakan” perbedaan kecil sehingga ranking lebih tegas.

---
## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [weighted-product-1.xls](/arsip/weighted-product-1.xls) ([sumber](https://github.com/contohprogram/wp))

 
Modifikasi sheet sesuai kebutuhan

---

## 💼 Diskusi & Tugas

### Soal 1 – Pemilihan Vendor Bahan Baku

Sebuah perusahaan manufaktur akan memilih vendor bahan baku menggunakan metode **Weighted Product (WP)**.

**Kriteria:**

- **C1: Harga** (Cost) — bobot 4
    
- **C2: Kualitas** (Benefit) — bobot 3
    
- **C3: Waktu Pengiriman** (Cost) — bobot 2
        

**Alternatif Vendor & Nilai:**

| Vendor | Harga (juta/ton) | Kualitas (1–10) | Waktu Pengiriman (hari) |
| ------ | ---------------- | --------------- | ----------------------- |
| V1     | 9                | 8               | 5                       |
| V2     | 11               | 9               | 4                       |
| V3     | 10               | 7               | 6                       |

**🙋‍♂️ Tugas:**
1. Normalisasi seluruh bobot.
2. Hitung $S_i$ tiap alternatif (ingat: biaya → bobot negatif).
3. Hitung $V_i$.
4. Tentukan lokasi terbaik berdasarkan nilai WP.
 
---

### Soal 2 – Pemilihan Lokasi Cabang Baru

Sebuah perusahaan retail ingin memilih lokasi cabang baru menggunakan metode **Weighted Product (WP)**.

**Kriteria:**

- **C1: Biaya Sewa** (Cost) — bobot 4
    
- **C2: Potensi Pasar** (Benefit) — bobot 5
    
- **C3: Aksesibilitas** (Benefit) — bobot 3
    
- **C4: Keamanan Lingkungan** (Benefit) — bobot 2
    

**Alternatif Lokasi:**

|Lokasi|Biaya Sewa (juta/bulan)|Potensi Pasar (skor)|Aksesibilitas (skor)|Keamanan (skor)|
|---|---|---|---|---|
|L1|30|85|80|90|
|L2|25|75|85|85|
|L3|35|90|70|95|

**🙋‍♂️ Tugas:**
1. Normalisasi seluruh bobot.
2. Hitung $S_i$ tiap alternatif (ingat: biaya → bobot negatif).
3. Hitung $V_i$.
4. Tentukan lokasi terbaik berdasarkan nilai WP.

---

### Soal 3 - Memilih supplier elektronik

Sebuah perusahaan ingin memilih **supplier komponen elektronik** menggunakan metode **Weighted Product (WP)**.

**1. Kriteria Penilaian**

Perusahaan menggunakan **5 kriteria** berikut:

|Kode|Kriteria|Jenis|Bobot|
|---|---|---|---|
|C1|Harga per unit|Cost|5|
|C2|Kualitas barang|Benefit|4|
|C3|Kecepatan pengiriman|Benefit|3|
|C4|Layanan purna jual|Benefit|2|
|C5|Konsistensi supply|Benefit|1|

**🙋‍♂️ Tugas:**
1. Normalisasi seluruh bobot.
2. Hitung $S_i$ tiap alternatif (ingat: biaya → bobot negatif).
3. Hitung $V_i$.
4. Tentukan lokasi terbaik berdasarkan nilai WP.


---

 **2. Data Alternatif Supplier**

Terdapat **6 alternatif supplier**:

| Supplier | Harga/unit (C1) | Kualitas (C2) | Kecepatan (C3) | Layanan (C4) | Konsistensi (C5) |
| -------- | --------------- | ------------- | -------------- | ------------ | ---------------- |
| A1       | 95              | 85            | 80             | 75           | 90               |
| A2       | 100             | 90            | 85             | 60           | 85               |
| A3       | 110             | 88            | 75             | 70           | 88               |
| A4       | 105             | 82            | 90             | 65           | 92               |
| A5       | 98              | 87            | 78             | 80           | 87               |
| A6       | 120             | 92            | 88             | 72           | 95               |

---

**🙋‍♂️ Tugas:**
1. Normalisasi seluruh bobot.
2. Hitung $S_i$ tiap alternatif (ingat: biaya → bobot negatif).
3. Hitung $V_i$.
4. Tentukan lokasi terbaik berdasarkan nilai WP.
