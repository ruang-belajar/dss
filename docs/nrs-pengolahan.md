# Pengolahan Kuisioner Numerical Rating Scale (NRS)

## 🎯 1. Pengertian Skala Numerical Rating Scale (NRS)

**Numerical Rating Scale (NRS)** adalah skala penilaian di mana responden diminta memberikan **nilai numerik** pada suatu pernyataan atau variabel, biasanya dalam rentang **1 sampai 10** (kadang 0–5, tergantung rancangan).  
Contoh:

> “Seberapa puas Anda terhadap kinerja sistem informasi ini?”
> 
> (1) Sangat Tidak Puas — (10) Sangat Puas

---

## 🧮 2. Langkah-langkah Mengolah Data dari Skala NRS

### Langkah 1 — Koding dan Input Data

Masukkan hasil jawaban ke dalam tabel data (Excel/SPSS) dalam bentuk angka sesuai pilihan responden.  
Contoh tabel:

|Responden|Kinerja|Kecepatan|Keamanan|Kemudahan|
|---|---|---|---|---|
|R1|8|7|9|8|
|R2|6|8|7|6|
|R3|9|9|10|9|

---

### Langkah 2 — Hitung Statistik Deskriptif

Gunakan ukuran statistik untuk menganalisis data:

|Ukuran|Rumus|Kegunaan|
|---|---|---|
|**Mean (rata-rata)**|Σx / n|Mengukur kecenderungan umum jawaban|
|**Median**|Nilai tengah dari data|Menunjukkan posisi tengah|
|**Modus**|Nilai yang paling sering muncul|Menunjukkan preferensi mayoritas|
|**Standar deviasi (SD)**|√(Σ(x−mean)²/n)|Menunjukkan variasi jawaban|

> 🔹 Tools: Excel (`=AVERAGE()`, `=STDEV()`, `=MODE()`), SPSS, atau Python.

---

### Langkah 3 — Kategorisasi Nilai (Opsional)

Untuk interpretasi yang lebih mudah dalam DSS, ubah hasil numerik ke dalam kategori kualitatif, misalnya:

|Rentang Nilai|Kategori|
|---|---|
|1 – 2.99|Sangat Buruk|
|3 – 4.99|Buruk|
|5 – 6.99|Cukup|
|7 – 8.99|Baik|
|9 – 10|Sangat Baik|

---

### Langkah 4 — Analisis Agregat

Hitung **nilai rata-rata per variabel** dan **total skor indeks**:

Contoh perhitungan:  
$Indeks = \frac{Σ \text{skor rata-rata semua indikator}}{\text{jumlah indikator}}$

Jika hasilnya, misal:

- Kinerja: 7.6
    
- Kecepatan: 8.0
    
- Keamanan: 8.7
    
- Kemudahan: 7.9
    

Maka sistem bisa disimpulkan **“Baik”** berdasarkan kategori di atas.

---

### Langkah 5 — Visualisasi (DSS Output)

Tampilkan hasil ke dalam bentuk:

- Diagram batang (nilai tiap indikator)
    
- Diagram radar (perbandingan antar aspek)
    
- Indeks total dalam dashboard DSS
    

Contoh grafik radar: menunjukkan kekuatan dan kelemahan relatif antar aspek sistem.

---

## 💡 Contoh Interpretasi

> Berdasarkan hasil rata-rata keseluruhan sebesar **8.05**, maka tingkat kepuasan pengguna terhadap sistem informasi berada pada kategori **“Baik”**.
> 
> Aspek yang paling kuat: **Keamanan (8.7)**  
> Aspek yang perlu ditingkatkan: **Kinerja (7.6)**

---

## 🧠 Relevansi dengan Decision Support System

Dalam DSS, hasil olahan dari skala numerical rating digunakan untuk:

- Menyediakan **indikator performa sistem**
    
- Membantu manajer dalam **pengambilan keputusan perbaikan**
    
- Menjadi **input kuantitatif** untuk metode analisis lanjutan (misal AHP, SAW, TOPSIS, dll)
    
---

## 💼 Diskusi & Tugas

Berikut adalah contoh hasil pengisian survei _Kepuasan Pengguna Sistem Informasi Akademik_. 

|No|Pernyataan|R1|R2|R3|R4|R5|
|---|---|---|---|---|---|---|
|1|Tampilan sistem mudah dipahami|8|7|9|8|9|
|2|Kecepatan akses sistem memadai|7|8|8|6|9|
|3|Fitur sistem sesuai kebutuhan pengguna|9|7|8|9|8|
|4|Sistem jarang mengalami gangguan/error|6|7|7|8|7|
|5|Keamanan data pengguna terjamin|9|8|10|9|9|


🙋‍♂️ Buat analisa dan interpretasi terhadap hasil survei