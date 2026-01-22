# Menggunakan AHP untuk Menentukan Bobot

Metode SAW, CPI, MOORA, WP, ... memerlukan nilai bobot untuk melakukan perhitungan. Menentukan bobot yang tepat tentu adalah hal krusial untuk bisa mendapatkan hasil perhitungan yang ideal. AHP adalah salah satu metode yang cukup umum untuk menentukan nilai bobot. Ada beberapa kondisi kapan kita bisa menggunakan AHP untuk menentukan bobot.

## 1. Ketika Bobot **Tidak Diketahui Secara Objektif**

Gunakan AHP jika:
- Tidak ada data historis atau rumus baku
- Bobot **bergantung pada preferensi dan pertimbangan pakar**

Contoh:
- Penentuan bobot kriteria seleksi dosen
- Penilaian risiko strategis
- Evaluasi kebijakan publik

## 2. Ketika Masalah Bersifat **Kompleks dan Hierarkis**

AHP sangat sesuai bila:
- Kriteria dapat diuraikan menjadi **subkriteria**
- Tingkat kepentingan **berbeda di setiap level**

Contoh:
- Pemilihan vendor (biaya → implementasi, operasional)
- Penilaian kinerja organisasi

## 3. Ketika Penilaian Bersifat Subjektif tetapi Harus Terukur

Gunakan AHP jika:
- Keputusan melibatkan opini, persepsi, dan pengalaman
- Subjektivitas **harus diubah menjadi angka yang rasional**

AHP menyediakan mekanisme formal untuk itu.

## 4. Ketika Konsistensi Penilaian Perlu Diuji

AHP tepat digunakan bila:
- Penilaian berasal dari manusia
- Diperlukan **validasi logika penilaian (CR ≤ 0,10)**

Metode lain **tidak memiliki uji konsistensi**.

---

## 5. Ketika Bobot Sangat Mempengaruhi Hasil Akhir

Gunakan AHP jika:
- Perubahan kecil bobot → perubahan signifikan hasil
- Keputusan bersifat **strategis atau berdampak besar**

Contoh:
- Investasi
- Pengadaan skala besar
- Penentuan prioritas proyek

---

## 6. Ketika DSS Membutuhkan **Justifikasi Akademik atau Formal**

AHP sering dipilih karena:
- Metodologi mapan
- Mudah dipertanggungjawabkan secara ilmiah
- Umum digunakan dalam penelitian dan audit keputusan

---

# KAPAN TIDAK PERLU MENGGUNAKAN AHP?

❌ **Tidak perlu AHP jika**:
- Bobot sudah ditentukan secara regulasi
- Data bersifat objektif dan kuantitatif murni
- Masalah sangat sederhana dan operasional
- Dibutuhkan keputusan **sangat cepat**

Alternatif:
- Bobot langsung
- Entropy
- Equal weighting

---

## PRAKTIK UMUM DALAM DSS

> **AHP digunakan untuk menentukan bobot, lalu metode lain digunakan untuk perangkingan.**

Contoh:
- **AHP → TOPSIS**
- **AHP → CPI**
- **AHP → SAW**
    

---

# CONTOH KASUS

## Contoh Kasus 1

Sebuah tim ingin menentukan **bobot kriteria** untuk pemilihan sistem (apa pun jenisnya).

**Kriteria:**
1. **Biaya (C1)**
2. **Kualitas (C2)**
3. **Risiko (C3)**

Tujuan: **Menentukan bobot masing-masing kriteria menggunakan AHP**

---

### LANGKAH 1 — Matriks Perbandingan Berpasangan

Berdasarkan penilaian pakar:
- Kualitas lebih penting dari Biaya → nilai 3
- Biaya lebih penting dari Risiko → nilai 2
- Kualitas jauh lebih penting dari Risiko → nilai 5

### Matriks Perbandingan

|Kriteria|Biaya (C1)|Kualitas (C2)|Risiko (C3)|
|---|---|---|---|
|**Biaya (C1)**|1|1/3|2|
|**Kualitas (C2)**|3|1|5|
|**Risiko (C3)**|1/2|1/5|1|

---

### LANGKAH 2 — Menjumlahkan Setiap Kolom

|Kolom|Jumlah|
|---|---|
|Biaya|4.50|
|Kualitas|1.53|
|Risiko|8.00|

---

### LANGKAH 3 — Normalisasi Matriks

Setiap elemen dibagi dengan total kolomnya.

|Kriteria|Biaya|Kualitas|Risiko|
|---|---|---|---|
|**Biaya**|0.22|0.22|0.25|
|**Kualitas**|0.67|0.65|0.63|
|**Risiko**|0.11|0.13|0.12|

---

### LANGKAH 4 — Menghitung Bobot (Vektor Prioritas)

Bobot = rata-rata setiap baris

|Kriteria|Bobot|
|---|---|
|**Biaya (C1)**|**0.23**|
|**Kualitas (C2)**|**0.65**|
|**Risiko (C3)**|**0.12**|
|**Total**|**1.00**|

➡️ **Interpretasi**:  
Kualitas adalah kriteria paling dominan (65%).

---

### LANGKAH 5 — Uji Konsistensi

#### 5.1 Hitung λmax

Kalikan matriks awal dengan bobot:

