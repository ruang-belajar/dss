Berikut penjelasan **cara mengolah hasil pengisian kuesioner dengan Skala Thurstone**, dalam konteks **Decision Support System (DSS)** atau penelitian kuantitatif berbasis persepsi:

---

## 🧭 1. Konsep Dasar Skala Thurstone

Skala **Thurstone** digunakan untuk **mengukur sikap** dengan membandingkan sejumlah pernyataan yang memiliki **nilai sikap (scale value)** tertentu.  
Responden diminta **menyatakan setuju atau tidak setuju** terhadap beberapa pernyataan yang telah diberi bobot oleh para ahli.

Ciri khasnya:

- Skala bersifat **interval**.
    
- Tiap item memiliki **nilai numerik hasil penilaian panel ahli (judges)**.
    
- Responden hanya memberi tanda **setuju/tidak setuju**, bukan menilai secara langsung.
    

---

## ⚙️ 2. Langkah-Langkah Pengolahan Data Skala Thurstone

### Langkah 1 — Menyusun dan Menilai Pernyataan

1. Buat sejumlah pernyataan (misal 20–30) yang menggambarkan berbagai tingkat sikap dari sangat positif hingga sangat negatif.
    
2. Kumpulkan pendapat dari **panel ahli (judges)** yang menilai tiap pernyataan pada **skala 1–11** (atau 1–9).
    
3. Hitung **nilai median (Me)** dari setiap item → ini disebut **nilai skala (Scale Value)**.
    
4. Hitung juga **interquartile range (IQR)** tiap item untuk melihat konsistensi antar-ahli.
    
    - Item dengan IQR kecil berarti tingkat kesepakatan tinggi → dipertahankan.
        

---

### Langkah 2 — Menyusun Kuesioner Akhir

- Pilih item dengan sebaran nilai skala yang **merata dari rendah ke tinggi** dan **IQR kecil**.
    
- Sajikan kepada responden dengan instruksi **“Beri tanda setuju pada pernyataan yang sesuai dengan pendapat Anda.”**
    

---

### Langkah 3 — Mengumpulkan Data Responden

- Setiap responden memberi tanda “setuju” atau “tidak setuju”.
    
- Setiap pernyataan memiliki **nilai skala (dari hasil Langkah 1)**.
    

---

### Langkah 4 — Menghitung Skor Responden

1. Untuk setiap responden, ambil **nilai skala** dari item-item yang **disetujui**.
    
2. Hitung **rata-rata nilai skala** dari semua pernyataan yang disetujui responden:
    
    [  
    \text{Skor sikap responden} = \frac{\sum \text{nilai skala item yang disetujui}}{\text{jumlah item yang disetujui}}  
    ]
    
3. Skor ini menunjukkan **posisi sikap responden** di sepanjang kontinum sikap (misal dari negatif ke positif).
    

---

### Langkah 5 — Interpretasi

- **Semakin tinggi skor rata-rata**, semakin positif sikap responden terhadap objek yang diukur.
    
- Anda dapat membagi skor menjadi kategori, misalnya:
    
    - 1.00 – 3.00 = Sikap negatif
        
    - 3.01 – 5.00 = Netral
        
    - 5.01 – 7.00 = Positif  
        (disesuaikan dengan skala dan konteks penelitian)
        

---

## 📊 6. Contoh Sederhana

Misal 5 item dipilih dengan nilai skala dari hasil panel ahli:

|No|Pernyataan|Nilai Skala|Jawaban Responden|
|---|---|---|---|
|1|“Saya percaya teknologi mempermudah kerja.”|8.2|✔️ Setuju|
|2|“Teknologi membuat manusia malas.”|3.1|❌ Tidak|
|3|“Saya tidak suka perubahan sistem digital.”|2.4|❌ Tidak|
|4|“Digitalisasi penting untuk efisiensi.”|7.5|✔️ Setuju|
|5|“Teknologi sering menyebabkan gangguan.”|4.0|❌ Tidak|

**Skor rata-rata responden:**  
$(8.2 + 7.5) / 2 = 7.85$  
→ berarti responden memiliki **sikap sangat positif terhadap teknologi**.

---

## 💡 7. Konteks dalam Decision Support System

Dalam DSS, pengolahan data Thurstone berguna untuk:

- Mengukur **preferensi pengguna terhadap sistem baru**.
    
- Menilai **tingkat penerimaan (acceptance)** terhadap solusi teknologi.
    
- Mengonversi hasil persepsi menjadi **input numerik** untuk analisis lanjutan (misalnya metode SAW, TOPSIS, atau AHP).
    
---

## 💼 Diskusi & Tugas

Berikut hasil survei _Kuesioner Kepuasan Pengguna Sistem Informasi Akademik_ atas 1 responden

| No  | Pernyataan                                                                 | Nilai Skala (dari panel ahli) | Setuju | Tidak Setuju |
| --- | -------------------------------------------------------------------------- | ----------------------------- | ------ | ------------ |
| 1   | Sistem informasi baru membantu saya bekerja lebih efisien.                 | 8.5                           | ✓      |              |
| 2   | Sistem informasi baru membuat pekerjaan saya lebih rumit.                  | 2.8                           |        | ✓            |
| 3   | Saya merasa puas dengan fitur yang ada dalam sistem.                       | 7.6                           | ✓      |              |
| 4   | Saya tidak percaya bahwa sistem ini dapat meningkatkan produktivitas.      | 3.0                           |        | ✓            |
| 5   | Saya senang perusahaan menerapkan sistem berbasis digital.                 | 8.8                           | ✓      |              |
| 6   | Sistem ini sering menyebabkan kesalahan dalam pekerjaan.                   | 3.5                           |        | ✓            |
| 7   | Penggunaan sistem informasi baru mempercepat proses pengambilan keputusan. | 7.9                           | ✓      |              |
| 8   | Sistem ini tidak memberikan manfaat yang signifikan.                       | 2.6                           |        | ✓            |
| 9   | Saya ingin terus menggunakan sistem ini di masa depan.                     | 8.3                           | ✓      |              |
| 10  | Sistem ini memperlambat komunikasi antarbagian.                            | 3.2                           |        | ✓            |
🙋‍♂️ Buat analisa dan interpretasi terhadap hasil survei