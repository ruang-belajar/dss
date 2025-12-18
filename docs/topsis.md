# Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)

## 1. Pendahuluan

TOPSIS merupakan salah satu metode penunjang Keputusan banyak kriteria yang pertama kali diperkenalkan oleh Yoon dan Hwang (Ying-Liang, WuXing-Yan Zhu, 2011).

TOPSIS menggunakan prinsip bahwa alternatif yang dipilih harus memiliki jarak terpendek dari solusi ideal positif dan memiliki jarak terjauh dari solusi ideal negatif dari titik geometris menggunakan jarak Euclidean untuk menentukan kedekatan relatif antara alternatif ke solusi yang optimal (Ding dkk, 2016).

Solusi ideal positif didefinisikan sebagai jumlah dari seluruh nilai terbaik yang dapat dicapai untuk setiap atribut, sedangkan Solusi negatif-ideal terdiri dari seluruh nilai terendah yang dicapai untuk setiap atribut. TOPSIS mempertimbangkan keduanya, jarak terhadap solusi ideal positif dan jarak terhadap solusi ideal negatif dengan mengambil kedekatan relatif terhadap solusi ideal positif. Berdasarkan perbandingan terhadap jarak relatifnya, susunan prioritas alternatif bisa dicapai (Wang dkk, 2019).

Metode TOPSIS digunakan sebagai suatu upaya untuk menyelesaikan permasalahan multiple criteria decision making. Hal ini disebabkan konsepnya sederhana dan mudah dipahami, komputasinya efisien dan memiliki kemampuan untuk mengukur kinerja relatif dari alternatifalternatif keputusan. Metode ini banyak digunakan untuk menyelesaikan pengambilan keputusan secara praktis.

---

## 2. Konsep Dasar TOPSIS

TOPSIS didasarkan pada beberapa konsep utama:

1. **Alternatif**: objek atau pilihan yang akan dievaluasi.
    
2. **Kriteria**: faktor atau atribut penilaian (benefit atau cost).
    
3. **Bobot Kriteria**: tingkat kepentingan relatif setiap kriteria.
    
4. **Solusi Ideal Positif (A⁺)**: nilai terbaik dari setiap kriteria.
    
5. **Solusi Ideal Negatif (A⁻)**: nilai terburuk dari setiap kriteria.
    
6. **Jarak Euclidean**: ukuran kedekatan alternatif terhadap solusi ideal.
    

---

## 3. Asumsi dan Karakteristik TOPSIS

- Nilai kriteria bersifat numerik dan dapat dibandingkan.
    
- Bobot kriteria telah ditentukan sebelumnya.
    
- Setiap kriteria diasumsikan bersifat monoton (semakin besar semakin baik, atau sebaliknya).
    
- Tidak memperhitungkan hubungan antar kriteria.
    

---

## 4. Langkah-langkah Perhitungan TOPSIS

Kita akan mempelajari perhitungan TOPSIS lewat sebuah contoh kasus: Pemilihan **supplier terbaik** berdasarkan 3 kriteria.

**Kriteria**

| Kode | Kriteria        | Jenis   |
| ---- | --------------- | ------- |
| C1   | Harga           | Cost    |
| C2   | Kualitas        | Benefit |
| C3   | Ketepatan Waktu | Benefit |

**Bobot Kriteria**
- w₁ (Harga) = 0,4
- w₂ (Kualitas) = 0,35
- w₃ (Ketepatan Waktu) = 0,25  
    (∑w = 1)
    

---

#### Langkah 1: Buat Matriks Keputusan

| Alternatif | C1 (Harga) | C2 (Kualitas) | C3 (Waktu) |
| ---------- | ---------- | ------------- | ---------- |
| A1         | 50         | 80            | 90         |
| A2         | 60         | 85            | 80         |
| A3         | 55         | 75            | 85         |

---

#### Langkah 2: Normalisasi Matriks Keputusan

Menggunakan **normalisasi vektor**:

$$r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{m} x_{ij}^2}}$$

**Hitung penyebut tiap kriteria**

- C1: √(50² + 60² + 55²) = √8625 = **92,87**
    
- C2: √(80² + 85² + 75²) = √19250 = **138,74**
    
- C3: √(90² + 80² + 85²) = √21725 = **147,40**
    

