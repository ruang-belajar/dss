![](topsis-header.png)
# Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)

## 1. Pendahuluan

TOPSIS merupakan salah satu metode penunjang Keputusan banyak kriteria yang pertama kali diperkenalkan oleh Yoon dan Hwang (Ying-Liang, WuXing-Yan Zhu, 2011).

TOPSIS menggunakan prinsip bahwa alternatif yang dipilih harus memiliki jarak terpendek dari solusi ideal positif dan memiliki jarak terjauh dari solusi ideal negatif dari titik geometris menggunakan jarak Euclidean untuk menentukan kedekatan relatif antara alternatif ke solusi yang optimal (Ding dkk, 2016).

Solusi ideal positif didefinisikan sebagai jumlah dari seluruh nilai terbaik yang dapat dicapai untuk setiap atribut, sedangkan Solusi negatif-ideal terdiri dari seluruh nilai terendah yang dicapai untuk setiap atribut. TOPSIS mempertimbangkan keduanya, jarak terhadap solusi ideal positif dan jarak terhadap solusi ideal negatif dengan mengambil kedekatan relatif terhadap solusi ideal positif. Berdasarkan perbandingan terhadap jarak relatifnya, susunan prioritas alternatif bisa dicapai (Wang dkk, 2019).

Metode TOPSIS digunakan sebagai suatu upaya untuk menyelesaikan permasalahan multiple criteria decision making. Hal ini disebabkan konsepnya sederhana dan mudah dipahami, komputasinya efisien dan memiliki kemampuan untuk mengukur kinerja relatif dari alternatifalternatif keputusan. Metode ini banyak digunakan untuk menyelesaikan pengambilan keputusan secara praktis.

---

## 2. Konsep Dasar TOPSIS

TOPSIS didasarkan pada beberapa konsep utama:

### 1️⃣ Solusi Ideal dalam TOPSIS

Konsep inti TOPSIS adalah penggunaan dua solusi hipotetik sebagai titik pembanding:

#### Solusi Ideal Positif (A⁺)
Solusi ideal positif merepresentasikan kondisi paling diinginkan, yang dibentuk dari:
- Nilai maksimum untuk setiap kriteria **benefit**.
- Nilai minimum untuk setiap kriteria **cost**.

Solusi ini mencerminkan performa optimal yang secara teoritis dapat dicapai.

#### Solusi Ideal Negatif (A⁻)
Solusi ideal negatif merepresentasikan kondisi paling tidak diinginkan, yang dibentuk dari:
- Nilai minimum untuk setiap kriteria **benefit**.
- Nilai maksimum untuk setiap kriteria **cost**.
    
Solusi ini menjadi batas bawah performa alternatif.

### 2️⃣ Kedekatan Relatif sebagai Dasar Penilaian

TOPSIS tidak menilai alternatif secara absolut, melainkan secara **relatif** terhadap dua solusi ideal tersebut.

Penilaian dilakukan dengan menghitung:
- **Jarak ke solusi ideal positif (D⁺)**
- **Jarak ke solusi ideal negatif (D⁻)**

Umumnya, jarak dihitung menggunakan **Euclidean distance** dalam ruang multidimensi kriteria.

### 3️⃣ Koefisien Kedekatan (Closeness Coefficient)

Kedekatan relatif setiap alternatif dirangkum dalam satu nilai indeks yang disebut **nilai preferensi** atau _closeness coefficient_:

$$C_i = \frac{D_i^-}{D_i^+ + D_i^-}$$

Karakteristik nilai ini:
- Rentang nilai: 0 ≤ Cᵢ ≤ 1
- Semakin besar nilai Cᵢ, semakin baik alternatif tersebut

Nilai inilah yang digunakan untuk melakukan **perangkingan alternatif**.

### 4️⃣ Peran Bobot Kriteria

Bobot kriteria mencerminkan tingkat kepentingan relatif antar kriteria.

Dalam TOPSIS:
- Bobot digunakan untuk membentuk matriks keputusan terbobot.
- Bobot memengaruhi posisi solusi ideal dan jarak alternatif terhadap solusi ideal.
    
Oleh karena itu, keakuratan hasil TOPSIS sangat bergantung pada **validitas bobot** yang digunakan.

### 5️⃣ Normalisasi sebagai Fondasi Perbandingan

