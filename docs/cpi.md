# METODE COMPOSITE PERFORMANCE INDEX (CPI)

---

## 1. Pendahuluan

Dalam **Sistem Pendukung Keputusan (Decision Support System)**, sering kali pengambil keputusan dihadapkan pada pemilihan alternatif terbaik berdasarkan **banyak kriteria** dengan **satuan dan skala yang berbeda**.  
Metode **Composite Performance Index (CPI)** merupakan salah satu metode _Multi-Criteria Decision Making (MCDM)_ yang digunakan untuk **menggabungkan kinerja alternatif pada berbagai kriteria menjadi satu nilai indeks komposit**.

CPI menekankan pada:

- Normalisasi terhadap **nilai minimum**
    
- Interpretasi hasil dalam bentuk **indeks kinerja relatif**
    
- Kemudahan analisis dan transparansi perhitungan
    

---

## 2. Konsep Dasar Composite Performance Index

### 2.1 Definisi

**Composite Performance Index (CPI)** adalah metode pengambilan keputusan yang menghitung **nilai indeks gabungan** dari beberapa kriteria dengan cara:

1. Menormalkan nilai kriteria terhadap nilai minimum
    
2. Mengalikan hasil normalisasi dengan bobot kriteria
    
3. Menjumlahkan seluruh nilai terbobot untuk setiap alternatif
    

Alternatif dengan **nilai CPI tertinggi** dianggap sebagai alternatif terbaik.

---

### 2.2 Karakteristik Metode CPI

|Karakteristik|Penjelasan|
|---|---|
|Jenis metode|Multi-Criteria Decision Making|
|Pendekatan|Penjumlahan terbobot|
|Normalisasi|Berbasis nilai minimum|
|Output|Nilai indeks komposit|
|Interpretasi|Semakin besar nilai CPI → semakin baik|

---

## 3. Komponen Utama Metode CPI

Dalam metode CPI terdapat beberapa komponen utama:

1. **Alternatif (Ai)**  
    Pilihan atau objek yang akan dibandingkan
    
2. **Kriteria (Cj)**  
    Faktor penilaian yang memengaruhi keputusan
    
3. **Bobot Kriteria (Wj)**  
    Tingkat kepentingan masing-masing kriteria  
    $$\sum W_j = 1$$
    
4. **Matriks Keputusan $Xij$**  
    Nilai kinerja alternatif ke-i terhadap kriteria ke-j
    

---

## 4. Jenis Kriteria dalam CPI

### 4.1 Kriteria Benefit

- Semakin **besar** nilai → semakin **baik**
    
- Contoh: kualitas, produktivitas, kepuasan
    

### 4.2 Kriteria Cost

- Semakin **kecil** nilai → semakin **baik**
    
- Contoh: biaya, waktu, risiko
    

Metode CPI menangani perbedaan ini pada tahap **normalisasi**.

---

## 5. Langkah-Langkah Metode Composite Performance Index

### Langkah 1: Menyusun Matriks Keputusan

$$X = [x_{ij}]$$

---

### Langkah 2: Menentukan Nilai Minimum Tiap Kriteria

$$x_j^{min} = \min(x_{1j}, x_{2j}, ..., x_{nj})$$

---

### Langkah 3: Normalisasi Nilai Kriteria

- **Untuk kriteria benefit:**  
    $$r_{ij} = \frac{x_{ij}}{x_j^{min}}$$
    
- **Untuk kriteria cost:**  
    $$r_{ij} = \frac{x_j^{min}}{x_{ij}}$$
    

---

### Langkah 4: Menghitung Nilai CPI

$$CPI_i = \sum_{j=1}^{m} (r_{ij} \times W_j)$$

---

### Langkah 5: Perangkingan Alternatif

- Alternatif dengan **nilai CPI terbesar** → peringkat tertinggi
    

---

## 6. Contoh Kasus Sederhana

### Kasus:

Pemilihan vendor IT berdasarkan 3 kriteria:

| Kriteria | Jenis   | Bobot |
| -------- | ------- | ----- |
| Biaya    | Cost    | 0,4   |
| Kualitas | Benefit | 0,35  |
| Layanan  | Benefit | 0,25  |

### Matriks Keputusan

| Alternatif | Biaya | Kualitas | Layanan |
| ---------- | ----- | -------- | ------- |
| A1         | 50    | 80       | 70      |
| A2         | 40    | 75       | 85      |
| A3         | 45    | 90       | 75      |

---

### Nilai Minimum

|Kriteria|Nilai Minimum|
|---|---|
|Biaya|40|
|Kualitas|75|
|Layanan|70|

---

### Normalisasi (contoh A1)

- Biaya (cost): (40/50 = 0,80)
    
- Kualitas (benefit): (80/75 = 1,07)
    
- Layanan (benefit): (70/70 = 1,00)
    

---

### Perhitungan CPI (contoh A1)

$$CPI_{A1} = (0,80 \times 0,4) + (1,07 \times 0,35) + (1,00 \times 0,25)$$

---

## 7. Interpretasi Hasil

- Nilai CPI **bersifat relatif**
    
- Perbandingan antar alternatif menjadi fokus utama
    
- Tidak menunjukkan nilai absolut, tetapi **tingkat kinerja relatif**
    

---

## 8. Kelebihan dan Keterbatasan Metode CPI

### 8.1 Kelebihan

- Mudah dipahami dan diimplementasikan
    
- Cocok untuk DSS berbasis spreadsheet
    
- Transparan dan sistematis
    
- Dapat menangani perbedaan satuan
    

### 8.2 Keterbatasan

- Sensitif terhadap nilai minimum ekstrem
    
- Tidak mempertimbangkan hubungan antar kriteria
    
- Penentuan bobot sangat subjektif
    

---

## 9. Perbandingan Singkat dengan Metode Lain

| Aspek        | CPI            | SAW         | WP               |
| ------------ | -------------- | ----------- | ---------------- |
| Normalisasi  | Minimum-based  | Max/Min     | Rasio            |
| Operasi      | Penjumlahan    | Penjumlahan | Perkalian        |
| Interpretasi | Indeks relatif | Skor akhir  | Nilai preferensi |
| Kompleksitas | Rendah         | Rendah      | Menengah         |

---

## 10. Aplikasi CPI dalam DSS

Metode CPI banyak digunakan dalam:

- Seleksi pemasok/vendor
    
- Penilaian kinerja karyawan
    
- Evaluasi proyek
    
- Penentuan prioritas investasi
    
- Sistem rekomendasi berbasis kriteria
    

---

## 11. Ringkasan

- CPI adalah metode MCDM berbasis indeks komposit
    
- Menggunakan nilai minimum sebagai acuan normalisasi
    
- Menghasilkan ranking alternatif secara objektif
    
- Cocok untuk DSS dengan kebutuhan perhitungan sederhana namun sistematis
    