**Matriks Normalisasi (R)**

|Alternatif|C1|C2|C3|
|---|---|---|---|
|A1|0,538|0,577|0,610|
|A2|0,646|0,613|0,543|
|A3|0,592|0,541|0,577|

---

#### Langkah 3: Normalisasi Terbobot

$$v_{ij} = w_j \times r_{ij}$$

|Alternatif|C1|C2|C3|
|---|---|---|---|
|A1|0,215|0,202|0,153|
|A2|0,258|0,215|0,136|
|A3|0,237|0,189|0,144|

---

#### Langkah 4: Menentukan Solusi Ideal Positif (A⁺) dan Negatif (A⁻)

|Kriteria|Jenis|A⁺ (Ideal +)|A⁻ (Ideal −)|
|---|---|---|---|
|C1|Cost|**min** = 0,215|**max** = 0,258|
|C2|Benefit|**max** = 0,215|**min** = 0,189|
|C3|Benefit|**max** = 0,153|**min** = 0,136|

---

#### Langkah 5: Menghitung Jarak ke Solusi Ideal

##### Jarak ke Solusi Ideal Positif (D⁺)

$$D_i^+ = \sqrt{\sum (v_{ij} - A_j^+)^2}$$

- A1 = 0
- A2 = 0,048
- A3 = 0,040

##### Jarak ke Solusi Ideal Negatif (D⁻)

$$D_i^- = \sqrt{\sum (v_{ij} - A_j^-)^2}$$

- A1 = 0,053
- A2 = 0,026
- A3 = 0,032

---

#### Langkah 6: Menghitung Nilai Preferensi

$$C_i = \frac{D_i^-}{D_i^+ + D_i^-}$$

|Alternatif|Cᵢ|
|---|---|
|A1|**1,000**|
|A2|0,351|
|A3|0,444|

---

#### Langkah 7: Perangkingan Alternatif

|Peringkat|Alternatif|Nilai Preferensi|
|---|---|---|
|1|**A1**|1,000|
|2|A3|0,444|
|3|A2|0,351|

**Interpretasi dalam DSS:**
- **A1** adalah alternatif terbaik karena **paling dekat dengan solusi ideal positif dan paling jauh dari solusi ideal negatif**.
- Nilai preferensi dapat langsung digunakan sebagai **output rekomendasi DSS**.
- Cocok untuk modul **ranking dan selection engine**.


---

## 5. Kelebihan dan Keterbatasan TOPSIS

TOPSIS banyak digunakan dengan alasan:
- Konsepnya sederhana dan mudah dipahami.
- Komputasi efisien.
- Memiliki kemampuan mengukur kinerja relatif dari alternatif alternatif
- keputusan dalam bentuk matematis yang sederhana
    
**Kelemahan** metodeTOPSIS Beberapa kelemahan dari metodeTOPSIS sebagai berikut (Syafnidawaty,2020):

- Belum adanya penentuan bobot prioritas yang menjadi prioritas hitungan terhadap kriteria, yang berguna untuk meningkatkan validitas nilai bobot perhitungan kriteria. Maka dengan alasan ini, metode ini dapat dikombinasikan misalnya dengan metodeAHPagar menghasilkanoutput atau keputusan yang lebih maksimal.
    
- Belum adanya bentuk linguistik untuk penilaian alternatif terhadap kriteria, biasanya bentuk linguistik ini diinterpretasikan dalam sebuah bilangan fuzzy
    
- Belum adanya mediator seperti hirarki jika diproses secara mandiri maka dalam ketepatan pengambilan keputusan cenderungbelum menghasilkan keputusan yang sempurna
    
- Metode TOPSIS ini dapat digunakan dalam menentukan perangkingan alternatif dengan memperhitungkan solusi ideal dari suatu masalah dan penentuan bobot setiap kriteria. Namun, kurang baik jika digunakan dalam mendapatkanbobot yang memperhitungkanhubungan antara kriteria.

- Pada proses yang menggunakan metode TOPSIS, perangkingan dan pembobotan kriteria adalah memiliki nilai yang telah pasti. Padahal, dalam aplikasinya di kehidupan nyata, terdapat informasi yang tidak lengkap atau informasi yang dibutuhkan tidak tersedia.
    
