
# Skala dan Pengukuran dalam Konteks Decision Support System (DSS)

---

## 🎯 Tujuan Pembelajaran

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. Menjelaskan konsep dasar **pengukuran (measurement)** dan **skala pengukuran (measurement scale)** dalam konteks DSS.
    
2. Mengidentifikasi empat jenis skala pengukuran (nominal, ordinal, interval, rasio).
    
3. Memahami bagaimana pemilihan skala memengaruhi proses analisis dan pengambilan keputusan dalam DSS.
    
4. Memberikan contoh penerapan skala dan pengukuran dalam sistem pendukung keputusan nyata.
    

---

## 🧭 1. Pengantar: Peran Pengukuran dalam DSS

Dalam **Decision Support System (DSS)**, setiap keputusan didasarkan pada **data dan informasi** yang harus dapat diukur, dibandingkan, dan dianalisis.  
Oleh karena itu, **pengukuran dan skala** menjadi elemen penting untuk memastikan:

- Data dapat **diinterpretasikan dengan benar**.
    
- Hasil analisis **relevan dengan konteks keputusan**.
    
- Sistem dapat **mengurutkan, menghitung, dan membandingkan alternatif keputusan** secara logis.
    

### 🔹 Definisi:

- **Pengukuran (Measurement)** adalah proses memberikan **angka atau simbol** pada objek, atribut, atau fenomena sesuai dengan aturan tertentu.
    
- **Skala (Scale)** adalah sistem atau tingkat **kuantifikasi** yang menunjukkan **sejauh mana data dapat dibandingkan dan dioperasikan secara matematis.**
    

Contoh:

> Dalam DSS yang menilai kinerja karyawan, skor penilaian 1–5 adalah hasil pengukuran dengan skala tertentu (ordinal atau interval, tergantung konteks).

---

## ⚖️ 2. Pentingnya Skala dan Pengukuran dalam DSS

Dalam DSS, pengukuran digunakan untuk:

1. **Menilai alternatif keputusan** berdasarkan kriteria tertentu (misalnya, biaya, kualitas, waktu).
    
2. **Mengubah data kualitatif menjadi kuantitatif** agar dapat diolah sistem.
    
3. **Mendukung metode pengambilan keputusan multikriteria** seperti:
    
    - Simple Additive Weighting (SAW)
        
    - Analytic Hierarchy Process (AHP)
        
    - TOPSIS
        
    - Weighted Product (WP)
        

Tanpa skala pengukuran yang jelas, sistem DSS dapat memberikan **hasil analisis yang bias atau tidak valid**.

---

## 🔢 3. Jenis-Jenis Skala Pengukuran

Secara umum, terdapat **empat skala pengukuran utama** yang sering digunakan dalam DSS, sebagaimana dikemukakan oleh _Stevens (1946)_.

---

### 🟩 3.1 Skala Nominal

#### 🔹 Definisi:

Skala yang hanya **membedakan kategori atau kelompok** tanpa menunjukkan urutan atau besar kecilnya nilai.  
Data hanya menunjukkan **identitas atau klasifikasi.**

#### 🔹 Ciri:

- Tidak ada hubungan “lebih besar” atau “lebih kecil”.
    
- Tidak dapat dilakukan operasi matematika selain menghitung frekuensi.
    

#### 🔹 Contoh dalam DSS:

|Kode|Jenis Keluhan|Keterangan|
|---|---|---|
|1|Kualitas produk|Nominal|
|2|Harga mahal|Nominal|
|3|Layanan lambat|Nominal|

Dalam DSS, skala ini digunakan untuk **pengelompokan data kategori** seperti jenis produk, departemen, atau wilayah.

---

### 🟨 3.2 Skala Ordinal

#### 🔹 Definisi:

Skala yang menunjukkan **urutan (ranking)** antar data, tetapi **jarak antar peringkat tidak diketahui secara pasti.**

#### 🔹 Ciri:

- Dapat membandingkan urutan (“lebih tinggi”, “lebih rendah”).
    
- Tidak bisa menjelaskan seberapa besar perbedaannya.
    

