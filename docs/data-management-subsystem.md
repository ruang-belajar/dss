# Data Management Subsystem


## 🧩 **1. Pengertian Data Management Subsystem**

**Data Management Subsystem** adalah **komponen DSS yang bertanggung jawab untuk mengelola, menyimpan, dan menyediakan data** yang dibutuhkan dalam proses pengambilan keputusan.

➡️ Fungsinya mirip “**mesin penyedia bahan bakar data**” bagi DSS — semua analisis, model, dan keputusan didasarkan pada data yang diatur di sini.

---

## 🧠 **2. Fungsi Utama Data Management Subsystem**

|Fungsi|Penjelasan|
|---|---|
|**Menyimpan data**|Menyimpan data internal (penjualan, biaya, inventori) dan eksternal (pasar, ekonomi, pesaing).|
|**Mengintegrasikan data**|Menggabungkan data dari berbagai sumber agar konsisten dan siap digunakan.|
|**Memelihara kualitas data**|Menjamin data yang digunakan akurat, mutakhir, dan bebas duplikasi.|
|**Menyediakan akses cepat**|Memberikan akses kepada pengguna DSS untuk mengambil, memfilter, dan menampilkan data sesuai kebutuhan analisis.|
|**Mendukung pengambilan keputusan**|Menyediakan data terstruktur bagi Model Management Subsystem untuk proses analisis, simulasi, atau prediksi.|

---

## 🧱 **3. Komponen Utama Data Management Subsystem**

Data Management Subsystem biasanya terdiri dari beberapa bagian berikut:

|Komponen|Deskripsi|
|---|---|
|**Database DSS (Decision Support Database)**|Kumpulan data yang relevan dengan keputusan — bisa mencakup data historis, transaksi, dan ringkasan agregat.|
|**Database Management System (DBMS)**|Perangkat lunak yang digunakan untuk membuat, memelihara, dan mengelola basis data DSS. Contohnya: MySQL, SQL Server, Oracle, PostgreSQL.|
|**Data Directory / Data Dictionary**|Kamus data yang menjelaskan sumber, format, dan makna setiap elemen data di dalam sistem.|
|**Query Tools (Alat Pengambil Data)**|Antarmuka yang memungkinkan pengguna mengambil data menggunakan bahasa seperti SQL atau melalui tampilan GUI (drag & drop).|
|**Data Integration Tools**|Menyatukan data dari berbagai sumber (ERP, CRM, sensor IoT, laporan keuangan, dll).|
|**ETL (Extract, Transform, Load)**|Proses untuk mengekstrak data dari sumber, mentransformasikannya agar sesuai format, dan memuatnya ke dalam database DSS.|

---

## 💡 **4. Contoh Alur Kerja Data Management Subsystem**

1. **Pengumpulan Data**
    
    - Dari sistem internal: penjualan, inventori, laporan keuangan.
        
    - Dari sumber eksternal: harga pasar, data ekonomi, tren industri.
        
2. **Integrasi & Pembersihan Data (ETL)**
    
    - Data yang dikumpulkan diproses agar konsisten dan bebas kesalahan.
        
3. **Penyimpanan dalam Database DSS**
    
    - Data disimpan secara terstruktur dalam warehouse atau mart.
        
4. **Akses oleh DSS**
    
    - Komponen lain seperti **Model Management Subsystem** menggunakan data ini untuk menjalankan analisis (misalnya forecasting, optimisasi).
        

---

## 🧪 **5. Contoh Penerapan Nyata**

### 🎯 **Kasus: DSS untuk Perencanaan Produksi**

**Situasi:**  
Sebuah perusahaan manufaktur menggunakan DSS untuk menentukan jumlah produksi optimal setiap bulan.

**Peran Data Management Subsystem:**

- Mengumpulkan data penjualan 3 tahun terakhir.
    
- Menyimpan data biaya produksi, ketersediaan bahan baku, dan permintaan pasar.
    
- Menyediakan data kepada **Model Management Subsystem** yang menjalankan model prediksi permintaan (forecasting).
    
- Memberikan hasil data yang divisualisasikan ke **User Interface Subsystem** dalam bentuk grafik tren dan rekomendasi jumlah produksi.
    

---

## ⚙️ **6. Hubungan dengan Subsystem Lain**

|Subsystem|Hubungan dengan Data Management|
|---|---|
|**Model Management Subsystem**|Menggunakan data untuk menjalankan model analitis dan simulasi.|
|**User Interface Subsystem**|Menampilkan data dan hasil analisis dalam bentuk tabel, grafik, dashboard.|
|**Knowledge Management Subsystem (jika ada)**|Mengambil data sebagai dasar pembelajaran atau inferensi.|
|**Communication Subsystem**|Mengizinkan pengguna berbagi data dan hasil analisis antar tim.|

---

## 🧾 **7. Contoh Struktur Teknis Sederhana**

```
Data Sources
   ↓
[ ETL Process ]
   ↓
Decision Support Database
   ↓
[ DBMS + Data Dictionary ]
   ↓
Query Tools / Model Subsystem / UI
```

---

## 🧩 **8. Kesimpulan**

> **Data Management Subsystem** adalah tulang punggung DSS yang memastikan semua keputusan diambil berdasarkan **data yang relevan, akurat, dan terintegrasi**.  
> Tanpa komponen ini, DSS tidak akan mampu menghasilkan informasi yang andal.

---

Apakah Anda ingin saya bantu **buatkan slide visual (PowerPoint)** berisi diagram arsitektur _Data Management Subsystem dalam DSS_ agar mudah dijelaskan ke mahasiswa?