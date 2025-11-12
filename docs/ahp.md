# Analytical Hierarchy Process (AHP)

## 🎯 Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. Menjelaskan konsep dan prinsip dasar dari metode **Analytical Hierarchy Process (AHP)**.
    
2. Menyusun **struktur hierarki keputusan** yang terdiri dari tujuan, kriteria, subkriteria, dan alternatif.
    
3. Melakukan **pembobotan kriteria dan alternatif** menggunakan perbandingan berpasangan (pairwise comparison).
    
4. Menghitung **konsistensi penilaian (Consistency Ratio)** untuk memastikan validitas keputusan.
    
5. Menerapkan AHP dalam **kasus pengambilan keputusan multikriteria** (misalnya: pemilihan supplier, lokasi, karyawan, dsb).
    

---

## 🧭 **1. Pendahuluan**

Dalam dunia nyata, pengambil keputusan sering dihadapkan pada **banyak alternatif dan banyak kriteria**.  
Contohnya:

> “Bagaimana memilih vendor terbaik?”  
> “Bagaimana menentukan prioritas proyek?”  
> “Bagaimana menyeleksi calon karyawan terbaik?”

Masalah-masalah seperti itu disebut **Multicriteria Decision Making (MCDM)**, dan salah satu metode yang paling terkenal untuk menyelesaikannya adalah **Analytical Hierarchy Process (AHP)**.

---

## 🧠 **2. Konsep Dasar AHP**

### 🔹 Definisi:

**Analytical Hierarchy Process (AHP)** adalah metode pengambilan keputusan yang dikembangkan oleh **Thomas L. Saaty (1970-an)** untuk membantu pengambil keputusan dalam **memilih alternatif terbaik berdasarkan beberapa kriteria yang kompleks**.

Metode ini memungkinkan seseorang untuk:

- Menyusun **masalah yang kompleks menjadi struktur hierarki**.
    
- **Membandingkan kriteria dan alternatif secara berpasangan (pairwise)**.
    
- Memberikan bobot **berdasarkan persepsi subjektif namun logis.**
    

---

## 🧩 **3. Struktur Hierarki AHP**

AHP menyusun masalah keputusan ke dalam bentuk **hierarki bertingkat**, biasanya terdiri dari tiga atau lebih level:

```
Level 1 : Tujuan (Goal)
Level 2 : Kriteria (dan Subkriteria jika ada)
Level 3 : Alternatif Keputusan
```

Contoh:

> Tujuan: Memilih Supplier Terbaik  
> Kriteria: Harga, Kualitas, Waktu Pengiriman  
> Alternatif: Supplier A, Supplier B, Supplier C

**Diagram:**

```
           Tujuan
              │
 ┌────────────┼────────────┐
Harga     Kualitas     Pengiriman
 │            │            │
A, B, C    A, B, C       A, B, C
```

---

## ⚖️ **4. Prinsip Dasar AHP**

Menurut Saaty, ada **empat prinsip utama** dalam AHP:

1. **Decomposition (Pemecahan Masalah)**  
    → Memecah masalah kompleks menjadi struktur hierarki.
    
2. **Comparative Judgement (Perbandingan Berpasangan)**  
    → Membandingkan setiap elemen secara berpasangan berdasarkan tingkat kepentingannya.
    
3. **Synthesis of Priorities (Sintesis Prioritas)**  
    → Menghitung bobot atau prioritas relatif dari setiap elemen.
    
4. **Consistency (Konsistensi Logis)**  
    → Memastikan bahwa penilaian yang diberikan tidak bertentangan secara logis.
    

---

## 📊 **5. Skala Penilaian AHP (Saaty’s Scale)**

Perbandingan antar elemen dilakukan menggunakan skala **1–9**, seperti tabel berikut:

|Nilai|Keterangan|Makna|
|---|---|---|
|1|Sama penting|Kedua elemen sama penting|
|3|Sedikit lebih penting|Salah satu sedikit lebih penting|
|5|Lebih penting|Salah satu lebih penting secara nyata|
|7|Sangat penting|Salah satu jauh lebih penting|
|9|Mutlak penting|Salah satu sangat dominan|
|2,4,6,8|Nilai antara|Untuk kompromi antar dua nilai di atas|

Jika elemen A lebih penting daripada B dengan nilai 5, maka elemen B dibanding A akan bernilai **1/5**.

---

## 🧮 **6. Langkah-langkah Perhitungan AHP**

### **Langkah 1: Menyusun Hierarki Keputusan**

Tentukan:

- Tujuan utama
    
- Kriteria dan subkriteria
    
- Alternatif keputusan
    

---

