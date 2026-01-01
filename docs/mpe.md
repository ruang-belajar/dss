# **Metode Perbandingan Eksponensial (MPE)**

## **1. Pendahuluan**

*Exponential Comparison Method*/Metode Perbandingan Eksponensial (MPE) adalah salah satu metode pengambilan keputusan multikriteria yang digunakan untuk menilai dan meranking alternatif berdasarkan sejumlah kriteria. Metode ini dikembangkan sebagai alternatif yang lebih sederhana dari Analytic Hierarchy Process (AHP), tetapi tetap mempertimbangkan bobot kepentingan secara proporsional dan non-linear.

MPE banyak digunakan dalam DSS karena:
- Mudah diterapkan,    
- Tidak memerlukan matriks perbandingan berpasangan seperti AHP,    
- Menghasilkan peringkat alternatif secara cepat dan konsisten,    
- Cocok ketika banyak kriteria dengan skala penilaian relatif.    

---

## **2. Konsep Dasar**

Metode MPE menyatakan bahwa **nilai suatu alternatif** ditentukan oleh:

$$V(a) = \sum_{i=1}^{n} w_i^{e_i}$$

Keterangan:

- $V(a)$ = nilai total alternatif
    
- $w_i$ = bobot preferensi alternatif terhadap kriteria ke-i (hasil normalisasi)
    
- $e_i$ = nilai eksponen (tingkat kepentingan kriteria ke-i)
    
- $n$ = jumlah kriteria
    

**Inti metode:**  
Kriteria yang lebih penting diberi **nilai eksponen lebih tinggi**, sehingga perbedaan antar alternatif menjadi lebih signifikan.

---

## **3. Langkah-langkah Perhitungan MPE**

### **Langkah 1 — Menentukan Kriteria**

Identifikasi semua kriteria yang digunakan untuk menilai alternatif.

Contoh:

- K1: Harga
    
- K2: Kualitas
    
- K3: Fitur
    

---

### **Langkah 2 — Menentukan Eksponen (Tingkat Kepentingan) Tiap Kriteria**

Eksponen menggambarkan tingkat kepentingan (importance power).  
Semakin penting, semakin besar eksponennya.

Contoh skala eksponen umum:

|Tingkat Kepentingan|Eksponen|
|---|---|
|Sangat rendah|1|
|Rendah|2|
|Sedang|3|
|Tinggi|4|
|Sangat tinggi|5|

---

### **Langkah 3 — Memberikan nilai alternatif terhadap tiap kriteria**

Penilaian bisa berupa:

- skala 1–10
    
- rating kualitatif dikonversi ke angka
    
- data kuantitatif yang dinormalisasi
    

---

### **Langkah 4 — Melakukan normalisasi**

Normalisasi memastikan nilai berada pada rentang 0–1.

Untuk _benefit criteria_:

$$w_i = \frac{x_i}{\max(x)}$$

Untuk _cost criteria_:

$$w_i = \frac{\min(x)}{x_i}$$

---

### **Langkah 5 — Menghitung nilai eksponensial**

Untuk tiap nilai normalisasi:

$$w_i^{e_i}$$
---

### **Langkah 6 — Menghitung nilai total alternatif**

$$V(a) = \sum w_i^{e_i}$$

Alternatif dengan nilai terbesar → **ranking terbaik**.

---

## **4. Contoh Kasus Lengkap**

### **Kasus: Pemilihan Laptop untuk Pegawai IT**

Kriteria:

- K1: Harga (cost) → e = 3
    
- K2: Performa (benefit) → e = 5
    
- K3: Daya tahan baterai (benefit) → e = 4

Alternatif: A1, A2, A3.

### **Data awal**

|Alternatif|Harga (juta)|Performa (1–10)|Baterai (jam)|
|---|---|---|---|
|A1|12|9|8|
|A2|10|7|6|
|A3|14|10|9|

---

### **Langkah Normalisasi**

**K1: Harga (cost)**  
Min = 10

|Alt|w1 = min/x|
|---|---|
|A1|10/12 = 0.833|
|A2|10/10 = 1|
|A3|10/14 = 0.714|

---

**K2: Performa (benefit)**  
Max = 10

|Alt|w2 = x/max|
|---|---|
|A1|9/10 = 0.9|
|A2|7/10 = 0.7|
|A3|10/10 = 1|

---

**K3: Baterai (benefit)**  
Max = 9

|Alt|w3 = x/max|
|---|---|
|A1|8/9 = 0.889|
|A2|6/9 = 0.667|
|A3|9/9 = 1|

