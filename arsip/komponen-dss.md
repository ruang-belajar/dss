# Komponen Decision Support System (DSS)

---

## 🎯 **Tujuan Pembelajaran**

Setelah mempelajari bab ini, mahasiswa diharapkan mampu:

1. Menjelaskan komponen utama dalam Decision Support System (DSS).
    
2. Memahami fungsi dan hubungan antar komponen DSS.
    
3. Mengidentifikasi bagaimana setiap komponen bekerja mendukung proses pengambilan keputusan.
    

---

## 🧭 **1. Pengantar**

Decision Support System (DSS) tidak hanya sekadar aplikasi untuk menampilkan data, tetapi merupakan **sistem terpadu** yang menggabungkan **data, model analisis, dan antarmuka pengguna** agar proses pengambilan keputusan menjadi efektif.

Menurut Turban et al. (2014), DSS terdiri dari **tiga komponen utama** dan beberapa **komponen tambahan**:

1. **Data Management Subsystem**
    
2. **Model Management Subsystem**
    
3. **User Interface Subsystem**  
    (+ opsional: **Knowledge Base** dan **Communication Subsystem**)
    

---

## 🧩 **2. Komponen Utama DSS**

---

### 🗃️ **2.1 Data Management Subsystem (Subsistem Manajemen Data)**

#### 🔹 Pengertian:

Merupakan komponen yang **mengelola semua data** yang digunakan dalam pengambilan keputusan, baik dari sumber internal maupun eksternal organisasi.

#### 🔹 Fungsi:

- Menyimpan data dalam **database terpusat (DSS Database)**.
    
- Mengambil data yang relevan sesuai permintaan pengguna.
    
- Mengelola **metadata** (data tentang data), seperti sumber, format, dan struktur data.
    
- Memastikan **kualitas, konsistensi, dan integritas** data.
    

#### 🔹 Komponen Pendukung:

- **Database DSS:** berisi data transaksi, data historis, data eksternal (misalnya data pasar).
    
- **DBMS (Database Management System):** sistem untuk mengatur penyimpanan dan akses data.
    
- **Data Directory:** tempat penyimpanan metadata.
    

#### 🔹 Contoh:

Dalam sistem DSS penjualan, subsistem ini mengelola data penjualan per wilayah, produk, dan periode waktu.

---

### 📊 **2.2 Model Management Subsystem (Subsistem Manajemen Model)**

#### 🔹 Pengertian:

Komponen yang menyediakan **model analisis, algoritma, atau perhitungan matematis/statistik** untuk membantu pengambil keputusan melakukan analisis data.

#### 🔹 Fungsi:

- Menyediakan **model-model keputusan**, seperti:
    
    - Model statistik (regresi, korelasi, forecasting)
        
    - Model optimisasi (linear programming)
        
    - Model simulasi (Monte Carlo, scenario analysis)
        
- Mengatur **eksekusi model**, termasuk input, proses, dan output.
    
- Memungkinkan pengguna **memodifikasi model** sesuai kebutuhan.
    

#### 🔹 Komponen Pendukung:

- **Model Base:** kumpulan model yang digunakan.
    
- **Model Base Management System (MBMS):** perangkat lunak pengelola model.
    
- **Model Dictionary:** informasi tentang model (tujuan, variabel, batasan).
    

#### 🔹 Contoh:

Manajer ingin menentukan kombinasi produk yang menghasilkan keuntungan maksimum. Model management akan menjalankan **model optimisasi (linear programming)** untuk menemukan solusi terbaik berdasarkan data penjualan.

---

### 💬 **2.3 User Interface Subsystem (Subsistem Antarmuka Pengguna)**

#### 🔹 Pengertian:

Merupakan **komponen penghubung antara pengguna dengan sistem DSS**.  
User Interface (UI) memungkinkan pengguna untuk berinteraksi, memasukkan data, menjalankan model, dan menampilkan hasil analisis secara visual.

#### 🔹 Fungsi:

- Menyediakan **antarmuka grafis (GUI)** untuk memudahkan interaksi.
    
- Menampilkan **hasil analisis dan laporan** dalam bentuk tabel, grafik, dashboard, atau visualisasi interaktif.
    
- Memungkinkan pengguna **melakukan skenario “what-if analysis”** (misalnya: “Bagaimana jika harga naik 10%?”).
    
- Menyediakan **menu, form input, dan tombol interaksi**.
    

#### 🔹 Contoh:

Dashboard Power BI atau Tableau yang memungkinkan manajer memilih parameter analisis dan langsung melihat hasil simulasi dalam bentuk grafik.