- Metode TOPSIS menentukan solusi berdasarkan jarak terpendek menuju solusi ideal dan jarak terbesar dari solusi negatif yang ideal. Namun, metode ini tidak mempertimbangkan kepentingan relatif (relative importance) dari masing-masing jarak tersebut.
    
- Pada metode TOPSIS, seringkali digunakan asumsi pada tingkat kepentingan relatif masing-masing respon dan digunakan kombinasi dengan metodelain untuk menyelesaikan asumsitersebut
    
- Pada metode TOPSIS, alternatif dengan ranking tertinggi merupakan solusi yang terbaik, namun belum tentu ranking tertinggi tersebut adalah yang terdekat dari solusi ideal.

**Kelebihan** metode TOPSIS Selain memiliki kekurangan, namun metode memiliki kelebihan sebagai berikut (Syafnidawaty, 2020):

- Konsepnya sederhana dan mudah dipahami, kesederhanaan ini dilihat dari alur proses metode TOPSIS yang tidak begitu rumit. Karena menggunakan indikator kriteria dan variabel alternatif sebagai pembantu untuk menentukan keputusan
    
- Komputasinya efisien, perhitungan komputasinya lebih efisien dan dan cepat
    
- Mampu dijadikan sebagai pengukur kinerja alternatif dan juga alternatif keputusan dalam sebuah bentuk output komputasi yang sederhana.
    
- Dapat digunakan sebagai metode pengambilan keputusan yang lebihcepat.

---

## 6. Perbandingan TOPSIS dengan Metode Lain

### 6.1. Kondisi Masalah yang Paling Sesuai untuk TOPSIS

TOPSIS paling optimal digunakan ketika:

1. **Tujuan utama adalah memilih alternatif yang paling mendekati kondisi ideal**
    - Ada konsep **solusi ideal positif (terbaik)** dan **solusi ideal negatif (terburuk)**.
    - Keputusan tidak hanya ingin nilai terbesar, tetapi juga **paling jauh dari kondisi terburuk**.
        
2. **Terdapat konflik antar kriteria**
    - Contoh:
        - Biaya (cost) rendah vs kualitas (benefit) tinggi
        - Risiko rendah vs keuntungan tinggi
    - TOPSIS menangani trade-off ini lebih eksplisit dibanding SAW atau CPI.
        
3. **Jumlah alternatif dan kriteria relatif banyak**
    - Efektif untuk:
        - Seleksi vendor
        - Prioritas proyek
        - Evaluasi risiko
        - Penilaian kinerja multi-dimensi
            
4. **Pengambil keputusan membutuhkan hasil yang rasional dan mudah dijustifikasi**
    - Konsep “kedekatan ke solusi ideal” mudah dijelaskan kepada stakeholder non-teknis.

---

### 6.2. Karakteristik Data yang Mendukung TOPSIS

TOPSIS unggul ketika data memiliki karakteristik berikut:

| Karakteristik Data           | Keterangan                                         |
| ---------------------------- | -------------------------------------------------- |
| Data numerik terukur         | Skala interval atau rasio                          |
| Kriteria campuran            | Ada benefit dan cost                               |
| Skala antar kriteria berbeda | Ditangani dengan normalisasi vektor                |
| Bobot kriteria tersedia      | Biasanya dari AHP, expert judgment, atau kebijakan |

---

### 6.3. Keunggulan TOPSIS Dibanding Metode Lain

#### Dibanding SAW

**TOPSIS lebih optimal jika:**
- Selisih nilai antar alternatif kecil tetapi signifikan.
- Diperlukan penalti terhadap alternatif yang mendekati nilai terburuk.

**Kelemahan SAW yang ditutupi TOPSIS:**
- SAW hanya menjumlahkan skor → alternatif bisa unggul meski buruk di satu kriteria kritis.

#### Dibanding Weighted Product (WP)

**TOPSIS lebih optimal jika:**
- Data mengandung nilai nol atau mendekati nol.
- Dibutuhkan interpretasi yang lebih intuitif.

**Kelemahan WP:**
- Sensitif terhadap nilai ekstrem.
- Sulit dijelaskan ke manajemen non-teknis.

#### Dibanding MPE (Metode Perbandingan Eksponensial)