Karena kriteria dapat memiliki satuan dan skala yang berbeda, TOPSIS melakukan **normalisasi data** agar:
- Setiap kriteria berada pada skala yang sebanding.
- Tidak terjadi dominasi kriteria tertentu akibat perbedaan satuan.

Normalisasi membentuk ruang keputusan yang adil untuk perhitungan jarak.

---

## 3. Asumsi Data yang digunakan dalam TOPSIS

Asumsi merupakan kondisi dasar yang harus dipenuhi agar hasil TOPSIS valid dan dapat diinterpretasikan dengan benar.

1. Alternatif Bersifat Terbatas dan Terdefinisi Jelas
	- Seluruh alternatif keputusan sudah diketahui sejak awal.
	- Tidak ada penambahan atau pengurangan alternatif selama proses perhitungan.
	- Implikasi DSS:  
		- TOPSIS cocok untuk _batch decision making_, bukan untuk keputusan dinamis real-time.

2. Kriteria Bersifat Monoton
	- Untuk setiap kriteria, preferensi bersifat:
	    - **Benefit**: semakin besar nilai, semakin baik.
	    - **Cost**: semakin kecil nilai, semakin baik.
	- Implikasi DSS:  
		- Kriteria harus diklasifikasikan secara tegas sebagai benefit atau cost sebelum perhitungan.

3. Nilai Kriteria Berskala Kuantitatif
	- Data kriteria berupa angka numerik.
	- Data kualitatif harus dikonversi terlebih dahulu (misalnya melalui skala Likert).
	- Implikasi DSS:  
		- Diperlukan modul _pre-processing_ atau _data transformation_.]]

4. Bobot Kriteria Diketahui dan Tetap
	- Bobot kriteria mencerminkan tingkat kepentingan relatif.
    - Bobot tidak berubah selama proses evaluasi.
	* Implikasi DSS: 
		* Penentuan bobot biasanya dilakukan dengan metode lain (AHP, expert judgment).

5. Kriteria Bersifat Independen
	- Tidak ada hubungan saling memengaruhi antar kriteria.
	- Tidak terjadi redundansi informasi.
	- Implikasi DSS:  TOPSIS tidak cocok jika terdapat korelasi kuat antar kriteria.

---

## 4. Langkah-langkah Perhitungan TOPSIS

Mari kita gunakan contoh sederhana untuk memahami perhitungan TOPSIS.

Berikut contoh skenario **Pemilihan Lokasi Gudang Baru** menggunakan TOPSIS

> Sebuah perusahaan logistik harus memilih satu dari tiga lokasi berdasarkan biaya sewa, jarak ke pelabuhan, dan luas bangunan.

**Alternatif:**
- **L1**: Lokasi A
- **L2**: Lokasi B
- **L3**: Lokasi C

**Kriteria & Bobot ($W$):**
1. **C1: Biaya Sewa** (Cost) | Bobot: **0.5**
2. **C2: Jarak ke Pelabuhan** (Cost) | Bobot: **0.3**
3. **C3: Luas Bangunan** (Benefit) | Bobot: **0.2**

**Data Awal (Matriks Keputusan $X$)**

| **Alternatif** | **C1 (Juta/Bulan)** | **C2 (Km)** | **C3 (m2)** |
| -------------- | ------------------- | ----------- | ----------- |
| **L1**         | 20                  | 15          | 500         |
| **L2**         | 30                  | 10          | 800         |
| **L3**         | 25                  | 20          | 600         |

---

### Langkah 1: Normalisasi Matriks ($R$)

Kita hitung pembagi untuk setiap kriteria menggunakan rumus $\sqrt{\sum x_{ij}^2}$:

- **C1**: $\sqrt{20^2 + 30^2 + 25^2} = 43.87$
    
- **C2**: $\sqrt{15^2 + 10^2 + 20^2} = 26.92$
    
- **C3**: $\sqrt{500^2 + 800^2 + 600^2} = 1118.03$
    

**Matriks $R$ (Data / Pembagi):**

| **Alt** | **C1** | **C2** | **C3** |
| ------- | ------ | ------ | ------ |
| **L1**  | 0.456  | 0.557  | 0.447  |
| **L2**  | 0.684  | 0.371  | 0.715  |
| **L3**  | 0.570  | 0.743  | 0.537  |

### Langkah 2: Matriks Normalisasi Terbobot ($Y$)

