# Simple Additive Weighting (SAW)

Dalam sistem pendukung keputusan (DSS), seringkali diperlukan suatu metode untuk membantu pengambil keputusan dalam memilih alternatif terbaik dari beberapa pilihan yang tersedia. Salah satu metode yang paling sederhana dan populer adalah **Simple Additive Weighting (SAW)**.  
Metode ini sering disebut juga sebagai **metode penjumlahan terbobot**, karena prinsip utamanya adalah menjumlahkan nilai-nilai dari setiap kriteria yang telah diberi bobot sesuai tingkat kepentingannya.

---

## 1. Konsep Dasar SAW

### 1.1. Pengertian

**Simple Additive Weighting (SAW)** merupakan salah satu metode yang dapat digunakan dalam menyelesaikan masalah Multi-Criteria Decision Making (MCDM), MCDM suatu metode pengambilan keputusan yang mengambil banyak kriteria sebagai dasar dalam pengambilan keputusan. (Fishburn 1967)

Metode SAW dikenal sebagai metode dengan penjumlahan terbobot. Konsep dasar metode SAW adalah mencari penjumlahan terbobot dari rating kinerja pada setiap alternatif pada seluruh atribut.

Metode SAW membutuhkan proses normalisasi matriks keputusan (X) ke suatu skala yang dapat diperbandingkan dengan semua rating alternatif yang ada.

### 1.2. Tujuan Metode SAW

- Membantu pengambilan keputusan dengan banyak kriteria.
    
- Menyediakan perhitungan yang sederhana dan efisien.
    
- Memberikan hasil berupa **peringkat alternatif terbaik**.

### 1.3. Karakteristik SAW

- Mudah dipahami dan diimplementasikan.
    
- Menggunakan **konsep normalisasi** agar semua kriteria berada dalam skala yang sama.
    
- Cocok digunakan untuk **pengambilan keputusan multi-kriteria (MCDM)**.
    
- Dapat menangani **kriteria keuntungan (benefit)** maupun **kriteria biaya (cost)**.
    

---

## 2. Langkah-Langkah Metode SAW

Langkah-langkah umum dalam penerapan metode SAW adalah sebagai berikut:

### Langkah 1. Menentukan Kriteria dan Alternatif

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

### Langkah 2. Menyusun Matriks Keputusan (X)

Susun tabel berisi nilai-nilai alternatif terhadap setiap kriteria.

Contoh:

|Alternatif|C₁|C₂|C₃|
|---|---|---|---|
|A₁|5|70|80|
|A₂|4|80|70|
|A₃|3|60|90|

---

### Langkah 3. Normalisasi Matriks Keputusan

Normalisasi dilakukan agar semua nilai berada dalam skala yang sama (0–1).

Rumus normalisasi:

- Untuk **kriteria benefit (semakin besar semakin baik)**:  
	    $$r_{ij} = \frac{x_{ij}}{\max(x_j)}$$
    
- Untuk **kriteria cost (semakin kecil semakin baik)**:  
    $$r_{ij} = \frac{\min(x_j)}{x_{ij}}$$
    

Contoh hasil normalisasi (asumsi C₁ = cost, C₂ & C₃ = benefit):

| Alternatif | C₁          | C₂            | C₃            |
| ---------- | ----------- | ------------- | ------------- |
| A₁         | 3/5 = 0.6   | 70/80 = 0.875 | 80/90 = 0.888 |
| A₂         | 3/4 = 0.75  | 80/80 = 1.000 | 70/90 = 0.778 |
| A₃         | 3/3 = 1.000 | 60/80 = 0.75  | 90/90 = 1.000 |

---

### Langkah 4. Menghitung Nilai Preferensi (V)

Setelah normalisasi, nilai total untuk setiap alternatif dihitung dengan:  
$$V_i = \sum_{j=1}^{n} (w_j \times r_{ij})$$
$V_i$ = Nilai akhir dari alternatif
$w_j$ = Bobot yang telah ditentukan
$r_{ij}$ = Normalisasi matrix

**Contoh perhitungan:**

|Alternatif|Perhitungan|Nilai Akhir (Vᵢ)|
|---|---|---|
|A₁|(0.3×0.6) + (0.4×0.875) + (0.3×0.888)|0.792|
|A₂|(0.3×0.75) + (0.4×1.000) + (0.3×0.778)|0.863|
|A₃|(0.3×1.000) + (0.4×0.75) + (0.3×1.000)|0.925|

---

### Langkah 5. Menentukan Alternatif Terbaik

Alternatif dengan **nilai total tertinggi (Vᵢ terbesar)** adalah alternatif terbaik.  
→ Dalam contoh di atas, **A₃** merupakan pilihan terbaik karena memiliki nilai 0.925.

---

## 3. Kelebihan dan Kelemahan SAW

|**Kelebihan**|**Kelemahan**|
|---|---|
|Mudah dipahami dan digunakan|Tidak mempertimbangkan interaksi antar kriteria|
|Perhitungannya cepat dan sederhana|Rentan terhadap skala penilaian yang tidak konsisten|
|Cocok untuk kasus dengan banyak alternatif|Mengasumsikan hubungan linear antara nilai dan bobot|
|Dapat diterapkan di berbagai bidang|Sensitif terhadap perubahan bobot|

---

## 4. Contoh Kasus Nyata

### Kasus: Pemilihan Smartphone Terbaik