|Kriteria|Nilai|
|---|---|
|Biaya|0.69 / 0.23 = 3.02|
|Kualitas|1.98 / 0.65 = 3.05|
|Risiko|0.37 / 0.12 = 3.08|

$$λ_{max} = \frac{3.02 + 3.05 + 3.08}{3} = 3.05$$

---

#### 5.2 Consistency Index (CI)

$$CI = \frac{λ_{max} - n}{n - 1}  
= \frac{3.05 - 3}{2}  
= 0.025$$

---

#### 5.3 Consistency Ratio (CR)

Untuk n = 3 → **RI = 0.58**

$$CR = \frac{0.025}{0.58} = 0.043$$

✅ **CR < 0.10 → Konsisten**

---

### HASIL AKHIR

Bobot kriteria hasil AHP:
- **Kualitas** = 0.65
- **Biaya** = 0.23
- **Risiko** = 0.12

Bobot ini **valid dan siap digunakan** dalam metode lain seperti:
- SAW
- TOPSIS
- MOORA
- CPI
- ARAS

---

### RINGKASAN UNTUK MAHASISWA

1. Bandingkan kriteria dua-dua
2. Normalisasi matriks
3. Hitung rata-rata baris → bobot
4. Uji konsistensi (CR)
5. Gunakan bobot untuk DSS
    
---

## Contoh Kasus 2 (Dengan Kriteria dan Subkriteria)

**Studi Kasus**: Pemilihan **Vendor ERP Terbaik**

### 1. Struktur Hierarki Keputusan

**Level 1 – Tujuan**  
Menentukan vendor ERP terbaik

**Level 2 – Kriteria**

- C1: Biaya
    
- C2: Kualitas Sistem
    
- C3: Layanan Purna Jual
    

**Level 3 – Subkriteria**

- C1:
    
    - SC11: Biaya Implementasi
        
    - SC12: Biaya Pemeliharaan
        
- C2:
    
    - SC21: Keandalan Sistem
        
    - SC22: Kemudahan Penggunaan
        
- C3:
    
    - SC31: Responsivitas Support
        
    - SC32: Training & Dokumentasi
        

---

### 2. Perhitungan Bobot Kriteria Utama

#### 2.1 Matriks Perbandingan Berpasangan (Kriteria)

|Kriteria|Biaya|Kualitas|Layanan|
|---|---|---|---|
|Biaya|1|1/3|1/2|
|Kualitas|3|1|2|
|Layanan|2|1/2|1|

---

#### 2.2 Normalisasi Matriks

Jumlah kolom:

- Biaya = 6
    
- Kualitas = 1.83
    
- Layanan = 3.5
    

Normalisasi:

|Kriteria|Biaya|Kualitas|Layanan|Rata-rata|
|---|---|---|---|---|
|Biaya|0.167|0.182|0.143|**0.164**|
|Kualitas|0.500|0.546|0.571|**0.539**|
|Layanan|0.333|0.273|0.286|**0.297**|

**Bobot Kriteria Utama**

- Biaya = **0.164**
    
- Kualitas Sistem = **0.539**
    
- Layanan = **0.297**
    

---

### 3. Perhitungan Bobot Subkriteria


#### 3.1 Subkriteria Biaya

|Biaya|Implementasi|Pemeliharaan|
|---|---|---|
|Implementasi|1|3|
|Pemeliharaan|1/3|1|

Bobot:

- Implementasi = **0.75**
    
- Pemeliharaan = **0.25**
    

---

#### 3.2 Subkriteria Kualitas Sistem

|Kualitas|Keandalan|Kemudahan|
|---|---|---|
|Keandalan|1|2|
|Kemudahan|1/2|1|

Bobot:

- Keandalan = **0.667**
    
- Kemudahan = **0.333**
    

---

#### 3.3 Subkriteria Layanan

|Layanan|Support|Training|
|---|---|---|
|Support|1|4|
|Training|1/4|1|

Bobot:

- Support = **0.80**
    
- Training = **0.20**
    

---

### 4. Bobot Global Subkriteria

Bobot Global = Bobot Kriteria × Bobot Subkriteria

|Subkriteria|Perhitungan|Bobot Global|
|---|---|---|
|Biaya Implementasi|0.164 × 0.75|**0.123**|
|Biaya Pemeliharaan|0.164 × 0.25|**0.041**|
|Keandalan Sistem|0.539 × 0.667|**0.359**|
|Kemudahan Penggunaan|0.539 × 0.333|**0.180**|
|Responsivitas Support|0.297 × 0.80|**0.238**|
|Training & Dokumentasi|0.297 × 0.20|**0.059**|

✔ Total bobot = **1.000**

---

### 5. Interpretasi Hasil

- Faktor **paling dominan**: _Keandalan Sistem_
    
- Faktor **paling kecil pengaruhnya**: _Biaya Pemeliharaan_
    
- Fokus keputusan **lebih condong ke kualitas dibanding biaya**
    

➡️ Bobot ini **siap digunakan** untuk:

- SAW
    
- TOPSIS
    
- MOORA
    
- CPI
    
- ARAS
    

---

### 6. Catatan Akademik Penting

- Konsistensi (CR) **diasumsikan valid** untuk tujuan pembelajaran
    
- Dalam penelitian formal, **CR harus dihitung dan ≤ 0,10**
    
