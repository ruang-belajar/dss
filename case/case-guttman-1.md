## 📋 **Contoh Kasus: Tingkat Penerimaan Pengguna terhadap Sistem Pendukung Keputusan (DSS)**


## 🧾 **Kuesioner Skala Guttman**

**Petunjuk:**  
Jawab setiap pernyataan dengan **“Ya” (1)** jika setuju, dan **“Tidak” (0)** jika tidak setuju.

|No|Pernyataan|Jawaban (Ya/Tidak)|
|---|---|---|
|P1|Saya mengetahui adanya Sistem Pendukung Keputusan (DSS) di tempat kerja.||
|P2|Saya pernah menggunakan sistem DSS tersebut.||
|P3|Saya sering menggunakan DSS untuk mendukung keputusan kerja saya.||
|P4|Saya merasa terbantu dalam pengambilan keputusan dengan DSS.||
|P5|Saya mampu menggunakan DSS tanpa bantuan orang lain.||

---

## 📊 **Contoh Hasil Pengisian oleh 5 Responden**

|Responden|P1|P2|P3|P4|P5|Total Skor|
|---|---|---|---|---|---|---|
|R1|1|1|1|1|1|5|
|R2|1|1|1|0|0|3|
|R3|1|1|0|0|0|2|
|R4|1|0|0|0|0|1|
|R5|1|1|1|1|0|4|

---

## 🔍 **Langkah Analisis**

### 1️⃣ **Menentukan Pola Ideal (Kumulatif)**

Karakteristik Guttman bersifat kumulatif, artinya:

> Jika responden menjawab “Ya” pada item ke-n, maka seharusnya “Ya” juga untuk item sebelumnya.

Pola ideal:

|Pola|Makna|
|---|---|
|11111|Sangat menerima DSS|
|11110|Menerima tinggi|
|11100|Sedang|
|11000|Rendah|
|10000|Sangat rendah|

---

### 2️⃣ **Hitung Jumlah Kesalahan (Error)**

Kesalahan = jawaban yang tidak sesuai pola ideal.

Contoh:

- R2: pola `11100` → sesuai
    
- R5: pola `11110` → sesuai
    
- R3: pola `11000` → sesuai
    
- R4: pola `10000` → sesuai
    
- R1: `11111` → sesuai  
    ✅ Tidak ada kesalahan → Error = 0
    

---

### 3️⃣ **Hitung Koefisien Reprodusibilitas (CR)**

[  
CR = 1 - \frac{\text{Jumlah kesalahan}}{\text{Jumlah item} \times \text{Jumlah responden}}  
]

[  
CR = 1 - \frac{0}{5 \times 5} = 1 - 0 = 1,00  
]

✅ Karena **CR = 1.00 ≥ 0.90**, maka skala **Guttman valid dan konsisten**.

---

### 4️⃣ **Interpretasi Skor**

|Total Skor|Kategori|
|---|---|
|0–1|Sangat Rendah|
|2–3|Sedang|
|4|Tinggi|
|5|Sangat Tinggi|

**Hasil:**

- R1: Sangat tinggi
    
- R2: Sedang
    
- R3: Sedang
    
- R4: Rendah
    
- R5: Tinggi
    

---

## 💡 **Kesimpulan**

Dari hasil di atas, dapat disimpulkan bahwa **mayoritas responden memiliki penerimaan sedang hingga tinggi terhadap DSS**.  
Skala Guttman efektif untuk mengukur tingkat kematangan penerimaan karena menunjukkan pola sikap yang tegas dan konsisten.
