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

### Langkah 2: Menentukan Nilai Minimum Tiap Kriteria

$$x_j^{min} = \min(x_{1j}, x_{2j}, ..., x_{nj})$$

### Langkah 3: Normalisasi Nilai Kriteria

- **Untuk kriteria benefit:**  
    $$r_{ij} = \frac{x_{ij}}{x_j^{min}}$$
    
- **Untuk kriteria cost:**  
    $$r_{ij} = \frac{x_j^{min}}{x_{ij}}$$

### Langkah 4: Menghitung Nilai CPI
$$CPI_i = \sum_{j=1}^{m} (r_{ij} \times W_j)$$

### Langkah 5: Perangkingan Alternatif

- Alternatif dengan **nilai CPI terbesar** → peringkat tertinggi
    

---

## 6. Contoh Kasus Sederhana

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

### Nilai Minimum

|Kriteria|Nilai Minimum|
|---|---|
|Biaya|40|
|Kualitas|75|
|Layanan|70|

### Normalisasi (contoh A1)

- Biaya (cost): (40/50 = 0,80)
    
- Kualitas (benefit): (80/75 = 1,07)
    
- Layanan (benefit): (70/70 = 1,00)
    
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

### 9. Perbandingan CPI, SAW, WP, dan MPE

### 9.1. Kondisi Umum di Mana CPI Lebih Optimal

Metode **CPI** paling tepat digunakan ketika:

1. **Nilai kriteria memiliki satuan dan skala yang sangat berbeda**
    - Contoh: rupiah, persen, skor, jumlah unit, waktu (hari/jam).
    - CPI menormalkan nilai relatif terhadap **nilai terbaik atau terburuk**, sehingga lebih stabil dibanding SAW.
        
2. **Diperlukan perbandingan kinerja relatif antar alternatif**
    - Fokus CPI bukan sekadar penjumlahan nilai, tetapi **indeks performa relatif**.
    - Cocok untuk evaluasi “seberapa baik alternatif dibandingkan standar terbaik”.
        
3. **Pengambil keputusan membutuhkan hasil yang mudah dijelaskan**
    - Nilai CPI berupa **indeks komposit**, mudah dipahami oleh manajemen non-teknis.
    - Lebih komunikatif dibanding WP (perkalian) atau MPE (eksponensial).
        
4. **Sensitivitas ekstrem perlu dikontrol**
    - CPI tidak terlalu menghukum nilai kecil seperti WP.
    - Tidak seagresif MPE dalam membesarkan perbedaan nilai.
        

---

### 9.2. Perbandingan Kondisi Optimal Antar Metode

|Kondisi Kasus|CPI|SAW|WP|MPE|
|---|---|---|---|---|
|Skala kriteria sangat berbeda|**Sangat cocok**|Kurang stabil|Cukup|Cukup|
|Perlu indeks kinerja relatif|**Sangat cocok**|Kurang|Kurang|Cukup|
|Interpretasi manajerial|**Mudah**|Mudah|Sulit|Sulit|
|Sensitivitas terhadap nilai kecil|Moderat|Rendah|**Sangat tinggi**|Tinggi|
|Data ekstrem/outlier|Lebih stabil|Sensitif|Sangat sensitif|Sangat sensitif|
|Evaluasi kinerja/benchmarking|**Sangat cocok**|Kurang|Tidak cocok|Kurang cocok|

---

### 9.3. Kasus Nyata di Mana CPI Lebih Unggul

#### Evaluasi Kinerja Pegawai

**Kriteria**:
- Produktivitas (unit)
- Kehadiran (%)
- Penilaian atasan (skor)
- Jumlah kesalahan (cost)

**Alasan CPI unggul**:
- Menghasilkan indeks kinerja total
- Mudah dijadikan dasar peringkat dan benchmarking
- Tidak menghukum satu nilai rendah secara ekstrem (dibanding WP)

---

#### Penilaian Kinerja Proyek

**Kriteria**:
- Biaya realisasi (Rp)
- Durasi (hari)
- Kualitas hasil (skor)
- Kepuasan stakeholder (%)

**Alasan CPI unggul**:
- Memungkinkan perbandingan performa proyek terhadap proyek terbaik
- Cocok untuk laporan evaluasi dan monitoring manajemen

---

#### Pemeringkatan Unit Kerja / Cabang

**Kriteria**:
- Pendapatan
- Pertumbuhan
- Efisiensi biaya
- Kepuasan pelanggan

**Alasan CPI unggul**:
- CPI menghasilkan skor komposit yang adil
- Sangat sesuai untuk sistem dashboard DSS

---

#### 9.4. Kapan Menggunakan CPI

CPI **kurang optimal** jika:
- Pengambil keputusan ingin **hukuman keras terhadap satu kriteria buruk** → WP lebih tepat
- Perbedaan antar alternatif perlu diperbesar secara tajam → MPE lebih tepat
- Kasus sederhana dengan data homogen → SAW sudah cukup

**Gunakan CPI ketika**:
- Evaluasi kinerja multi-kriteria
- Skala data beragam
- Hasil harus komunikatif dan adil
- DSS digunakan sebagai alat monitoring dan pemeringkatan

**Gunakan metode lain jika tujuan berbeda**, bukan karena CPI lebih lemah, tetapi karena **fokus keputusan yang tidak sama**.


---
## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [cpi-1.xls](/arsip/cpi-1.xlsx) ([sumber](https://github.com/contohprogram/wp))
 
