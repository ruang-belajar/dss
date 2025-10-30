
# Pengolahan Kuisioner Guttman

Berikut penjelasan lengkap **cara mengolah hasil pengisian kuesioner dengan skala Guttman** dalam konteks **Decision Support System (DSS)** dan penelitian sistem informasi.

## 🎯 1. Konsep Dasar Skala Guttman

**Skala Guttman** digunakan untuk mengukur sikap atau pendapat responden secara **kumulatif dan tegas (ya/tidak, setuju/tidak setuju)**.  
Artinya, jika seseorang **setuju pada pernyataan dengan tingkat tinggi**, maka **otomatis setuju juga dengan pernyataan di bawahnya**.

Contoh:

|Pernyataan|Respon|
|---|---|
|1. Saya pernah menggunakan sistem DSS.|Ya|
|2. Saya sering menggunakan sistem DSS.|Ya|
|3. Saya mahir menggunakan sistem DSS.|Tidak|

Dari pola di atas, responden berhenti di tingkat ke-2 — artinya tingkat penerimaan berada di **level menengah**.

---

## 🧾 2. Langkah-langkah Pengolahan Data Skala Guttman

### **Langkah 1. Pemberian Skor**

Gunakan nilai **1 = Ya/Setuju** dan **0 = Tidak/ Tidak setuju**.  
Contoh tabel:

|Responden|P1|P2|P3|P4|
|---|---|---|---|---|
|R1|1|1|1|0|
|R2|1|0|0|0|
|R3|1|1|1|1|

---

### **Langkah 2. Menentukan Pola Respon Ideal**

Pola ideal bersifat **kumulatif**, misalnya untuk 4 item:

|Pola Ideal|Interpretasi|
|---|---|
|1111|Tingkat tertinggi|
|1110|Sedikit di bawah tertinggi|
|1100|Menengah|
|1000|Rendah|
|0000|Tidak sama sekali|

---

### **Langkah 3. Menghitung Skor Total per Responden**

Jumlahkan skor setiap responden.

|Responden|P1|P2|P3|P4|Total|
|---|---|---|---|---|---|
|R1|1|1|1|0|**3**|
|R2|1|0|0|0|**1**|
|R3|1|1|1|1|**4**|

---

### **Langkah 4. Menguji Kumulatifitas (Reproducibility Coefficient)**

Untuk memastikan kuesioner benar-benar mengikuti pola Guttman, hitung **Koefisien Reprodusibilitas (CR)**:

$CR = 1 - \frac{\text{Jumlah kesalahan}}{\text{Jumlah item} \times \text{Jumlah responden}}$

- Jika **CR ≥ 0,90**, maka skala dikatakan **valid secara kumulatif**.
    

Contoh:

- Jumlah item = 4
    
- Jumlah responden = 3
    
- Kesalahan (jawaban yang tidak sesuai pola ideal) = 1
    

$CR = 1 - \frac{1}{(4 \times 3)} = 1 - 0,083 = 0,917$

✅ Karena > 0,9 → skala **cukup baik**.

---

### **Langkah 5. Analisis dan Interpretasi**

Gunakan skor total untuk menilai tingkat variabel yang diukur, misalnya:

|Total Skor|Kategori|
|---|---|
|0–1|Rendah|
|2–3|Sedang|
|4|Tinggi|

Misalnya, R3 memiliki skor 4 → **sikap sangat positif terhadap DSS**.

---

## 📊 3. Implementasi di Excel / SPSS

**Di Excel:**

- Gunakan formula `=SUM(B2:E2)` untuk menghitung total skor.
    
- Hitung CR dengan rumus di atas.
    
- Bisa divisualisasikan dengan grafik batang untuk tiap responden.
    

**Di SPSS:**

- Masukkan data (1/0) per item.
    
- Gunakan _Descriptive Statistics → Frequencies_ untuk melihat distribusi.
    
- Untuk uji validitas Guttman, hitung CR secara manual menggunakan syntax atau Excel.
    

---

## 🧠 4. Relevansi dengan Decision Support System

Dalam konteks **DSS**, skala Guttman dapat digunakan untuk:

- Mengukur **tingkat penerimaan pengguna terhadap sistem** (acceptance level).
    
- Menilai **kematangan adopsi teknologi**.
    
- Menentukan **tingkat kesiapan organisasi terhadap penerapan sistem informasi**.
    
---

## 💼 Diskusi & Tugas

Berikut adalah contoh hasil pengisian survei _Mengetahui sejauh mana pegawai menerima dan menggunakan sistem DSS dalam kegiatan pengambilan keputusan._. 

**Pertanyaan:**

|No|Pernyataan|Jawaban (Ya/Tidak)|
|---|---|---|
|P1|Saya mengetahui adanya Sistem Pendukung Keputusan (DSS) di tempat kerja.||
|P2|Saya pernah menggunakan sistem DSS tersebut.||
|P3|Saya sering menggunakan DSS untuk mendukung keputusan kerja saya.||
|P4|Saya merasa terbantu dalam pengambilan keputusan dengan DSS.||
|P5|Saya mampu menggunakan DSS tanpa bantuan orang lain.||

**Contoh Hasil Pengisian oleh 5 Responden**

| Responden | P1  | P2  | P3  | P4  | P5  | Total Skor |
| --------- | --- | --- | --- | --- | --- | ---------- |
| R1        | 1   | 1   | 1   | 1   | 1   | 5          |
| R2        | 1   | 1   | 1   | 0   | 0   | 3          |
| R3        | 1   | 1   | 0   | 0   | 0   | 2          |
| R4        | 1   | 0   | 0   | 0   | 0   | 1          |
| R5        | 1   | 1   | 1   | 1   | 0   | 4          |

🙋‍♂️ Buat analisa dan interpretasi terhadap hasil survei