#### 🔹 Contoh dalam DSS:

Penilaian kepuasan pelanggan:

|Peringkat|Keterangan|
|---|---|
|1|Sangat tidak puas|
|2|Tidak puas|
|3|Netral|
|4|Puas|
|5|Sangat puas|

Dalam DSS, skala ordinal sering digunakan untuk **survei persepsi**, **preferensi pengguna**, atau **rating alternatif keputusan.**

---

### 🟦 3.3 Skala Interval

#### 🔹 Definisi:

Skala yang menunjukkan **urutan dan jarak antar nilai yang sama besar**, tetapi **tidak memiliki nol absolut (nol bukan berarti ketiadaan).**

#### 🔹 Ciri:

- Dapat dilakukan operasi matematika (penjumlahan, pengurangan).
    
- Tidak bisa menghitung perbandingan rasio (karena nol relatif).
    

#### 🔹 Contoh dalam DSS:

Suhu ruangan: 30°C, 20°C, dan 10°C.  
Kita bisa tahu perbedaan suhu 10°C, tapi tidak bisa mengatakan “30°C dua kali lebih panas dari 15°C”.

Dalam DSS, skala ini digunakan untuk **data psikometrik, indeks kinerja, atau skor penilaian karyawan.**

---

### 🟥 3.4 Skala Rasio

#### 🔹 Definisi:

Skala tertinggi yang memiliki **sifat urutan, jarak yang sama, dan nol absolut (nol = ketiadaan nilai).**

#### 🔹 Ciri:

- Semua operasi matematika (tambah, kurang, kali, bagi) valid.
    
- Dapat digunakan untuk analisis statistik penuh.
    

#### 🔹 Contoh dalam DSS:

|Alternatif|Biaya (juta rupiah)|Waktu (jam)|
|---|---|---|
|A|10|5|
|B|20|10|

Dalam DSS, skala rasio sering digunakan untuk **data kuantitatif riil** seperti biaya, waktu, volume produksi, atau laba.

---
## 4. Hubungan Skala dengan Proses Analisis DSS

Jenis skala pengukuran menentukan **metode analisis dan model DSS** yang dapat digunakan:

|Jenis Skala|Analisis yang Cocok|Contoh Metode DSS|
|---|---|---|
|**Nominal**|Frekuensi, klasifikasi|Clustering, Decision Tree|
|**Ordinal**|Ranking, median|AHP, SAW|
|**Interval**|Korelasi, regresi|Forecasting, Trend Analysis|
|**Rasio**|Operasi aritmatika, optimisasi|Linear Programming, Cost-Benefit Analysis|

---

## 💡 5. Contoh Kasus Penerapan

**Kasus:** Sebuah perusahaan ingin memilih vendor terbaik untuk proyek TI.  
Kriteria yang digunakan:

- Harga (Rp juta) → Skala Rasio
    
- Reputasi vendor (peringkat 1–5) → Skala Ordinal
    
- Keandalan sistem (skor 0–100) → Skala Interval
    
- Jenis vendor (lokal/internasional) → Skala Nominal
    

Dalam DSS, data dari berbagai skala ini harus **dinormalisasi terlebih dahulu** agar dapat dibandingkan secara adil, misalnya menggunakan **metode SAW atau AHP**.

---

## 6. Tantangan dan Pentingnya Pemahaman Skala

1. **Kesalahan klasifikasi skala** → dapat menyebabkan hasil analisis yang salah.
    
2. **Konsistensi antar pengguna DSS** → penting agar interpretasi data sama.
    
3. **Konversi skala** → perlu hati-hati saat mengubah data kualitatif ke kuantitatif.
    
4. **Pemilihan metode analisis** → harus disesuaikan dengan jenis skala agar hasil valid.
    


---

## 📚 Referensi
- Stevens, S. S. (1946). _On the Theory of Scales of Measurement._ Science, 103(2684), 677–680.    
- Turban, E., Aronson, J. E., & Liang, T.-P. (2014). _Decision Support Systems and Intelligent Systems._ Pearson.    
- Power, D. J. (2011). _Decision Support, Analytics, and Business Intelligence._
    