Modifikasi sheet sesuai kebutuhan

Anda bisa check juga script perhitungan CPI menggunakan python: [cpi1.py](/app/cpi/cpi1.py)

---

## 💼 Diskusi & Tugas

### Soal 1 – Seleksi Penerima Beasiswa

Sebuah perguruan tinggi ingin menentukan **penerima beasiswa** berdasarkan 3 kriteria berikut:

| Kriteria                           | Jenis   | Bobot |
| ---------------------------------- | ------- | ----- |
| IPK                                | Benefit | 0,40  |
| Penghasilan Orang Tua (juta/bulan) | Cost    | 0,35  |
| Jumlah Tanggungan                  | Benefit | 0,25  |

Data 3 mahasiswa sebagai alternatif:

|Mahasiswa|IPK|Penghasilan|Tanggungan|
|---|---|---|---|
|A1|3,80|6|2|
|A2|3,60|4|3|
|A3|3,75|5|1|

**🙋‍♂️ Tugas:**

1. Tentukan nilai minimum atau maksimum tiap kriteria sesuai jenisnya.
2. Hitung nilai **indeks ternormalisasi CPI** untuk setiap kriteria.
3. Hitung **nilai CPI total** tiap mahasiswa.
4. Tentukan **peringkat mahasiswa** berdasarkan nilai CPI.
    

---

### Soal 2 – Pemilihan Supplier

Sebuah perusahaan ingin memilih **supplier terbaik** berdasarkan kriteria berikut:

|Kriteria|Jenis|Bobot|
|---|---|---|
|Harga (Rp/unit)|Cost|0,30|
|Kualitas (skala 1–100)|Benefit|0,35|
|Ketepatan Waktu (%)|Benefit|0,20|
|Jarak (km)|Cost|0,15|

Data supplier:

|Supplier|Harga|Kualitas|Ketepatan Waktu|Jarak|
|---|---|---|---|---|
|S1|52.000|85|90|18|
|S2|50.000|80|95|25|
|S3|55.000|90|85|15|

**🙋‍♂️ Tugas:**

1. Lakukan normalisasi CPI untuk setiap kriteria (benefit dan cost).
2. Hitung nilai CPI terbobot untuk masing-masing supplier.
3. Tentukan supplier terbaik berdasarkan nilai CPI tertinggi.
4. Jelaskan mengapa CPI sesuai digunakan pada kasus ini.
    

---

### Soal 3 – Evaluasi Kinerja Karyawan

Manajer HR ingin mengevaluasi **kinerja karyawan** menggunakan metode CPI dengan kriteria berikut:

|Kriteria|Jenis|Bobot|
|---|---|---|
|Produktivitas (%)|Benefit|0,30|
|Kehadiran (%)|Benefit|0,25|
|Kesalahan Kerja|Cost|0,20|
|Lama Penyelesaian (jam)|Cost|0,25|

Data karyawan:

|Karyawan|Produktivitas|Kehadiran|Kesalahan|Lama Penyelesaian|
|---|---|---|---|---|
|K1|88|95|4|7|
|K2|92|90|6|6|
|K3|85|98|3|8|
|K4|90|93|5|7|

**🙋‍♂️ Tugas:**

1. Tentukan nilai referensi (min/max) tiap kriteria.
2. Hitung indeks CPI masing-masing kriteria.
3. Hitung nilai CPI total setiap karyawan.
4. Urutkan karyawan dari kinerja terbaik hingga terendah.
5. Berikan interpretasi hasil keputusan.

---

### Soal 4 – Pemilihan Lokasi Cabang Usaha

Sebuah perusahaan akan memilih **lokasi cabang usaha terbaik** berdasarkan 5 kriteria berikut:

**Kriteria dan Bobot**

|Kode|Kriteria|Jenis|Bobot|
|---|---|---|---|
|C1|Biaya Sewa (juta/bulan)|Cost|0,25|
|C2|Jumlah Penduduk Sekitar (ribu jiwa)|Benefit|0,20|
|C3|Akses Transportasi (skala 1–10)|Benefit|0,20|
|C4|Tingkat Persaingan (jumlah pesaing)|Cost|0,15|
|C5|Keamanan Lingkungan (skala 1–10)|Benefit|0,20|
|**Total**|||**1,00**|

**Data Alternatif**

|Alternatif|C1|C2|C3|C4|C5|
|---|---|---|---|---|---|
|A1|18|45|7|5|8|
|A2|20|50|8|6|7|
|A3|16|40|6|4|9|
|A4|22|55|9|7|8|
|A5|17|48|7|5|6|
|A6|19|52|8|6|9|
|A7|15|38|6|3|7|

**🙋‍♂️ Tugas**

1. Tentukan **nilai referensi** tiap kriteria:
2. Lakukan **normalisasi CPI** dengan rumus:
3. Hitung **nilai CPI terbobot**:  
4. Tentukan **peringkat alternatif** berdasarkan nilai CPI terbesar.
5. Jelaskan **alternatif terbaik** sebagai rekomendasi keputusan dan berikan alasan singkat berdasarkan kontribusi kriteria dominan.

---

### Soal 5 – Perbandingan dengan SAW

Lihat contoh perhitungan SAW ([simpleadditiveweight.xlsx](simpleadditiveweight.xlsx)), lakukan perhitungan dari data serupa (bobot dan alterlatifnya ambil dari file tersebut) menggunakan CPI.
