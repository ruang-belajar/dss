# Contoh Kasus Memilih Smartphone

## Judul kasus

Memilih **smartphone** terbaik untuk dibeli berdasarkan beberapa kriteria.

---

## 1. Deskripsi singkat masalah

Seorang pembeli ingin memilih 1 dari 3 pilihan smartphone (S1, S2, S3). Penilaian dilakukan berdasarkan 4 kriteria:

- **C1 — Harga (Cost)** (lebih murah lebih baik)
    
- **C2 — Kapasitas baterai (Benefit)** (mAh, lebih besar lebih baik)
    
- **C3 — Kamera (Benefit)** (MP, lebih besar lebih baik)
    
- **C4 — Penyimpanan (Benefit)** (GB, lebih besar lebih baik)
    

Bobot kepentingan tiap kriteria ditetapkan:

- $w_{C1} = 0{,}30$ (Harga)
    
- $w_{C2} = 0{,}30$ (Baterai)
    
- $w_{C3} = 0{,}25$ (Kamera)
    
- $w_{C4} = 0{,}15$ (Penyimpanan)  
    Jumlah bobot = 1,00.
    

---

## 2. Matriks keputusan (nilai asli)

| Alternatif | Harga (Rp) | Baterai (mAh) | Kamera (MP) | Storage (GB) |     |
| ---------- | ---------- | ------------- | ----------- | -----------: | --- |
| S1         | 3.000.000  | 4000          | 48          |          128 |     |
| S2         | 2.500.000  | 5000          | 64          |          256 |     |
| S3         | 3.200.000  | 4500          | 50          |          128 |     |

---

## 3. Normalisasi (rumus SAW)

- Untuk **kriteria benefit**: $r_{ij} = \dfrac{x_{ij}}{\max(x_j)}$
    
- Untuk **kriteria cost**: $r_{ij} = \dfrac{\min(x_j)}{x_{ij}}$
    

Hitung nilai ekstrim per kriteria:

- Harga (cost): $\min = 2.500.000$ (S2)
    
- Baterai (benefit): $max = 5000$ (S2)
    
- Kamera (benefit): $max = 64$ (S2)
    
- Storage (benefit): $max = 256$ (S2)
    

### Normalisasi per alternatif:

**C1 — Harga (cost)**

- $r_{11} = 2.500.000 / 3.000.000 = 0{,}833333\ldots$ (S1)
    
- $r_{21} = 2.500.000 / 2.500.000 = 1{,}000$ (S2)
    
- $r_{31} = 2.500.000 / 3.200.000 = 0{,}78125$ (S3)
    

**C2 — Baterai (benefit)**

- $r_{12} = 4000 / 5000 = 0{,}8$ (S1)
    
- $r_{22} = 5000 / 5000 = 1{,}0$ (S2)
    
- $r_{32} = 4500 / 5000 = 0{,}9$ (S3)
    

**C3 — Kamera (benefit)**

- $r_{13} = 48 / 64 = 0{,}75$ (S1)
    
- $r_{23} = 64 / 64 = 1{,}0$ (S2)
    
- $r_{33} = 50 / 64 = 0{,}78125$ (S3)
    

**C4 — Storage (benefit)**

- $r_{14} = 128 / 256 = 0{,}5$ (S1)
    
- $r_{24} = 256 / 256 = 1{,}0$ (S2)
    
- $r_{34} = 128 / 256 = 0{,}5$ (S3)
    

Tabel normalisasi $R = [r_{ij}]$:

| Alternatif | C1 (Harga) | C2 (Baterai) | C3 (Kamera) | C4 (Storage) |
| ---------: | ---------: | -----------: | ----------: | -----------: |
|         S1 |  0.833333… |     0.800000 |    0.750000 |     0.500000 |
|         S2 |   1.000000 |     1.000000 |    1.000000 |     1.000000 |
|         S3 |   0.781250 |     0.900000 |    0.781250 |     0.500000 |

---

## 4. Menghitung skor preferensi (V_i)

Rumus:  
$$V_i = \sum_{j=1}^{4} w_j \cdot r_{ij}$$

### Perhitungan rinci (hitung digit-demi-digit):

**Untuk S1**

- $0{,}30 \times 0{,}833333\ldots = 0{,}25) (karena (0{,}833333\ldots = 5/6), (5/6 \times 0{,}3 = 0{,}25)$
    
- $0{,}30 \times 0{,}8 = 0{,}24$
    
- $0{,}25 \times 0{,}75 = 0{,}1875$
    
- $0{,}15 \times 0{,}5 = 0{,}075$
    Jumlah: $0{,}25 + 0{,}24 + 0{,}1875 + 0{,}075 = 0{,}7525$
    ⇒ **(V_1 = 0{,}7525)**
    

**Untuk S2**

- $0{,}30 \times 1{,}0 = 0{,}30$
    
- $0{,}30 \times 1{,}0 = 0{,}30$
    
- $0{,}25 \times 1{,}0 = 0{,}25$
    
- $0{,}15 \times 1{,}0 = 0{,}15$
    Jumlah: (0{,}30 + 0{,}30 + 0{,}25 + 0{,}15 = 1{,}00)  
    ⇒ **(V_2 = 1{,}0000)**
    

**Untuk S3**

- $0{,}30 \times 0{,}78125 = 0{,}234375$
    
- $0{,}30 \times 0{,}9 = 0{,}27$
    
- $0{,}25 \times 0{,}78125 = 0{,}1953125$
    
- $0{,}15 \times 0{,}5 = 0{,}075$  
    Jumlah: $0{,}234375 + 0{,}27 + 0{,}1953125 + 0{,}075 = 0{,}7746875$
    ⇒ **$V_3 = 0{,}7746875$**
    

---

## 5. Hasil dan Peringkat

Urutkan $V_i$ dari besar ke kecil:

1. **S2** — $V_2 = 1{,}0000$ → **Alternatif terbaik**
    
2. **S3** — $V_3 = 0{,}7746875$
    
3. **S1** — $V_1 = 0{,}7525$
    

**Kesimpulan:** Berdasarkan metode SAW dengan bobot yang diberikan, **S2** adalah pilihan terbaik (memiliki skor tertinggi).

---

## 6. Interpretasi & Catatan

- S2 unggul di semua kriteria (harga terendah, baterai terbesar, kamera terbaik, storage terbesar) sehingga mendapat skor sempurna 1,00.
    
- Jika bobot kriteria diubah (mis. pembeli sangat menekankan kamera), peringkat akhir bisa berubah. Oleh karena itu **sensitivitas bobot** penting untuk dianalisis bila keputusan sensitif terhadap preferensi pembuat keputusan.
    
- SAW sederhana, cepat, dan mudah diimplementasikan, tetapi bergantung kuat pada penentuan bobot dan skala normalisasi.
    