---

## 🤖 **3. Komponen Tambahan DSS (Opsional)**

Selain tiga komponen utama, DSS modern sering dilengkapi dengan dua subsistem tambahan:

---

### 🧠 **3.1 Knowledge-Based Subsystem (Basis Pengetahuan)**

#### 🔹 Pengertian:

Komponen yang berisi **pengetahuan atau aturan (rules)** yang dikumpulkan dari para ahli untuk membantu dalam proses pengambilan keputusan.

#### 🔹 Fungsi:

- Menyediakan **rekomendasi cerdas** berdasarkan pengetahuan yang disimpan.
    
- Mendukung **penalaran (reasoning)** seperti sistem pakar (expert system).
    
- Menggunakan teknologi **Artificial Intelligence (AI)** seperti _rule-based system_ atau _machine learning_.
    

#### 🔹 Contoh:

Dalam DSS medis, sistem dapat memberikan saran diagnosis berdasarkan gejala pasien dan pengetahuan dokter yang telah disimpan sebelumnya.

---

### 🧑‍🤝‍🧑 **3.2 Communication Subsystem (Subsistem Komunikasi)**

#### 🔹 Pengertian:

Komponen yang mendukung **kolaborasi dan komunikasi** antar pengguna dalam proses pengambilan keputusan kelompok (Group DSS).

#### 🔹 Fungsi:

- Menghubungkan beberapa pengguna DSS dalam jaringan (lokal atau online).
    
- Memfasilitasi **rapat virtual, diskusi, atau voting** dalam kelompok pengambil keputusan.
    
- Mendukung **GDSS (Group Decision Support System)**.
    

#### 🔹 Contoh:

Sistem DSS berbasis web yang memungkinkan beberapa manajer dari cabang berbeda bekerja sama dalam menentukan strategi perusahaan.

---

## 🔄 **4. Hubungan Antar Komponen DSS**

Diagram hubungan sederhana:

```
         +------------------------+
         |   User Interface (UI)  |
         +-----------+------------+
                     |
                     v
   +-----------------+-----------------+
   |     Model Management Subsystem    |
   +-----------------+-----------------+
                     |
                     v
   +-----------------+-----------------+
   |     Data Management Subsystem     |
   +-----------------------------------+
```

📌 Alur proses:

1. Pengguna berinteraksi dengan **User Interface**.
    
2. UI mengirimkan permintaan ke **Model Management** untuk melakukan analisis.
    
3. Model Management mengambil data dari **Data Management**.
    
4. Hasil analisis dikirim kembali ke UI untuk ditampilkan kepada pengguna.
    

---

## 🧮 **5. Contoh Kasus Sederhana**

**Kasus:** Seorang manajer ingin mengetahui strategi harga yang optimal untuk meningkatkan laba.

- **Data Management:** Menyediakan data historis penjualan, harga, dan biaya produksi.
    
- **Model Management:** Menggunakan model regresi untuk memprediksi dampak perubahan harga terhadap laba.
    
- **User Interface:** Menampilkan grafik hubungan antara harga dan laba, serta memungkinkan simulasi “what-if”.
    
- **Knowledge Base (opsional):** Memberikan saran berdasarkan pengalaman manajer sebelumnya.
    

---

## 💡 **6. Ringkasan**

|Komponen|Fungsi Utama|Contoh Implementasi|
|---|---|---|
|Data Management|Mengelola dan menyediakan data|Database penjualan, SQL, Data Warehouse|
|Model Management|Menjalankan analisis dan simulasi|Excel Solver, R, Python|
|User Interface|Menyediakan interaksi dan visualisasi|Dashboard, GUI, Web App|
|Knowledge Base (opsional)|Menyimpan aturan dan pengetahuan|Sistem pakar|
|Communication Subsystem (opsional)|Mendukung kolaborasi antar pengguna|GDSS, Google Workspace|

---

## 📘 **Referensi**

- Turban, E., Aronson, J. E., & Liang, T.-P. (2014). _Decision Support Systems and Intelligent Systems._ Pearson.
    
- Marakas, G. M. (2003). _Decision Support Systems in the 21st Century._ Prentice Hall.
    
- Power, D. J. (2011). _Decision Support, Analytics, and Business Intelligence._
    

---

Apakah Anda ingin saya lanjutkan **membuat versi PowerPoint (slide visual)** untuk materi _Komponen DSS_ ini — lengkap dengan diagram, tabel, dan contoh visual (misalnya alur kerja DSS)?