## **Perbandingan Contoh Kasus dan Metode Sistem Pendukung Keputusan**


## **1. Tinjauan Singkat Metode DSS**

1.1 AHP (Analytic Hierarchy Process)**
- Berbasis perbandingan berpasangan
- Menghasilkan bobot kriteria
- Memiliki uji konsistensi (CR)

**Kelebihan:** Cocok untuk data kualitatif dan pendapat pakar.  
**Keterbatasan:** Perhitungan membesar secara eksponensial jika alternatif sangat banyak.

---

### 1.2 Weighted Product (WP)**

- Menggunakan operasi perkalian berbobot
- Semua nilai alternatif dibandingkan dalam bentuk rasio relatif

**Kelebihan:** Cocok untuk data kuantitatif dan skala besar.  
**Keterbatasan:** Sensitif terhadap bobot.

---

### 1.3 Simple Additive Weighting (SAW)**

- Menggunakan normalisasi linear
- Nilai akhir adalah penjumlahan berbobot

**Kelebihan:** Sederhana, paling banyak digunakan.  
**Keterbatasan:** Hasil sangat bergantung pada metode normalisasi.

---

### **1.4 Profile Matching**

- Mengukur gap antara kompetensi aktual dan standar
- Menggunakan bobot Core Factor (CF) dan Secondary Factor (SF)

**Kelebihan:** Sangat cocok untuk seleksi karyawan.  
**Keterbatasan:** Membutuhkan standar kompetensi yang jelas.

---

### 1.5 Metode Perbandingan Eksponensial (MPE)**

- Menggunakan skala eksponensial untuk memberi pembeda lebih besar
- Cocok ketika nilai antar alternatif sangat dekat

**Kelebihan:** Memberikan diferensiasi kuat.  
**Keterbatasan:** Sulit dijelaskan pada pemangku kepentingan awam.

---

### **1.6 Composite Performance Index (CPI)**

- Menggabungkan berbagai indikator kinerja menjadi satu indeks
- Biasa digunakan dalam manajemen kinerja

**Kelebihan:** Sangat intuitif untuk dashboard manajerial.  
**Keterbatasan:** Perlu struktur indikator yang baik.

---

### **1.7 TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)**

- Berdasarkan jarak ke solusi ideal dan anti-ideal
- Menentukan alternatif dengan jarak terdekat ke titik ideal

**Kelebihan:** Kuat untuk data kuantitatif banyak kriteria.  
**Keterbatasan:** Sensitif terhadap skala data.

---

### **1.8 ARAS (Additive Ratio Assessment)**

- Mengukur utilitas relatif terhadap alternatif optimal
- Menggunakan penjumlahan nilai ter-normalisasi

**Kelebihan:** Konsep utilitas sangat jelas.  
**Keterbatasan:** Tidak sepopuler TOPSIS tapi hasil sangat stabil.

---

### **1.9 MOORA (Multi-Objective Optimization by Ratio Analysis)**

- Memisahkan benefit dan cost
- Rasio normalisasi menghasilkan peringkat akhir

**Kelebihan:** Perhitungan cepat dan sangat stabil.  
**Keterbatasan:** Interpretasi bagi pemula sedikit abstrak.

---

## **2. Contoh Kasus DSS dan Metode yang Tepat**

|Jenis Kasus|Contoh Detail|Metode yang Paling Tepat|Alasan|
|---|---|---|---|
|Seleksi karyawan|Memilih kandidat posisi supervisor|Profile Matching, SAW|Kompetensi dapat dibandingkan dengan standar|
|Seleksi vendor|Pembelian bahan baku|AHP, TOPSIS, MOORA|Melibatkan pakar dan kriteria kuantitatif|
|Penilaian kinerja|Evaluasi unit atau departemen|CPI, AHP|CPI menghasilkan indeks komposit|
|Pemilihan produk|Smartphone terbaik|WP, SAW, TOPSIS|Banyak kriteria kuantitatif|
|Prioritas risiko|Risiko proyek konstruksi|AHP, TOPSIS|AHP untuk bobot, TOPSIS untuk perankingan|
|Pemilihan lokasi|Lokasi gudang|AHP, SAW|Perlu perbandingan kriteria strategis|
|Optimasi multiobjektif|Pemilihan material teknik|MOORA|Rasio benefit–cost stabil|
|Kasus nilai mirip|Alternatif hampir sama nilainya|MPE|Memperkuat perbedaan nilai|
|Evaluasi strategi|Strategi pemasaran|ARAS|Utilitas relatif langsung terlihat|

---

## **3. Tabel Ringkas Pemilihan Metode**

|Metode|Cocok Untuk|Tidak Cocok Untuk|
|---|---|---|
|**AHP**|Penentuan bobot; kriteria kualitatif|Data besar dengan banyak alternatif|
|**WP**|Data numerik dan berskala besar|Data yang tidak rasional atau kualitatif|
|**SAW**|Perhitungan cepat, umum|Kasus dengan varians data ekstrim|
|**Profile Matching**|HR dan gap kompetensi|Penilaian non-kompetensi|
|**MPE**|Kasus nilai sangat dekat|Data kualitatif|
|**CPI**|Kinerja komposit|Kasus pemilihan alternatif|
|**TOPSIS**|Banyak kriteria kuantitatif|Data tidak terstandardisasi|
|**ARAS**|Evaluasi optimalitas|Data kualitatif dominan|
|**MOORA**|Multi-objektif benefit & cost|Kasus deskriptif kualitatif|

---

## **4. Pedoman Memilih Metode DSS**

### **Pertanyaan Kunci:**

1. **Apakah ada standar kompetensi?**  
    Gunakan Profile Matching.
    
2. **Apakah kriteria berasal dari pendapat pakar?**  
    Gunakan AHP.
    
3. **Apakah datanya numerik/kuantitatif?**  
    Pilih SAW, WP, TOPSIS, ARAS, atau MOORA.
    
4. **Apakah nilai antar alternatif mirip?**  
    Gunakan MPE.
    
5. **Apakah ingin menghitung jarak dari solusi ideal?**  
    Gunakan TOPSIS.
    
6. **Apakah ingin membuat indeks kinerja?**  
    Gunakan CPI.
    

---

## **5. Studi Kasus Singkat**

### **Kasus: Pemilihan Supplier Bahan Baku**

**Kriteria:** Harga (cost), kualitas (benefit), ketepatan pengiriman (benefit), layanan purna jual (benefit)  
**Alternatif:** A1, A2, A3

Metode yang dapat digunakan:

- **AHP** untuk menentukan bobot kriteria (karena melibatkan pakar)
    
- **TOPSIS** untuk perankingan terbaik
    
- **MOORA/ARAS** sebagai alternatif yang lebih efisien
    
- **WP/SAW** untuk versi perhitungan sederhana
    

---

## **6. Kesimpulan**

- Tidak ada metode DSS yang paling baik untuk semua kasus.
    
- Pemilihan metode harus menyesuaikan **karakteristik data**, **tujuan analisis**, dan **kebutuhan pengambil keputusan**.
    
- Kombinasi metode sering kali menghasilkan hasil yang lebih kuat (misalnya AHP untuk bobot + TOPSIS untuk ranking).
    
