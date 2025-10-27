# 🎓 Statistik Parametrik dan Nonparametrik


---

## 🧠 **1. Pengantar: Statistik dalam DSS**

**Decision Support System (DSS)** menggunakan **analisis statistik** untuk membantu pengambil keputusan memahami data, mengenali pola, dan memprediksi hasil.

Analisis statistik dalam DSS dapat dikelompokkan menjadi dua pendekatan utama:

- **Statistik Parametrik**, dan
    
- **Statistik Nonparametrik.**
    

Kedua pendekatan ini digunakan sesuai dengan **jenis data** dan **asumsi tentang populasi** yang dianalisis.

---

## ⚙️ **2. Statistik Parametrik**

### 📘 **Definisi:**

Statistik parametrik adalah metode analisis statistik yang **mengasumsikan bahwa data berasal dari populasi dengan distribusi tertentu**, biasanya **distribusi normal**.  
Metode ini menggunakan **parameter populasi** seperti **mean (rata-rata)** dan **standard deviation (simpangan baku)** untuk membuat kesimpulan.

---

### 📊 **Ciri-Ciri Statistik Parametrik:**

|Aspek|Penjelasan|
|---|---|
|**Asumsi Distribusi**|Data harus berdistribusi **normal**.|
|**Jenis Data**|Menggunakan data **interval** atau **rasio**.|
|**Parameter yang digunakan**|Menggunakan parameter populasi seperti **mean, variance, standard deviation**.|
|**Tujuan utama**|Menguji hipotesis tentang parameter populasi.|
|**Ketelitian**|Lebih sensitif dan efisien jika asumsi terpenuhi.|

---

### 🔹 **Contoh Uji Parametrik:**

|Jenis Uji|Tujuan|Contoh Penggunaan dalam DSS|
|---|---|---|
|**t-test**|Membandingkan rata-rata dua kelompok|Menguji apakah kepuasan pengguna DSS berbeda antara dua divisi.|
|**ANOVA (Analysis of Variance)**|Membandingkan rata-rata lebih dari dua kelompok|Menilai perbedaan efisiensi DSS di tiga cabang perusahaan.|
|**Pearson Correlation**|Mengukur hubungan linear antar variabel|Hubungan antara waktu penggunaan DSS dan peningkatan produktivitas.|
|**Regression Analysis**|Memprediksi variabel dependen berdasarkan independen|Memprediksi permintaan barang berdasarkan data historis.|

---

### ✅ **Kelebihan Statistik Parametrik:**

- Lebih **tepat dan efisien** jika asumsi normalitas terpenuhi.
    
- Dapat digunakan untuk **prediksi dan generalisasi populasi**.
    
- Memberikan hasil yang **kuantitatif dan terukur**.
    

### ❌ **Kelemahan:**

- **Tidak cocok** untuk data ordinal atau nominal.
    
- Hasil bisa **tidak valid** jika asumsi distribusi normal dilanggar.
    
- Rentan terhadap **outlier** (data ekstrem).
    

---

## ⚙️ **3. Statistik Nonparametrik**

### 📘 **Definisi:**

Statistik nonparametrik adalah metode analisis statistik yang **tidak bergantung pada asumsi distribusi tertentu**.  
Metode ini sering digunakan ketika:

- Data tidak berdistribusi normal,
    
- Jumlah sampel kecil, atau
    
- Data berskala **nominal** dan **ordinal**.
    

---

### 📊 **Ciri-Ciri Statistik Nonparametrik:**

|Aspek|Penjelasan|
|---|---|
|**Asumsi Distribusi**|Tidak membutuhkan asumsi distribusi normal.|
|**Jenis Data**|Dapat digunakan untuk data **nominal** dan **ordinal**.|
|**Tujuan utama**|Menguji perbedaan atau hubungan tanpa parameter populasi.|
|**Ketelitian**|Kurang sensitif, tapi lebih fleksibel.|
|**Teknik Analisis**|Berdasarkan **peringkat (ranking)** atau **frekuensi**.|

---

### 🔹 **Contoh Uji Nonparametrik:**

|Jenis Uji|Tujuan|Contoh Penggunaan dalam DSS|
|---|---|---|
|**Chi-Square Test**|Menguji hubungan antar variabel kategori|Apakah penggunaan DSS dipengaruhi oleh tingkat pendidikan pengguna?|
|**Mann-Whitney U Test**|Menguji perbedaan dua kelompok independen|Membandingkan tingkat kepuasan pengguna DSS pria dan wanita.|
|**Kruskal-Wallis Test**|Alternatif nonparametrik untuk ANOVA|Menguji perbedaan persepsi terhadap DSS di tiga cabang.|
|**Spearman Rank Correlation**|Mengukur hubungan berdasarkan peringkat|Hubungan antara kepuasan pengguna dan frekuensi penggunaan DSS.|
|**Wilcoxon Signed Rank Test**|Menguji perbedaan dua sampel berpasangan|Menilai perubahan kepuasan pengguna sebelum dan sesudah pembaruan DSS.|