### **Langkah 2: Menyusun Matriks Perbandingan Berpasangan**

Setiap kriteria dibandingkan **satu sama lain** menggunakan skala 1–9.

Contoh matriks perbandingan antar kriteria:

|Kriteria|Harga|Kualitas|Pengiriman|
|---|---|---|---|
|Harga|1|1/3|3|
|Kualitas|3|1|5|
|Pengiriman|1/3|1/5|1|

---

### **Langkah 3: Menormalisasi Matriks**

Setiap nilai dibagi dengan total kolomnya, lalu dihitung **rata-rata setiap baris** untuk mendapatkan **bobot (priority vector)**.

---

### **Langkah 4: Menghitung Rasio Konsistensi (Consistency Ratio / CR)**

Tujuan: memastikan bahwa perbandingan yang dibuat **tidak inkonsisten**.

Langkah:

1. Hitung **λmax** (nilai eigen terbesar)
    
2. Hitung **Consistency Index (CI)** = (λmax – n) / (n – 1)
    
3. Hitung **Consistency Ratio (CR)** = CI / RI
    
    - RI = Random Index (tabel standar tergantung n)
        

| n   | 1   | 2   | 3    | 4    | 5    | 6    | 7    | 8    | 9    |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| RI  | 0   | 0   | 0.58 | 0.90 | 1.12 | 1.24 | 1.32 | 1.41 | 1.45 |

**Kriteria Konsistensi:**

> Jika CR ≤ 0.1 → Konsisten  
> Jika CR > 0.1 → Penilaian harus diperbaiki

---

### **Langkah 5: Sintesis Global**

Kalikan bobot setiap kriteria dengan bobot alternatifnya di bawahnya untuk mendapatkan **skor total** setiap alternatif.

Contoh:

|Alternatif|Harga (0.3)|Kualitas (0.5)|Pengiriman (0.2)|Skor Total|
|---|---|---|---|---|
|Supplier A|0.6|0.3|0.5|0.45|
|Supplier B|0.3|0.5|0.3|0.40|
|Supplier C|0.1|0.2|0.2|0.15|

> Hasil: **Supplier A** memiliki skor tertinggi, sehingga menjadi alternatif terbaik.

---

## 🧩 **7. Kelebihan dan Kekurangan AHP**

### ✅ **Kelebihan:**

1. Dapat menangani **masalah kompleks dan multikriteria.**
    
2. Menggabungkan **penilaian kualitatif dan kuantitatif.**
    
3. Ada **uji konsistensi logis** untuk menilai validitas hasil.
    
4. Mudah diterapkan menggunakan Excel atau software DSS.
    

### ⚠️ **Kekurangan:**

1. Subjektif — sangat tergantung pada **penilaian manusia.**
    
2. **Sulit diterapkan** jika kriteria/alternatif terlalu banyak.
    
3. Hasil bisa **berubah** jika terjadi inkonsistensi penilaian.
    

---

## 🧰 **8. Penerapan AHP dalam DSS**

AHP banyak diintegrasikan dalam sistem pendukung keputusan untuk berbagai bidang:

|Bidang|Contoh Penerapan|
|---|---|
|Manajemen Proyek|Menentukan prioritas proyek pembangunan|
|Rekrutmen|Memilih kandidat terbaik berdasarkan kriteria|
|Rantai Pasok|Memilih supplier / vendor terbaik|
|Energi|Menentukan lokasi pembangkit listrik|
|Pendidikan|Evaluasi kinerja dosen atau program studi|

---

## 💻 **9. Software Pendukung AHP**

Beberapa tools yang dapat digunakan:
- **Expert Choice**    
- **Super Decisions**    
- **Microsoft Excel (manual & VBA)**    
- **Python (NumPy, AHPy Library)**    
- **Web-based DSS AHP Tools**    

---

## 🧾 **10. Ringkasan**

- **AHP** adalah metode pengambilan keputusan multikriteria berbasis perbandingan berpasangan.
    
- Melibatkan langkah: _hierarchy building → pairwise comparison → normalization → consistency test → synthesis_.
    
- Hasil akhir berupa **bobot prioritas** setiap alternatif.
    
- Dapat diintegrasikan dengan DSS berbasis model maupun data.
    

---

## 📚 **Referensi**

- Saaty, T. L. (1980). _The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation._ McGraw-Hill.
    
- Turban, E., Aronson, J. E., & Liang, T.-P. (2014). _Decision Support Systems and Intelligent Systems._ Pearson.
    
- Vargas, L. G. (1990). _An overview of the analytic hierarchy process: Applications and progress since its inception._ European Journal of Operational Research.
    
