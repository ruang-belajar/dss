# Simple Additive Weighting (SAW)

## **1. Pendahuluan**

### **1.1 Latar Belakang**

Dalam sistem pendukung keputusan (DSS), seringkali diperlukan suatu metode untuk membantu pengambil keputusan dalam memilih alternatif terbaik dari beberapa pilihan yang tersedia. Salah satu metode yang paling sederhana dan populer adalah **Simple Additive Weighting (SAW)**.  
Metode ini sering disebut juga sebagai **metode penjumlahan terbobot**, karena prinsip utamanya adalah menjumlahkan nilai-nilai dari setiap kriteria yang telah diberi bobot sesuai tingkat kepentingannya.

---

## **2. Konsep Dasar SAW**

### **2.1 Pengertian**

**Simple Additive Weighting (SAW)** adalah metode penilaian multi-kriteria di mana setiap alternatif dievaluasi berdasarkan sejumlah kriteria yang memiliki bobot tertentu. Nilai total dari tiap alternatif diperoleh dengan menjumlahkan hasil perkalian antara nilai kriteria yang telah dinormalisasi dengan bobotnya.

Metode ini digunakan untuk menemukan alternatif terbaik dengan **nilai total tertinggi**.

### **2.2 Karakteristik SAW**

- Mudah dipahami dan diimplementasikan.
    
- Menggunakan **konsep normalisasi** agar semua kriteria berada dalam skala yang sama.
    
- Cocok digunakan untuk **pengambilan keputusan multi-kriteria (MCDM)**.
    
- Dapat menangani **kriteria keuntungan (benefit)** maupun **kriteria biaya (cost)**.
    

---

## **3. Langkah-Langkah Metode SAW**

Langkah-langkah umum dalam penerapan metode SAW adalah sebagai berikut:

### **Langkah 1. Menentukan Kriteria dan Alternatif**

- Tentukan daftar **alternatif (A₁, A₂, A₃, ...)**.
    
- Tentukan daftar **kriteria (C₁, C₂, C₃, ...)** beserta jenisnya (benefit atau cost).
    
- Tentukan **bobot (W)** untuk setiap kriteria berdasarkan tingkat kepentingan.
    

Contoh:

|Kriteria|Bobot (W)|Jenis|
|---|---|---|
|C₁: Harga|0.3|Cost|
|C₂: Kualitas|0.4|Benefit|
|C₃: Daya Tahan|0.3|Benefit|

---

### **Langkah 2. Menyusun Matriks Keputusan (X)**

Susun tabel berisi nilai-nilai alternatif terhadap setiap kriteria.

Contoh:

|Alternatif|C₁|C₂|C₃|
|---|---|---|---|
|A₁|5|70|80|
|A₂|4|80|70|
|A₃|3|60|90|

---

### **Langkah 3. Normalisasi Matriks Keputusan**

Normalisasi dilakukan agar semua nilai berada dalam skala yang sama (0–1).

Rumus normalisasi:

- Untuk **kriteria benefit (semakin besar semakin baik)**:  
    [  
    r_{ij} = \frac{x_{ij}}{\max(x_j)}  
    ]
    
- Untuk **kriteria cost (semakin kecil semakin baik)**:  
    [  
    r_{ij} = \frac{\min(x_j)}{x_{ij}}  
    ]
    

Contoh hasil normalisasi (asumsi C₁ = cost, C₂ & C₃ = benefit):

|Alternatif|C₁|C₂|C₃|
|---|---|---|---|
|A₁|3/5 = 0.6|70/80 = 0.875|80/90 = 0.888|
|A₂|3/4 = 0.75|80/80 = 1.000|70/90 = 0.778|
|A₃|3/3 = 1.000|60/80 = 0.75|90/90 = 1.000|

---

### **Langkah 4. Menghitung Nilai Preferensi (V)**

Setelah normalisasi, nilai total untuk setiap alternatif dihitung dengan:  
[  
V_i = \sum_{j=1}^{n} (w_j \times r_{ij})  
]

Contoh perhitungan:

|Alternatif|Perhitungan|Nilai Akhir (Vᵢ)|
|---|---|---|
|A₁|(0.3×0.6) + (0.4×0.875) + (0.3×0.888)|0.792|
|A₂|(0.3×0.75) + (0.4×1.000) + (0.3×0.778)|0.863|
|A₃|(0.3×1.000) + (0.4×0.75) + (0.3×1.000)|0.925|

---

### **Langkah 5. Menentukan Alternatif Terbaik**

Alternatif dengan **nilai total tertinggi (Vᵢ terbesar)** adalah alternatif terbaik.  
→ Dalam contoh di atas, **A₃** merupakan pilihan terbaik karena memiliki nilai 0.925.

---

## **4. Kelebihan dan Kelemahan SAW**

|**Kelebihan**|**Kelemahan**|
|---|---|
|Mudah dipahami dan digunakan|Tidak mempertimbangkan interaksi antar kriteria|
|Perhitungannya cepat dan sederhana|Rentan terhadap skala penilaian yang tidak konsisten|
|Cocok untuk kasus dengan banyak alternatif|Mengasumsikan hubungan linear antara nilai dan bobot|
|Dapat diterapkan di berbagai bidang|Sensitif terhadap perubahan bobot|

---

## **5. Contoh Kasus Nyata**

### **Kasus: Pemilihan Smartphone Terbaik**

Kriteria:

- C₁: Harga (Cost)
    
- C₂: Kamera (Benefit)
    
- C₃: Baterai (Benefit)
    
- Bobot: [0.3, 0.4, 0.3]
    

Langkah-langkah perhitungan dilakukan seperti di atas untuk menentukan smartphone terbaik berdasarkan data penilaian.

---

## **6. Implementasi dalam DSS**

Metode SAW sering diintegrasikan dalam sistem pendukung keputusan berbasis komputer seperti:

- Sistem pemilihan karyawan terbaik
    
- Sistem rekomendasi produk
    
- Sistem seleksi beasiswa
    
- Sistem penentuan lokasi usaha
    

Biasanya, DSS berbasis SAW dibangun menggunakan **basis data + bahasa pemrograman (PHP, Python, Java)** dan menghasilkan laporan keputusan otomatis.

---

## **7. Kesimpulan**

- **SAW** adalah metode MCDM sederhana namun efektif untuk pengambilan keputusan berbasis kriteria ganda.
    
- Proses utamanya adalah **normalisasi → pembobotan → penjumlahan terbobot**.
    
- Alternatif terbaik adalah yang memiliki nilai **V tertinggi**.
    
- Meskipun sederhana, metode ini sangat bermanfaat untuk aplikasi praktis DSS di berbagai bidang.
    

---

## **8. Tugas Mahasiswa**

1. Buat studi kasus penerapan metode SAW untuk masalah pengambilan keputusan (misalnya pemilihan supplier, kendaraan, atau pegawai terbaik).
    
2. Implementasikan perhitungan SAW menggunakan **Excel atau Python**.
    
3. Analisis hasil dan berikan kesimpulan.
    

---

Apakah Anda ingin saya bantu buatkan **versi PowerPoint (slide kuliah)** dari materi ini juga (dengan visual tabel, rumus, dan contoh kasus)?