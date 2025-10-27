
# Pengolahan Kuisioner Semantic Differential

berikut penjelasan **cara mengolah hasil pengisian kuesioner dengan skala _Semantic Differential_** dalam konteks **Decision Support System (DSS)** atau analisis data survei:

---

## 🧩 1. **Konsep Dasar Skala Semantic Differential**

Skala _Semantic Differential_ digunakan untuk **mengukur persepsi, sikap, atau penilaian responden terhadap suatu objek** dengan **dua kutub yang berlawanan** (bipolar).  
Contoh:

|Aspek|Kutub Negatif|Skala|Kutub Positif|
|---|---|---|---|
|Desain Aplikasi|Jelek (1)|2 3 4 5 6 7|Bagus (7)|
|Kecepatan Sistem|Lambat (1)|2 3 4 5 6 7|Cepat (7)|
|Kemudahan|Sulit (1)|2 3 4 5 6 7|Mudah (7)|

Responden memilih angka di antara dua kutub tersebut.

---

## 🧮 2. **Langkah-Langkah Pengolahan Data**

### **Langkah 1: Pengkodean Skor**

Setiap titik pada skala diberi nilai numerik, misalnya 1–7.

- Nilai **rendah (1)** menunjukkan kutub negatif.
    
- Nilai **tinggi (7)** menunjukkan kutub positif.
    

Jika ada pernyataan yang bersifat **terbalik (reverse)**, maka **skor harus dibalik**:

> Contoh: skala "Tidak Ramah (1) – Ramah (7)" berarti 7 = positif.  
> Tapi jika item "Ramah" diubah menjadi "Tidak Ramah", maka pembalikan skor dilakukan (7 → 1, 6 → 2, dst).

---

### **Langkah 2: Hitung Rata-Rata Tiap Aspek**

Setelah semua skor dikodekan, hitung **rata-rata untuk tiap dimensi atau atribut**:  
$\text{Mean Aspek} = \frac{\text{Jumlah skor seluruh responden untuk aspek}}{\text{Jumlah responden}}$

Contoh:

|Aspek|Rata-rata|
|---|---|
|Desain|5.8|
|Kecepatan|4.2|
|Kemudahan|6.1|

---

### **Langkah 3: Interpretasi Hasil**

Gunakan pedoman interpretasi seperti:

|Interval Skor|Kategori|
|---|---|
|1.00 – 2.49|Sangat Negatif|
|2.50 – 3.49|Negatif|
|3.50 – 4.49|Netral|
|4.50 – 5.49|Positif|
|5.50 – 7.00|Sangat Positif|

Hasil rata-rata dapat digunakan untuk menilai **persepsi responden terhadap objek penelitian**.

---

### **Langkah 4: Visualisasi (Opsional)**

Untuk analisis dalam **Decision Support System**, visualisasi dapat membantu interpretasi:

- **Diagram batang (bar chart)** untuk perbandingan antar-aspek.
    
- **Spider/Radar chart** untuk menampilkan profil persepsi secara keseluruhan.
    

---

### **Langkah 5: Analisis Lanjutan (Jika Diperlukan)**

Jika ingin mendalam, bisa dilakukan:

- **Analisis faktor** untuk mengelompokkan atribut.
    
- **Analisis korelasi** untuk melihat hubungan antar-aspek.
    
- **Analisis deskriptif** untuk menggambarkan persepsi umum responden.
    

---

## 📊 Contoh Tabel Olahan

|Responden|Desain|Kecepatan|Kemudahan|
|---|---|---|---|
|R1|6|5|7|
|R2|5|4|6|
|R3|7|3|5|
|**Rata-rata**|**6.0**|**4.0**|**6.0**|

Interpretasi:

- Desain dan kemudahan dinilai **positif**,
    
- Kecepatan sistem perlu **peningkatan (skor 4 = netral)**.
    

---

## 💡 Kesimpulan dalam Konteks DSS

Dalam _Decision Support System_, hasil dari kuesioner _Semantic Differential_ bisa digunakan untuk:

- Menilai **kepuasan pengguna terhadap sistem**,
    
- Membantu **pengambilan keputusan strategis** (misalnya peningkatan fitur atau UI/UX),
    
- Menjadi dasar **prioritas perbaikan sistem** berdasarkan persepsi pengguna.
    

---

## 💼 Diskusi & Tugas

Berikut adalah contoh hasil pengisian survei _Mengukur persepsi pengguna terhadap kualitas sistem informasi internal perusahaan_. 

| Aspek                | R1  | R2  | R3  | R4  | R5  |
| -------------------- | --- | --- | --- | --- | --- |
| Tampilan antarmuka   | 4   | 5   | 6   | 5   | 6   |
| Kecepatan sistem     | 3   | 4   | 5   | 4   | 3   |
| Kemudahan penggunaan | 6   | 6   | 7   | 5   | 6   |
| Keandalan sistem     | 4   | 4   | 5   | 5   | 4   |
| Respons layanan IT   | 5   | 6   | 6   | 5   | 6   |


🙋‍♂️ Buat analisa dan interpretasi terhadap hasil survei