## Kasus singkat

Tujuan: **Memilih supplier terbaik**  
Kriteria: **Harga (C1)**, **Kualitas (C2)**, **Pengiriman (C3)**  
Alternatif: **A**, **B**, **C**

---

# 1) Matriks perbandingan berpasangan — **Kriteria**

Matriks (baris vs kolom: Harga, Kualitas, Pengiriman)

| Kriteria   |  Harga | Kualitas | Pengiriman |
| ---------- | -----: | -------: | ---------: |
| Harga      | 1.0000 |   0.3333 |     3.0000 |
| Kualitas   | 3.0000 |   1.0000 |     5.0000 |
| Pengiriman | 0.3333 |   0.2000 |     1.0000 |


### a) Jumlah tiap kolom

- kolom Harga = **4.3333**
    
- kolom Kualitas = **1.5333**
    
- kolom Pengiriman = **9.0000**
    

### b) Normalisasi (setiap elemen ÷ jumlah kolom masing-masing)

Normalisasi matriks:

| Kriteria   |  Harga | Kualitas | Pengiriman | Rata-rata baris (Bobot) |
| ---------- | -----: | -------: | ---------: | ----------------------: |
| Harga      | 0.2308 |   0.2174 |     0.3333 |              **0.2605** |
| Kualitas   | 0.6923 |   0.6522 |     0.5556 |              **0.6333** |
| Pengiriman | 0.0769 |   0.1304 |     0.1111 |              **0.1062** |

→ **Bobot kriteria (priority vector)**:

- Harga = **0.2605**
    
- Kualitas = **0.6333**
    
- Pengiriman = **0.1062**
    

(total ≈ 1.0000)

---

# 2) Uji konsistensi (untuk matriks kriteria)

Langkah:

1. Hitung **Weighted Sum Vector** = (Matriks asli) × (vektor bobot)
    

Weighted sum per baris:

- Harga = 0.7901
    
- Kualitas = 1.9456
    
- Pengiriman = 0.3197
    

2. Hitung λi = (Weighted Sum) ÷ (Bobot)
    

- λ_Harga = 3.0330
    
- λ_Kualitas = 3.0719
    
- λ_Pengiriman = 3.0112
    

3. λ_max = rata-rata(λi) = **3.0387**
    
4. Consistency Index (CI) = (λ_max − n) / (n − 1)  
    n = 3 → CI = (3.0387 − 3) / (2) = **0.019357**
    
5. Random Index (RI) untuk n=3 = **0.58**
    
6. Consistency Ratio (CR) = CI / RI = **0.0334** (≈ 3.34%)
    

**Interpretasi:** CR = 0.0334 ≤ 0.10 → **penilaian konsisten**.

---

# 3) Matriks perbandingan alternatif (per kriteria)

Saya gunakan tiga matriks contoh (baris & kolom: A, B, C).

### a) Matriks untuk **Harga**

||A|B|C|
|---|--:|--:|--:|
|**A**|1.0000|0.3333|0.2000|
|**B**|3.0000|1.0000|0.3333|
|**C**|5.0000|3.0000|1.0000|

Normalisasi kolom & rata-rata baris → **Bobot pada kriteria Harga**:

- A = **0.1062**
    
- B = **0.2605**
    
- C = **0.6333**
    

(artinya C terbaik dari sisi harga dalam contoh ini)

---

### b) Matriks untuk **Kualitas**

||A|B|C|
|---|--:|--:|--:|
|**A**|1.0000|0.3333|1.0000|
|**B**|3.0000|1.0000|5.0000|
|**C**|1.0000|0.2000|1.0000|

Normalisasi → **Bobot pada kriteria Kualitas**:

- A = **0.1867**
    
- B = **0.6555**
    
- C = **0.1578**
    

(B paling unggul kualitasnya)

---

### c) Matriks untuk **Pengiriman**

||A|B|C|
|---|--:|--:|--:|
|**A**|1.0000|0.5000|3.0000|
|**B**|2.0000|1.0000|5.0000|
|**C**|0.3333|0.2000|1.0000|

Normalisasi → **Bobot pada kriteria Pengiriman**:

- A = **0.3092**
    
- B = **0.5813**
    
- C = **0.1096**
    

(B juga unggul di pengiriman pada contoh ini)

> (Catatan: untuk tiap matriks alternatif di atas saya menggunakan nilai perbandingan contoh — Anda bebas mengganti nilai tersebut sesuai data nyata, lalu ulangi langkah normalisasi.)

---

# 4) Sintesis — hitung skor total tiap alternatif

Susun bobot alternatif per kriteria (baris=alternatif A,B,C; kolom=Harga, Kualitas, Pengiriman):

|Alternatif|Harga (w=0.1062)|Kualitas (w=0.1867)|Pengiriman (w=0.3092)|
|---|--:|--:|--:|
|**A**|0.1061563|0.1867495|0.3091503|
|**B**|0.2604980|0.6554865|0.5812636|
|**C**|0.6333457|0.1577640|0.1095861|

Catatan: angka di kolom adalah bobot relatif per kriteria (lihat bagian 3).

Gunakan bobot kriteria (global) = [0.2605, 0.6333, 0.1062] (Harga, Kualitas, Pengiriman) — hasil dari langkah 1.

Skor total tiap alternatif = Σ ( bobot_alternatif_pada_kriteria × bobot_kriteria )

Perhitungan (dibulatkan 4 desimal):

- **Skor A** = 0.1061563×0.2604979 + 0.1867495×0.6333457 + 0.3091503×0.1061563  
    ≈ 0.0276 + 0.1183 + 0.0329 = **0.1787**
    
- **Skor B** = 0.26049796×0.2604979 + 0.65548654×0.6333457 + 0.5812636×0.1061563  
    ≈ 0.0679 + 0.4150 + 0.0618 = **0.5447**
    
- **Skor C** = 0.63334572×0.2604979 + 0.15776398×0.6333457 + 0.10958606×0.1061563  
    ≈ 0.1650 + 0.1000 + 0.0116 = **0.2765**
    

---

# 5) Hasil akhir dan ranking

|Alternatif|Skor Total|
|---|--:|
|**B**|**0.5447** → **Peringkat 1 (Terbaik)**|
|**C**|0.2765 → Peringkat 2|
|**A**|0.1787 → Peringkat 3|

**Kesimpulan:** Berdasarkan simulasi AHP ini (dengan matriks contoh yang diberikan), **Supplier B** memiliki skor tertinggi → direkomendasikan sebagai pilihan terbaik.

---

# 6) Catatan praktis & tips

- **Konsistensi**: selalu cek CR pada matriks kriteria; jika CR > 0.10, perbaiki penilaian pairwise. (Dalam contoh CR ≈ **0.0334**, konsisten.)
    
- **Alternatif**: Anda bisa juga menghitung CR untuk setiap matriks alternatif (opsional) untuk mengecek konsistensi penilaian pada level alternatif.
    
- **Normalisasi & pembulatan**: lakukan perhitungan dengan banyak desimal di Excel lalu tampilkan 3–4 desimal untuk presentasi.
    
- **Otomatisasi**: cocok dimasukkan ke template Excel yang otomatis menghitung normalisasi, bobot, weighted sum, λmax, CI, CR, dan sintesis akhir.
    

---

Jika Anda mau, saya bisa:

1. **Buatkan file Excel (.xlsx)** otomatis yang berisi seluruh langkah (input matriks, normalisasi, bobot, uji konsistensi, dan sintesis), atau
    
2. **Kirimkan langkah-langkah rumus Excel** (sel per sel) agar Anda mengimplementasikannya sendiri.
    

Mau yang mana?