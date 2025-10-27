
# Pengolahan Kuisioner Likert

Berikut penjelasan **langkah demi langkah cara mengolah hasil kuisioner skala Likert**, dari tahap awal hingga interpretasi hasilnya 👇

---

## 🧩 **1. Pahami Skala Nilai Likert**

Setiap pilihan jawaban diberi bobot nilai numerik:

|Jawaban|Skor|
|---|---|
|Sangat Tidak Setuju|1|
|Tidak Setuju|2|
|Netral|3|
|Setuju|4|
|Sangat Setuju|5|

> Untuk pernyataan negatif, skor dibalik (misalnya STS=5, SS=1).

---

## 📥 **2. Input Data ke Excel atau SPSS**

Masukkan hasil kuisioner ke dalam tabel.  
Contoh data (5 responden, 3 pertanyaan):

|Responden|Q1|Q2|Q3|
|---|---|---|---|
|R1|4|5|3|
|R2|3|4|4|
|R3|5|5|4|
|R4|2|3|2|
|R5|4|4|3|

---

## 🧮 **3. Hitung Skor Rata-Rata per Pertanyaan**

Rumus di Excel:

```excel
=AVERAGE(B2:B6)
```

**Contoh hasil:**

|Pertanyaan|Rata-rata|
|---|---|
|Q1|3.6|
|Q2|4.2|
|Q3|3.2|

---

## 📊 **4. Interpretasikan Nilai Rata-rata**

Gunakan kategori interpretasi seperti berikut:

|Rentang Skor|Kategori|
|---|---|
|1.00 – 1.79|Sangat Tidak Setuju / Sangat Rendah|
|1.80 – 2.59|Tidak Setuju / Rendah|
|2.60 – 3.39|Netral / Cukup|
|3.40 – 4.19|Setuju / Tinggi|
|4.20 – 5.00|Sangat Setuju / Sangat Tinggi|

**Contoh hasil interpretasi:**

|Pertanyaan|Rata-rata|Interpretasi|
|---|---|---|
|Q1|3.6|Setuju (Tinggi)|
|Q2|4.2|Sangat Setuju (Sangat Tinggi)|
|Q3|3.2|Netral (Cukup)|

---

## 📈 **5. Hitung Skor Total dan Rata-Rata Variabel**

Jika ada beberapa indikator dalam satu variabel, hitung rata-rata gabungannya.

**Contoh:**  
Variabel _Kepuasan Pengguna_ terdiri dari Q1–Q3.

Rumus:

```excel
=AVERAGE(C2:C4)
```

Hasilnya misalnya **3.67 → kategori "Setuju (Tinggi)"**.

---

## 🧠 **6. (Opsional) Uji Validitas & Reliabilitas**

Untuk memastikan data **layak dianalisis**, gunakan:

- **Uji Validitas**: Korelasi Pearson → pastikan _r hitung > r tabel_.
    
- **Uji Reliabilitas**: Cronbach’s Alpha → nilai > 0.7 = reliabel.
    

Ini bisa dilakukan di SPSS atau Python.

---

## 💡 **7. Gunakan dalam Analisis DSS**

Setelah hasil kuisioner diolah:

- Jadikan skor rata-rata tiap variabel sebagai **input** dalam metode DSS seperti:
    
    - **SAW (Simple Additive Weighting)**
        
    - **AHP (Analytic Hierarchy Process)**
        
    - **TOPSIS**, dll.
        
- Misalnya, nilai rata-rata “Kepuasan Pengguna = 4.1” bisa dijadikan **bobot preferensi** untuk keputusan peningkatan sistem.
    

---

## 📘 **Contoh Interpretasi Akhir**

|Variabel|Nilai Rata-Rata|Interpretasi|Keputusan DSS|
|---|---|---|---|
|Kemudahan Penggunaan|4.3|Sangat Tinggi|Pertahankan desain UI|
|Kecepatan Akses|3.6|Tinggi|Optimalkan server|
|Keandalan Sistem|2.8|Cukup|Lakukan perbaikan bug|

---

## 💼 Diskusi & Tugas

Berikut adalah contoh hasil pengisian survei _Kepuasan Pengguna Sistem Informasi Akademik_. 

|No|Pernyataan|R1|R2|R3|R4|R5|
|---|---|---|---|---|---|---|
|1|Sistem mudah digunakan|4|5|4|3|4|
|2|Tampilan sistem menarik dan mudah dibaca|3|4|4|3|4|
|3|Proses login dan akses data cepat|5|4|4|2|4|
|4|Laporan yang dihasilkan sistem akurat|4|5|5|3|5|
|5|Sistem jarang mengalami error|3|4|3|2|4|
🙋‍♂️ Buat analisa dan interpretasi terhadap hasil survei