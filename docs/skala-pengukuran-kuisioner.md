# Skala Pengukuran Kuesioner
 

Dalam sistem pendukung keputusan (_Decision Support System_), data yang digunakan sering berasal dari **penilaian subjektif pengguna** — misalnya persepsi, kepuasan, atau preferensi terhadap alternatif keputusan.  
Untuk memperoleh data tersebut secara terukur, digunakan **instrumen kuesioner dengan berbagai jenis skala pengukuran**.

Jenis skala pengukuran menentukan bagaimana:
- Pertanyaan disusun,    
- Jawaban diberi bobot, dan    
- Hasil diinterpretasikan untuk analisis dalam DSS.
    
Berikut beberapa skala pengukuran yang biasa digunakan untuk mengolah data kuisioner:
- Skala Likert    
- Skala Guttman    
- Skala Semantic Differential    
- Skala Rating (Numerical Rating)    
- Skala Thurstone

---

## 1. Skala Likert

#### 📘 Definisi:

Skala Likert digunakan untuk **mengukur sikap, pendapat, atau persepsi** seseorang terhadap suatu objek dengan **rentang jawaban berurutan dari sangat negatif ke sangat positif.**

#### 💡 Contoh:

> “Sistem DSS membantu saya dalam mengambil keputusan yang lebih baik.”

|Pilihan Jawaban|Nilai|
|---|---|
|Sangat Tidak Setuju|1|
|Tidak Setuju|2|
|Netral|3|
|Setuju|4|
|Sangat Setuju|5|

![](img/likert.png)

#### ⚙️ Karakteristik:

- Jenis skala: **Ordinal (sering diperlakukan sebagai interval)**
    
- Dapat digunakan untuk menghitung **rata-rata, frekuensi, dan distribusi respon**
    
- Cocok untuk **mengukur persepsi atau kepuasan pengguna DSS**
    

#### ✅ Kelebihan:

- Mudah dipahami dan digunakan.
    
- Efisien untuk banyak variabel.
    

#### ❌ Kelemahan:

- Responden sering memilih jawaban tengah (bias netral).
    
- Tidak menunjukkan jarak yang pasti antar kategori.
    

---

## 2. Skala Guttman

#### 📘 Definisi:

Skala Guttman (atau _Cumulative Scale_) digunakan untuk **mengukur tingkat kesetujuan yang bersifat kumulatif dan logis berurutan.**

Jika responden setuju pada pernyataan tingkat tinggi, maka diasumsikan ia juga setuju pada pernyataan yang tingkatnya lebih rendah.

### 💡 Contoh:

Topik: _Penerimaan terhadap DSS di perusahaan_

|No|Pernyataan|Jawaban (Ya/Tidak)|
|---|---|---|
|1|Saya tahu bahwa perusahaan menggunakan DSS.|☐ Ya ☐ Tidak|
|2|Saya pernah mencoba menggunakan DSS.|☐ Ya ☐ Tidak|
|3|Saya menggunakan DSS secara rutin.|☐ Ya ☐ Tidak|
|4|Saya percaya DSS membantu meningkatkan kinerja saya.|☐ Ya ☐ Tidak|
|5|Saya merekomendasikan DSS kepada rekan kerja.|☐ Ya ☐ Tidak|

### ⚙️ Karakteristik:

- Jawaban bersifat **dikotomis (Ya/Tidak)**.
    
- Dapat digunakan untuk melihat **tingkat kedalaman sikap**.
    
- Skor dihitung berdasarkan jumlah “Ya”.
    

### ✅ Kelebihan:

- Sederhana dan jelas (responden tidak bingung).
    
- Mudah untuk mengukur sikap progresif.
    

### ❌ Kelemahan:

- Tidak bisa mengukur intensitas (hanya “setuju/tidak setuju”).
    
- Cocok hanya untuk topik dengan urutan logis.
    

---

## 3. Skala Semantic Differential (Skala Diferensial Semantik)

#### 📘 Definisi:

Skala ini digunakan untuk **mengukur makna dan persepsi terhadap suatu objek** melalui pasangan kata yang **berlawanan (bipolar)**.

Responden menilai posisi mereka antara dua kutub kata yang berlawanan.

#### 💡 Contoh:

![](img/semantic.png)

#### ⚙️ Karakteristik:

- Menggunakan **skala interval** (biasanya 5–7 poin).
    
- Mengukur persepsi terhadap **dimensi makna psikologis (baik–buruk, cepat–lambat, efisien–tidak efisien)**.
    

#### ✅ Kelebihan:

- Memberi gambaran persepsi yang lebih kaya dan mendalam.
    
- Dapat membandingkan persepsi antar dimensi.
    