---

### **Penghitungan Eksponensial**

Eksponen:

- e1 = 3
    
- e2 = 5
    
- e3 = 4
    

Hitung $w^e$ untuk semua alternatif:

#### **A1**

- $w_1^3 = 0.833^3 = 0.578$
    
- $w_2^5 = 0.9^5 = 0.590$
    
- $w_3^4 = 0.889^4 = 0.625$
    

Total:  

$$V(A1) = 0.578 + 0.590 + 0.625 = 1.793$$

---

#### **A2**

- $w_1^3 = 1^3 = 1$

- $w_2^5 = 0.7^5 = 0.168$

- $w_3^4 = 0.667^4 = 0.198$

Total:  
$$
V(A2) = 1 + 0.168 + 0.198 = 1.366  
$$

---

#### **A3**

- $w_1^3 = 0.714^3 = 0.364$
    
- $w_2^5 = 1^5 = 1$
    
- $w_3^4 = 1^4 = 1$

Total:  

$$
V(A3) = 0.364 + 1 + 1 = 2.364  
$$

---

### **Hasil Akhir (Ranking)**

|Ranking|Alternatif|Nilai|
|---|---|---|
|1|**A3**|2.364|
|2|A1|1.793|
|3|A2|1.366|

**Keputusan:** Alternatif terbaik adalah **A3**.

---

## **5. Keunggulan MPE**

- Perhitungan lebih cepat dan lebih sederhana daripada AHP.
    
- Eksponen memungkinkan sensitivitas keputusan yang lebih fleksibel.
    
- Cocok untuk banyak kriteria.
    
- Mudah diterapkan pada Excel.
    

---

## **6. Kelemahan MPE**

- Eksponen cenderung subjektif → perlu justifikasi kuat.
    
- Tidak menyediakan pengujian konsistensi seperti AHP.
    
- Tidak selalu cocok untuk keputusan yang sangat kompleks dan hierarkis.
    

---

## **7. Penerapan MPE dalam DSS**

MPE sering dipakai dalam masalah:
- Seleksi vendor    
- Pemilihan karyawan    
- Penentuan prioritas proyek    
- Seleksi lokasi    
- Pemilihan produk terbaik    
- Evaluasi risiko (ketika banyak parameter)
    
---

## Perbandingan SAW vs MPE

Jika Anda bandingkan, cara perhitungan MPE sangat mirip dengan perhitungan dalam SAW. Perbedaan utamanya adalah pada proses normalisasi. Hal ini menyebabkan hasil akhir bisa sangat sensitif terhadap perubahan kecil pada data.

Berikut tabel tabel perbandingan SAW vs MPE

| Aspek       | SAW                                                                  | MPE                                                                                       |
| ----------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Definisi    | Metode penjumlahan terbobot untuk memperoleh nilai total alternatif. | Metode pengambilan keputusan dengan penilaian eksponensial berdasarkan bobot kepentingan. |
| Prinsip     | Linear additive model.                                               | Non-linear weighted exponential model.                                                    |
| Sifat hasil | Linear dan stabil                                                    | Non-linear, bisa lebih ekstrem                                                            |
| Rumus       | $V(a) = \sum w_i \cdot r_{i}$                                        | $V(a) = \sum w_i^{e_i}$                                                                   |
| Cocok untuk | Sistem yang bobotnya stabil dan objektif.                            | Sistem yang butuh diferensiasi kuat antar kriteria.                                       |

### Kapan Menggunakan SAW vs MPE?

Gunakan SAW jika:
- Kriteria memiliki tingkat kepentingan yang tidak terlalu jauh.    
- Anda ingin hasil yang stabil dan tidak ekstrem.    
- Sistem memerlukan perhitungan cepat dan mudah dijelaskan.    
- Proses pengambilan keputusan memerlukan transparansi tinggi.
    
Gunakan MPE jika:
- Ada kriteria yang _sangat dominan_ dan harus lebih menonjol.    
- Perbedaan antar alternatif terlalu kecil secara linear.    
- Diperlukan pembobotan menggunakan sensitivitas tinggi.    
- Pengambil keputusan ingin kontrol lebih besar melalui eksponen.

---
## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [Rumus MPE](https://docs.google.com/spreadsheets/d/17uaxCKO9OyAoJ-MIPbN6kfUn3anaqCA8RxrNubIgsug/edit?usp=sharing)

Modifikasi sheet sesuai kebutuhan