Kalikan setiap kolom di matriks $R$ dengan bobotnya ($W$).

- $C1 \times 0.5$, $C2 \times 0.3$, $C3 \times 0.2$

**Matriks $Y$:**

| **Alt** | **C1 (W=0.5)** | **C2 (W=0.3)** | **C3 (W=0.2)** |
| ------- | -------------- | -------------- | -------------- |
| **L1**  | 0.228          | 0.167          | 0.089          |
| **L2**  | 0.342          | 0.111          | 0.143          |
| **L3**  | 0.285          | 0.223          | 0.107          |

### Langkah 3: Solusi Ideal Positif ($A^+$) & Negatif ($A^-$)

- **$A^+$**: Ambil **Min** untuk Cost (C1, C2) dan **Max** untuk Benefit (C3).
    
- **$A^-$**: Ambil **Max** untuk Cost (C1, C2) dan **Min** untuk Benefit (C3).
    

|**Tipe**|**C1 (Cost)**|**C2 (Cost)**|**C3 (Benefit)**|
|---|---|---|---|
|**$A^+$**|**0.228**|**0.111**|**0.143**|
|**$A^-$**|**0.342**|**0.223**|**0.089**|

### Langkah 4: Jarak Solusi ($D^+$ dan $D^-$)

Gunakan rumus Euclidean Distance untuk mencari jarak tiap alternatif ke $A^+$ dan $A^-$.

|**Alternatif**|**Jarak ke Positif (D+)**|**Jarak ke Negatif (D−)**|
|---|---|---|
|**L1**|$\sqrt{(0.228-0.228)^2 + (0.167-0.111)^2 + (0.089-0.143)^2} = \mathbf{0.078}$|**0.128**|
|**L2**|$\sqrt{(0.342-0.228)^2 + (0.111-0.111)^2 + (0.143-0.143)^2} = \mathbf{0.114}$|**0.124**|
|**L3**|$\sqrt{(0.285-0.228)^2 + (0.223-0.111)^2 + (0.107-0.143)^2} = \mathbf{0.131}$|**0.060**|
Menghitung _Jarak ke Negatif (D-)_ menggunakan rumus yang sama dengan menghitung _Jarak ke Positif (D+)_, pembedanya adalah _pengurang_-nya $A^-$

### Langkah 5: Nilai Preferensi ($V$) & Perankingan

Rumus: $V_i = \frac{D_i^-}{D_i^- + D_i^+}$

1. **L1**: $128 / (128 + 078) = \mathbf{0.621}$
    
2. **L2**: $124 / (124 + 114) = \mathbf{0.521}$
    
3. **L3**: $060 / (060 + 131) = \mathbf{0.314}$
    

### Langkah 6: Interpretasi

Lokasi terbaik adalah L1 (Lokasi A) karena memiliki nilai preferensi tertinggi. Meskipun L2 memiliki luas bangunan terbesar, L1 menang karena biaya sewanya paling rendah dan jaraknya ke pelabuhan cukup ideal (bobot biaya sewa 50% sangat berpengaruh di sini).

---

## 5. Kelebihan dan Keterbatasan TOPSIS
    
**Keterbatasan** metode TOPSIS Beberapa kelemahan dari metode TOPSIS sebagai berikut (Syafnidawaty,2020):
- Belum adanya penentuan bobot prioritas yang menjadi prioritas hitungan terhadap kriteria, yang berguna untuk meningkatkan validitas nilai bobot perhitungan kriteria. Maka dengan alasan ini, metode ini dapat dikombinasikan misalnya dengan metode AHP agar menghasilkanoutput atau keputusan yang lebih maksimal.
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

### 6.2. Keunggulan TOPSIS Dibanding Metode Lain

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

### 6.3. Contoh Kasus di Mana TOPSIS Lebih Optimal

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

**Alasan:** TOPSIS mampu menyeimbangkan risiko dan manfaat secara simultan.

---

### 6.4. Ringkasan Perbandingan Singkat

| Kondisi Utama                          | Metode Paling Optimal |
| -------------------------------------- | --------------------- |
| Kedekatan ke solusi ideal & anti-ideal | **TOPSIS**            |
| Penilaian cepat dan sederhana          | SAW                   |
| Rasio dan perbandingan relatif kuat    | WP                    |
| Penekanan dominasi kriteria            | MPE                   |
| Indeks kinerja agregat                 | CPI                   |