**TOPSIS lebih optimal jika:**
- Tidak ingin efek eksponensial yang memperbesar perbedaan kecil.
- Fokus pada kedekatan relatif terhadap solusi ideal, bukan dominasi satu kriteria.

#### Dibanding CPI

**TOPSIS lebih optimal jika:**
- Alternatif memiliki profil kelebihan dan kelemahan yang seimbang.
- Pengambil keputusan ingin mempertimbangkan jarak terhadap kondisi terburuk secara eksplisit.

**CPI lebih cocok untuk:**
- Penilaian kinerja agregat atau pemeringkatan administratif.

---

### 6.4. Contoh Kasus di Mana TOPSIS Lebih Optimal

#### Seleksi Vendor Strategis

**Kriteria:**
- Harga (cost)
- Kualitas (benefit)
- Risiko pasokan (cost)
- Ketepatan waktu (benefit)

**Alasan TOPSIS optimal:**
- Vendor terbaik bukan hanya murah, tetapi juga paling dekat ke vendor “ideal”.

---

#### Prioritas Proyek Investasi

**Kriteria:**
- ROI (benefit)
- Risiko (cost)
- Waktu implementasi (cost)
- Dampak strategis (benefit)

TOPSIS mampu:
- Menyeimbangkan risiko dan manfaat secara simultan.

---

#### Penilaian Risiko dalam RMS

**Kriteria:**
- Probabilitas (cost)
- Dampak finansial (cost)
- Dampak reputasi (cost)
- Kesiapan mitigasi (benefit)

TOPSIS:
- Memilih risiko yang paling “kritis” berdasarkan kedekatan ke kondisi terburuk.

---

### 6.5. Ringkasan Perbandingan Singkat

|Kondisi Utama|Metode Paling Optimal|
|---|---|
|Kedekatan ke solusi ideal & anti-ideal|**TOPSIS**|
|Penilaian cepat dan sederhana|SAW|
|Rasio dan perbandingan relatif kuat|WP|
|Penekanan dominasi kriteria|MPE|
|Indeks kinerja agregat|CPI|

---

## 6. Kesimpulan DSS

**TOPSIS paling optimal digunakan ketika DSS:**
- Menghadapi **multi-kriteria yang saling bertentangan**
- Membutuhkan **hasil yang adil, seimbang, dan mudah dipertanggungjawabkan**
- Digunakan untuk **keputusan strategis atau semi-strategis**, bukan sekadar administratif
    
Jika diinginkan, saya dapat:
- Menyusun **tabel panduan pemilihan metode DSS**
- Memberikan **studi kasus komparatif SAW vs TOPSIS**
- Menyediakan **contoh perhitungan numerik TOPSIS** untuk konteks tertentu (risiko, vendor, proyek)
    
---

## 📚 Referensi Singkat

- Hwang, C. L., & Yoon, K. (1981). _Multiple Attribute Decision Making: Methods and Applications_. Springer.
- Triantaphyllou, E. (2000). _Multi-Criteria Decision Making Methods_. Springer.
- Krzysztof Palczewskia, Wojciech Sałabuna, ” The fuzzy TOPSIS applications in the last decade”., 23rd International Conference on Knowledge-Based and Intelligent Information & Engineering System., 2019
- Ahmad Abdul Chamid., “Penerapan Metode Topsis Untuk Menentukan Prioritas Kondisi Rumah”.,
- Irvan Muzakkir., “Penerapan Metode Topsis untuk Sistem Pendukung Keputusan Penentuan Keluarga Miskin pada Desa Panca Karsa II., Jurnal Ilmu Komputer., Volume 9 Nomor 3 Desember 2017
- Vinay Yadav, Subhankar Karmakar, Pradip P. Kalbar, A.K. Dikshit. “PyTOPS: A Python based tool for TOPSIS., Software X., Volume 9, January–June 2019, Pages 217-222
- Bruno Miranda dos Santos, Leoni Pentiado Godoy, Lucila M.S. Campos., “Performance evaluation of green suppliers using entropy-TOPSIS-F., Journal of Cleaner Production, Volume 207, 10 January 2019, Pages 498-509
- [Metode Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) by Feri Alpiyasin, M.Kom](https://www.canva.com/design/DAG7of6ouEw/jQjx6yC57R9QyDPLgojAWg/edit)