Kriteria:

- C₁: Harga (Cost)
    
- C₂: Kamera (Benefit)
    
- C₃: Baterai (Benefit)
    
- Bobot: [0.3, 0.4, 0.3]
    

Langkah-langkah perhitungan dilakukan seperti di atas untuk menentukan smartphone terbaik berdasarkan data penilaian.

Check juga beberapa contoh kasus berikut:
1. [Kasus: Seleksi Karyawan untuk Promosi](/case/case-saw-hrd-1.md)
2. [Kasus: Memilih Smartphone](/case/case-saw-smartphone-1.md)


---

## 5. Implementasi dalam DSS

Metode SAW sering diintegrasikan dalam sistem pendukung keputusan berbasis komputer seperti:

- Sistem pemilihan karyawan terbaik
    
- Sistem rekomendasi produk
    
- Sistem seleksi beasiswa
    
- Sistem penentuan lokasi usaha
    

Biasanya, DSS berbasis SAW dibangun menggunakan **basis data + bahasa pemrograman (PHP, Python, Java)** dan menghasilkan laporan keputusan otomatis.

---

## 6. Kesimpulan

- **SAW** adalah metode MCDM sederhana namun efektif untuk pengambilan keputusan berbasis kriteria ganda.
    
- Proses utamanya adalah **normalisasi → pembobotan → penjumlahan terbobot**.
    
- Alternatif terbaik adalah yang memiliki nilai **V tertinggi**.
    
- Meskipun sederhana, metode ini sangat bermanfaat untuk aplikasi praktis DSS di berbagai bidang.
    

---

## 💼 Diskusi & Tugas

### Soal 1 -- Pemilihan Karyawan Terbaik

Sebuah perusahaan ingin menentukan **karyawan terbaik** berdasarkan beberapa kriteria.  
Empat kandidat yang dinilai adalah:

- A₁ = Andi
    
- A₂ = Budi
    
- A₃ = Citra
    
- A₄ = Dedi
    

Perusahaan menggunakan **4 kriteria** berikut:

| Kode | Kriteria         | Jenis Kriteria | Bobot (W) |
| ---- | ---------------- | -------------- | --------- |
| C₁   | Disiplin         | Benefit        | 0,30      |
| C₂   | Prestasi Kerja   | Benefit        | 0,40      |
| C₃   | Pengalaman Kerja | Benefit        | 0,20      |
| C₄   | Absensi (hari)   | Cost           | 0,10      |

Berikut hasil penilaian awal (skor sebelum normalisasi):

| Alternatif | C₁ (Disiplin) | C₂ (Prestasi) | C₃ (Pengalaman) | C₄ (Absensi) |
| ---------- | ------------- | ------------- | --------------- | ------------ |
| A₁ Andi    | 80            | 70            | 5               | 3            |
| A₂ Budi    | 90            | 85            | 3               | 2            |
| A₃ Citra   | 75            | 95            | 4               | 4            |
| A₄ Dedi    | 85            | 80            | 6               | 1            |

🎯 **Tugas (Soal):**
1. Lakukan **normalisasi matriks keputusan** menggunakan metode SAW.
2. Hitung **nilai preferensi (Vi)** untuk masing-masing alternatif:  
3. Tentukan **alternatif terbaik** berdasarkan nilai _Vi_ tertinggi.

---
### Soal 2 -- Pemilihan Menu Restoran

Sebuah restoran ingin menentukan **menu unggulan** yang akan dipromosikan bulan depan.  
Pemilihan dilakukan berdasarkan beberapa **kriteria penilaian dari pelanggan dan manajer restoran**.

**🥘 Daftar Alternatif (Menu):**
- A₁ = Nasi Goreng Spesial    
- A₂ = Ayam Bakar Madu    
- A₃ = Sate Ayam    
- A₄ = Mie Goreng Seafood    


**⚙️ Kriteria Penilaian:**

| Kode | Kriteria        | Bobot (W) |
| ---- | --------------- | --------- |
| C₁   | Rasa            | 0,40      |
| C₂   | Harga           | 0,25      |
| C₃   | Kandungan Gizi  | 0,20      |
| C₄   | Waktu Penyajian | 0,15      |

**📊 Data Penilaian Awal (Skor dari Survei):**

| Menu (Alternatif) | C₁ (Rasa) | C₂ (Harga, ribu) | C₃ (Gizi) | C₄ (Waktu, menit) |
| ----------------- | --------- | ---------------- | --------- | ----------------- |
| A₁                | 85        | 25               | 80        | 10                |
| A₂                | 90        | 30               | 75        | 15                |
| A₃                | 80        | 20               | 70        | 12                |
| A₄                | 95        | 28               | 85        | 8                 |

**🎯 Tugas (Soal):**
1. Lakukan **normalisasi matriks keputusan** berdasarkan kriteria _benefit_ dan _cost_ menggunakan rumus:
2. Hitung **nilai preferensi (Vᵢ)** untuk setiap menu menggunakan rumus:
3. Tentukan **menu terbaik** yang layak dijadikan **menu unggulan promosi** berdasarkan nilai _Vᵢ_ tertinggi.

---

## Referensi:
- [Metode SAW by Feri Alpiyasin, M.Kom](https://www.canva.com/design/DAG1uVWyIvk/4tGRZzsmkF0XCtO88OBLsg/edit)