---

## 7. Fuzzy dan Dynamic TOPSIS

 **TOPSIS** yang dirancang untuk memeringkat alternatif berdasarkan kedekatannya dengan solusi ideal positif dan jauhnya dari solusi ideal negatif menggunakan **data numerik yang pasti (crisp)** pada **satu kondisi waktu yang statis**. Pendekatan ini efektif untuk masalah keputusan yang terstruktur dan datanya jelas, namun memiliki keterbatasan ketika penilaian melibatkan **subjektivitas, ketidakpastian, dan penilaian linguistik** dari pengambil keputusan.

Untuk mengatasi keterbatasan tersebut, dikembangkan **Fuzzy TOPSIS**, yang mengintegrasikan **teori himpunan fuzzy** ke dalam kerangka TOPSIS. Dalam pendekatan ini, nilai kriteria dan/atau bobot dapat dinyatakan dalam bentuk **bilangan fuzzy**, sehingga metode menjadi lebih mampu merepresentasikan **ambiguitas dan ketidakpastian penilaian manusia**. Meskipun demikian, Fuzzy TOPSIS masih bersifat **statis**, karena evaluasi keputusan tetap dilakukan pada satu periode waktu.

Tahap perkembangan selanjutnya adalah **Fuzzy Dynamic TOPSIS**, yang memperluas Fuzzy TOPSIS dengan memasukkan **dimensi waktu** ke dalam proses pengambilan keputusan. Metode ini memungkinkan nilai kriteria dan bobot berubah antar periode serta menggabungkan hasil evaluasi secara temporal. Dengan demikian, Fuzzy Dynamic TOPSIS memberikan kerangka keputusan yang **lebih adaptif dan realistis** untuk lingkungan yang **dinamis**, di mana kondisi dan preferensi pengambil keputusan terus berkembang dari waktu ke waktu.

Untuk pembahasan lebih lengkap, check [Fuzzy TOPSIS](topsis-fuzzy.md) dan [Dynamic TOPSIS](topsis-dynamic.md)

---

## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [Template TOPSIS (Google Sheet)](https://docs.google.com/spreadsheets/d/1r7bqRNE9BN5wfxinVUOakH-xIkItPPTRku41_r87VVE/edit?usp=sharing)
 
Modifikasi sheet sesuai kebutuhan

---

## 💼 Diskusi & Tugas

Buat perhitungan pengambilan keputusan menggunakan TOPSIS, menggunakan data pada latihan sebelumnya:

1. [Soal 1 - CPI](cpi.md#soal-1--seleksi-penerima-beasiswa)
2. [Soal 2 - CPI](cpi.md#soal-2--pemilihan-supplier)
3. [Soal 3 - SAW](saw.md#soal-3----pemilihan-lokasi-cabang-restoran-baru)

---
## 📚 Referensi

- Hwang, C. L., & Yoon, K. (1981). _Multiple Attribute Decision Making: Methods and Applications_. Springer.
- Triantaphyllou, E. (2000). _Multi-Criteria Decision Making Methods_. Springer.
- Krzysztof Palczewskia, Wojciech Sałabuna, ” The fuzzy TOPSIS applications in the last decade”., 23rd International Conference on Knowledge-Based and Intelligent Information & Engineering System., 2019
- Ahmad Abdul Chamid., “Penerapan Metode Topsis Untuk Menentukan Prioritas Kondisi Rumah”.,
- Irvan Muzakkir., “Penerapan Metode Topsis untuk Sistem Pendukung Keputusan Penentuan Keluarga Miskin pada Desa Panca Karsa II., Jurnal Ilmu Komputer., Volume 9 Nomor 3 Desember 2017
- Vinay Yadav, Subhankar Karmakar, Pradip P. Kalbar, A.K. Dikshit. “PyTOPS: A Python based tool for TOPSIS., Software X., Volume 9, January–June 2019, Pages 217-222
- Bruno Miranda dos Santos, Leoni Pentiado Godoy, Lucila M.S. Campos., “Performance evaluation of green suppliers using entropy-TOPSIS-F., Journal of Cleaner Production, Volume 207, 10 January 2019, Pages 498-509
- [Metode Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) by Feri Alpiyasin, M.Kom](https://www.canva.com/design/DAG7of6ouEw/jQjx6yC57R9QyDPLgojAWg/edit)