#### ❌ Kelemahan:

- Menyusun pasangan kata bipolar yang relevan cukup sulit.
    
- Interpretasi bisa berbeda antar individu.
    

---

## 4. Skala Rating (Numerical Rating Scale)

#### 📘 Definisi:

Skala Rating adalah bentuk pengukuran di mana responden **memberi nilai numerik** terhadap suatu objek atau pernyataan berdasarkan tingkatannya.

Skala ini mirip dengan penilaian skor (rating) yang sering digunakan dalam survei kepuasan pelanggan atau sistem evaluasi kinerja.

#### 💡 Contoh:

> Nilai kemampuan DSS dalam membantu pengambilan keputusan:  
> 0 = Sangat Buruk … 10 = Sangat Baik

|Aspek|Skor (0–10)|
|---|---|
|Kecepatan Sistem|8|
|Keakuratan Hasil|9|
|Tampilan Antarmuka|7|

#### ⚙️ Karakteristik:

- Dapat berupa **skala numerik (0–10)** atau **grafik (bintang, garis)**.
    
- Umumnya dianggap **skala interval atau rasio** tergantung konteks.
    

#### ✅ Kelebihan:

- Mudah dipahami responden.
    
- Memberikan variasi jawaban yang luas.
    
- Cocok untuk analisis statistik kuantitatif.
    

#### ❌ Kelemahan:

- Bisa muncul bias ekstrem (responden memberi nilai sangat tinggi atau rendah).
    
- Interpretasi antar individu tidak selalu sama.
    

---

## 5. Skala Thurstone (Equal-Appearing Interval Scale)

#### 📘 Definisi:

Skala Thurstone digunakan untuk **mengukur sikap dengan sejumlah pernyataan yang telah diberi bobot nilai oleh panel ahli**, berdasarkan tingkat kesetujuannya.

Responden kemudian memilih pernyataan yang paling menggambarkan pandangannya.

#### 💡 Contoh:

Topik: _Sikap terhadap penggunaan DSS di perusahaan._

|No|Pernyataan|Nilai Bobot|
|---|---|---|
|1|DSS tidak penting dalam pengambilan keputusan.|1|
|2|DSS hanya digunakan oleh tim IT.|3|
|3|DSS membantu mempercepat analisis data.|7|
|4|DSS sangat penting dalam strategi bisnis.|10|

Responden memilih satu atau beberapa pernyataan yang paling sesuai dengan pendapatnya.  
Skor rata-rata dari pernyataan yang dipilih digunakan untuk menunjukkan posisi sikap responden.

#### ⚙️ Karakteristik:

- Skala interval (jarak antar pernyataan dianggap sama).
    
- Setiap pernyataan memiliki **nilai bobot hasil penilaian para ahli**.
    

#### ✅ Kelebihan:

- Lebih objektif karena bobot ditentukan oleh panel ahli.
    
- Cocok untuk topik yang membutuhkan validitas tinggi.
    

#### ❌ Kelemahan:

- Proses pembuatan skala memakan waktu dan kompleks.
    
- Responden harus membaca banyak pernyataan.
    

---

## 🧮 6. Perbandingan Antar Skala

|Jenis Skala|Jenis Data|Bentuk Jawaban|Contoh Pertanyaan|Kelebihan Utama|
|---|---|---|---|---|
|**Likert**|Ordinal|Tingkat persetujuan (1–5)|“Saya puas dengan DSS.”|Mudah dan populer|
|**Guttman**|Nominal (Ya/Tidak)|Dikotomis|“Saya menggunakan DSS setiap hari.”|Sederhana, logis|
|**Differensial Semantik**|Interval|Dua kutub makna|“Cepat – Lambat”|Mengukur persepsi makna|
|**Rating**|Interval/Rasio|Skor numerik (0–10)|“Nilai tampilan DSS.”|Kuantitatif dan fleksibel|
|**Thurstone**|Interval|Pilihan pernyataan berbobot|“DSS sangat penting bagi bisnis.”|Valid dan objektif|
> Pemilihan jenis skala pengukuran sangat penting dalam perancangan kuesioner karena akan memengaruhi **keakuratan data, metode analisis, dan hasil keputusan** dalam DSS.

- **Skala Likert** cocok untuk mengukur sikap umum pengguna.
    
- **Skala Guttman** cocok untuk mengukur sikap bertingkat (progresif).
    
- **Skala Differensial** cocok untuk mengukur persepsi terhadap kualitas atau makna.
    
- **Skala Rating** cocok untuk evaluasi kuantitatif atau kepuasan.
    
- **Skala Thurstone** cocok untuk pengukuran sikap dengan dasar teori kuat.