---

### ✅ **Kelebihan Statistik Nonparametrik:**

- **Tidak memerlukan asumsi distribusi normal.**
    
- Cocok untuk **data kualitatif (nominal, ordinal)**.
    
- **Fleksibel** terhadap data yang tidak memenuhi asumsi statistik klasik.
    
- Dapat digunakan pada **sampel kecil.**
    

### ❌ **Kelemahan:**

- Kurang efisien dibandingkan uji parametrik jika data normal.
    
- Tidak memberikan informasi detail seperti rata-rata populasi.
    
- Kadang hasilnya **kurang presisi**.
    

---

## ⚖️ **4. Perbandingan Parametrik dan Nonparametrik**

|Aspek|Statistik Parametrik|Statistik Nonparametrik|
|---|---|---|
|**Asumsi Distribusi**|Mengasumsikan distribusi normal|Tidak memerlukan distribusi tertentu|
|**Jenis Data**|Interval / Rasio|Nominal / Ordinal|
|**Ukuran Sampel**|Relatif besar|Dapat digunakan pada sampel kecil|
|**Ketelitian**|Lebih sensitif dan presisi|Kurang sensitif namun fleksibel|
|**Contoh Uji**|t-test, ANOVA, Pearson, Regresi|Chi-Square, Mann-Whitney, Kruskal-Wallis, Spearman|
|**Contoh Penggunaan dalam DSS**|Analisis performa sistem, prediksi, peramalan|Analisis kepuasan pengguna, evaluasi preferensi|

---

## 🧩 **5. Penerapan Statistik dalam DSS**

Dalam **Decision Support System**, statistik parametrik dan nonparametrik digunakan untuk membantu berbagai analisis:

|Jenis Analisis|Metode Statistik|Tujuan dalam DSS|
|---|---|---|
|**Analisis Kinerja Sistem**|ANOVA, t-test|Membandingkan kinerja DSS di berbagai unit.|
|**Analisis Kepuasan Pengguna**|Chi-square, Spearman|Mengukur hubungan faktor demografis dengan kepuasan.|
|**Peramalan dan Prediksi**|Regresi Linear, Time Series|Memprediksi tren penjualan atau permintaan.|
|**Pemeringkatan Alternatif Keputusan**|Rank Correlation, Kruskal-Wallis|Menentukan alternatif terbaik berdasarkan preferensi pengguna.|

---

## 📈 **6. Contoh Kasus Sederhana**

### 🧮 **Kasus:**

Sebuah perusahaan ingin mengetahui apakah penggunaan **Sistem DSS baru** berpengaruh terhadap peningkatan efisiensi kerja.

### 📊 **Langkah Analisis:**

1. **Kumpulkan data waktu kerja** sebelum dan sesudah DSS digunakan (dalam jam).
    
2. Jika data **berdistribusi normal** → gunakan **Paired t-test (parametrik)**.
    
3. Jika data **tidak normal** atau skala ordinal → gunakan **Wilcoxon Signed Rank Test (nonparametrik)**.
    

Kedua hasil uji tersebut membantu manajemen menentukan **apakah penerapan DSS benar-benar memberikan dampak signifikan.**

---

## 🧭 **7. Kesimpulan**

> Baik **statistik parametrik** maupun **nonparametrik** merupakan alat analisis penting dalam DSS.  
> Pemilihan metode bergantung pada **jenis data**, **ukuran sampel**, dan **asumsi distribusi populasi.**

- Gunakan **parametrik** jika data memenuhi asumsi normal dan berskala interval/rasio.
    
- Gunakan **nonparametrik** jika data tidak memenuhi asumsi atau berskala nominal/ordinal.
    

Dengan memahami kedua pendekatan ini, pengambil keputusan dapat:

- Melakukan analisis yang **lebih akurat**,
    
- Meminimalkan kesalahan interpretasi, dan
    
- Meningkatkan **efektivitas sistem pendukung keputusan.**
    

---

## 🧩 **8. Latihan / Tugas Mahasiswa**

1. Jelaskan perbedaan mendasar antara statistik parametrik dan nonparametrik.
    
2. Sebutkan contoh kasus nyata di mana **statistik nonparametrik** lebih tepat digunakan dalam DSS.
    
3. Buat simulasi kecil (menggunakan Excel atau SPSS) untuk menguji perbedaan rata-rata dua kelompok menggunakan **t-test** dan **Mann-Whitney Test**, lalu bandingkan hasilnya.
    
