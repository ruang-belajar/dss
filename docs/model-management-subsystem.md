# Model Management Subsystem


## 🧩 **1. Pengertian Model Management Subsystem**

**Model Management Subsystem (MMS)** adalah bagian dari DSS yang:

> bertanggung jawab untuk membuat, menyimpan, mengelola, dan menjalankan berbagai **model analitis atau matematis** yang digunakan untuk membantu pengambilan keputusan.

Jika **Data Management Subsystem** menyediakan *bahan mentah (data)*, maka **Model Management Subsystem** adalah *dapur tempat data tersebut diolah menjadi informasi dan rekomendasi keputusan*.

---

## 🧠 **2. Fungsi Utama Model Management Subsystem**

| Fungsi                                  | Penjelasan                                                                                  |
| --------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Menyediakan model keputusan**         | Menyediakan berbagai jenis model seperti statistik, optimisasi, simulasi, dan prediksi.     |
| **Menjalankan perhitungan analisis**    | Menggunakan data dari Data Management Subsystem untuk menghitung hasil dan rekomendasi.     |
| **Mendukung eksperimen dan simulasi**   | Memungkinkan pengguna mencoba berbagai skenario *“what-if”* untuk melihat dampak keputusan. |
| **Memelihara integritas model**         | Menjaga model agar tetap akurat dan relevan dengan kondisi terkini.                         |
| **Memfasilitasi integrasi antar model** | Menggabungkan beberapa model yang berbeda untuk analisis komprehensif.                      |

---

## 🧱 **3. Komponen Utama Model Management Subsystem**

| Komponen                                | Deskripsi                                                                                        |
| --------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Model Base (Basis Model)**            | Tempat penyimpanan seluruh model matematis, statistik, atau finansial yang digunakan DSS.        |
| **Model Base Management System (MBMS)** | Perangkat lunak yang berfungsi mengelola pembuatan, penyimpanan, modifikasi, dan eksekusi model. |
| **Model Dictionary (Kamus Model)**      | Berisi deskripsi setiap model: nama, fungsi, variabel input/output, dan hubungan antar model.    |
| **Model Execution / Solver**            | Mesin perhitungan yang menjalankan model untuk menghasilkan output keputusan.                    |
| **Model Integration Tools**             | Alat bantu untuk menggabungkan beberapa model (misalnya model keuangan dan model logistik).      |

---

## 💡 **4. Jenis-Jenis Model dalam DSS**

| Jenis Model           | Fungsi / Contoh                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------- |
| **Model Strategis**   | Untuk keputusan jangka panjang — misalnya analisis ekspansi pasar, perencanaan investasi. |
| **Model Taktis**      | Untuk keputusan menengah — seperti perencanaan produksi atau alokasi sumber daya.         |
| **Model Operasional** | Untuk keputusan harian — seperti penjadwalan, pemesanan ulang stok.                       |

Selain itu, model DSS juga bisa diklasifikasikan berdasarkan pendekatan analisis:

| Pendekatan               | Contoh Model                                     |
| ------------------------ | ------------------------------------------------ |
| **Model Statistik**      | Regresi, korelasi, analisis tren.                |
| **Model Optimisasi**     | Linear Programming, Integer Programming.         |
| **Model Simulasi**       | Simulasi Monte Carlo, sistem antrian.            |
| **Model Keuangan**       | Analisis ROI, NPV, IRR, break-even analysis.     |
| **Model Multi-Kriteria** | Analytical Hierarchy Process (AHP), TOPSIS, SAW. |

---

## ⚙️ **5. Alur Kerja Model Management Subsystem**

1. **Input Data:**
   Mengambil data dari **Data Management Subsystem** (database DSS).

2. **Pemilihan Model:**
   Pengguna memilih model yang sesuai dengan jenis keputusan (misalnya model AHP untuk prioritas alternatif).

3. **Eksekusi Model:**
   Model dijalankan menggunakan **Model Execution Engine / Solver**.

4. **Output:**
   Hasil analisis ditampilkan dalam bentuk tabel, grafik, atau rekomendasi di **User Interface Subsystem**.

5. **Analisis “What-If”:**
   Pengguna dapat mengubah variabel input untuk melihat dampak pada hasil keputusan.

---

## 🧪 **6. Contoh Kasus Penerapan**

### 🎯 **Kasus: DSS untuk Perencanaan Produksi di Perusahaan Manufaktur**

**Masalah:**
Menentukan jumlah produksi optimal agar biaya minimum tetapi tetap memenuhi permintaan.

**Komponen yang terlibat:**

* **Data Management Subsystem:** menyimpan data biaya produksi, permintaan pasar, kapasitas mesin.
* **Model Management Subsystem:** menggunakan **Linear Programming Model** untuk mencari kombinasi produksi terbaik.
* **User Interface Subsystem:** menampilkan hasil optimal dalam bentuk grafik biaya vs kapasitas.

**Proses:**

1. Input data → biaya, kapasitas, permintaan.
2. Jalankan model optimisasi.
3. Sistem menghitung dan merekomendasikan hasil produksi optimal.
4. Pengguna dapat melakukan simulasi "what-if" (misalnya jika permintaan naik 10%).

---

## 🧭 **7. Hubungan Model Management dengan Komponen DSS Lain**

| Komponen DSS                                  | Hubungan dengan Model Management                                                     |
| --------------------------------------------- | ------------------------------------------------------------------------------------ |
| **Data Management Subsystem**                 | Menyediakan data input untuk dijalankan dalam model.                                 |
| **User Interface Subsystem**                  | Menampilkan hasil model kepada pengguna (grafik, tabel, dashboard).                  |
| **Communication Subsystem**                   | Memungkinkan kolaborasi antar pengguna dalam memilih model dan menafsirkan hasil.    |
| **Knowledge Management Subsystem (jika ada)** | Menyediakan pengetahuan atau aturan untuk memilih model terbaik berdasarkan konteks. |

---

## 🧾 **8. Contoh Diagram Sederhana**

```
+-----------------------------------+
|        Model Management            |
+-----------------------------------+
| Model Base  |  MBMS  |  Solver    |
+-----------------------------------+
         ↑               ↓
   Data from            Output to
   Data Subsystem   →   User Interface
```

---

## ✅ **9. Kesimpulan**

> **Model Management Subsystem** adalah “otak analitis” dari DSS.
> Ia mengubah data menjadi wawasan melalui berbagai model matematis, statistik, atau simulasi — sehingga manajer dapat mengambil keputusan **berbasis analisis, bukan intuisi semata**.

