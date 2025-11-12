# Profile Matching
## 🔍 Pengertian Profile Matching (PM)

**Profile Matching** adalah sebuah mekanisme pengambilan keputusan dengan mengasumsikan bahwa terdapat Tingkat variabel prediktor yang ideal yang harus dipenuhi oleh subyek yang diteliti, bukannya tingkat minimal yang harus dipenuhi atau dilewati (Kusrini, 2007)

Proses perhitungan pada metode PM, diawali dengan pendefinisian nilai minimum untuk setiap variabel variabel penilaian. Selisih setiap nilai data testing terhadap nilai minimum masing-masing variabel, merupakan gap yang kemudian diberi bobot. Bobot setiap variabel akan dihitung rata-rata berdasarkan kelompok variabel Core Factor (CF) dan Secondary Factor (SF). Komposisi CF ditambah SF adalah 100%, tergantung dari kepentingan pengguna metode ini. Tahap terakhir dari metode ini, adalah proses akumulasi nilai CF dan SF berdasarkan nilai-nilai variabel data testing (Kusrini, 2007)

Pembobotan pada metode PM, merupakan nilai pasti yang tegas pada nilai tertentu karena nilai-nilai yang ada merupakan anggota himpunan tegas (crisp set). Di dalam himpunan tegas, keanggotaan suatu unsur di dalam himpunan dinyatakan secara tegas, apakah objek tersebut anggota himpunan atau bukan dengan menggunakan fungsi karakteristik.

---

## ⚙️ Konsep Dasar

1. **Profil Ideal (Target)**  
    Nilai atau kriteria standar yang dianggap paling sesuai untuk suatu posisi, jabatan, atau keputusan.  
    Contoh: karyawan ideal memiliki kemampuan komunikasi = 5, kepemimpinan = 4, loyalitas = 5.
    
2. **Profil Aktual (Alternatif)**  
    Nilai nyata yang dimiliki kandidat atau objek yang akan dinilai.  
    Contoh: kandidat A memiliki komunikasi = 4, kepemimpinan = 3, loyalitas = 5.
    
3. **Gap (Selisih)**  
    Dihitung sebagai selisih antara profil aktual dan profil ideal.  
    $$Gap = {Nilai Aktual} - {Nilai Ideal}$$
    
4. **Bobot Gap (Bobot Nilai Selisih)**  
    Setiap gap diberi nilai bobot sesuai tingkat perbedaan. Misalnya:
    
| Gap | Bobot Nilai |
| --- | ----------- |
| 0   | 5           |
| 1   | 4.5         |
| -1  | 4           |
| 2   | 3.5         |
| -2  | 3           |
| 3   | 2.5         |
| -3  | 2           |
    
5. **Faktor Core dan Secondary**  
    Setiap aspek dapat dibagi menjadi dua jenis kriteria:
    
    - **Core Factor (CF):** faktor utama yang paling menentukan.
        
    - **Secondary Factor (SF):** faktor pendukung.
        
    Kemudian dihitung rata-rata bobot keduanya:  
    $$Nilai_Aspek = (CF \times 60\%) + (SF \times 40\%)$$
	
1. **Nilai Akhir (Ranking)**  
    Semua aspek dijumlahkan dengan bobot sesuai kepentingannya untuk mendapatkan **nilai total** dan menentukan **peringkat (ranking)** alternatif.

---

## 🧮 Langkah-Langkah Perhitungan Profile Matching

1. Menentukan **kriteria dan bobot**.
    
2. Menetapkan **profil ideal (standar)** untuk setiap kriteria.
    
3. Mengumpulkan **data aktual** dari setiap alternatif.
    
4. Menghitung **gap (selisih)** antara profil aktual dan profil ideal.
    
5. Memberikan **bobot nilai** pada setiap gap.
    
6. Menghitung **nilai rata-rata** CF dan SF.
    
7. Menggabungkan hasil setiap aspek menjadi **nilai total akhir**.
    
8. Menentukan **ranking alternatif** berdasarkan nilai total.
    

---

## 📊 Contoh Sederhana

Berikut contoh perhitungan $Nilai Aspek$ untuk 1 kandidat

| Kriteria     | Bobot | Ideal | Kandidat A | Gap | Nilai Bobot |
| ------------ | ----- | ----- | ---------- | --- | ----------- |
| Komunikasi   | CF    | 5     | 4          | -1  | 4           |
| Kepemimpinan | CF    | 4     | 3          | -1  | 4           |
| Loyalitas    | SF    | 5     | 5          | 0   | 5           |

Hitung:  
$$CF = (4 + 4) / 2 = 4$$  $$SF = (5) / 1 = 5$$  $${Nilai Aspek} = (CF \times 0.6) + (SF \times 0.4) = (4 \times 0.6) + (5 \times 0.4) = 4.4$$
Jika dibandingkan dengan kandidat lain, maka yang memiliki nilai aspek tertinggi dianggap **paling sesuai dengan profil ideal**.

---
## Panduan Bobot CF : SF Berdasarkan Jenis Pekerjaan

Dalam sistem pendukung keputusan, **bobot CF:SF dianggap sebagai parameter pengendali keputusan (decision parameter)**.  
Artinya:

> 💡 Bobot tersebut bisa diubah dalam sistem untuk **melihat dampak perubahan prioritas terhadap hasil akhir (sensitivity analysis)**.

Dengan begitu, pembuat keputusan bisa melihat bagaimana perubahan bobot (misalnya dari 60:40 menjadi 70:30) memengaruhi **ranking kandidat**.

Berikut adalah 📊 **tabel panduan umum** yang bisa menjadi acuan untuk menentukan **bobot Core Factor (CF)** dan **Secondary Factor (SF)** dalam metode **Profile Matching**, disesuaikan dengan **jenis pekerjaan**.

|**Kategori Pekerjaan**|**Contoh Jabatan**|**Bobot CF**|**Bobot SF**|**Alasan Utama / Pertimbangan**|
|---|---|:-:|:-:|---|
|**Teknis / Operasional**|Teknisi, Programmer, Analis Data, Operator Mesin|**70%**|**30%**|Keberhasilan pekerjaan sangat tergantung pada kemampuan teknis dan pengalaman inti.|
|**Administratif / Back Office**|Staf Administrasi, Petugas Arsip, Sekretaris|**60%**|**40%**|Faktor teknis dan ketelitian penting, namun kemampuan komunikasi & kerapian juga berpengaruh.|
|**Manajerial / Kepemimpinan**|Supervisor, Manajer Proyek, Kepala Departemen|**55%**|**45%**|Faktor kepemimpinan dan pengambilan keputusan menjadi inti, namun komunikasi dan interpersonal juga penting.|
|**Pemasaran / Sales / Customer Service**|Sales Executive, Marketing Officer, Customer Relation|**50%**|**50%**|Kinerja ditentukan oleh kemampuan komunikasi, negosiasi, dan hubungan interpersonal yang setara pentingnya dengan skill inti.|
|**Kreatif / Desain / Inovasi**|Desainer Grafis, Copywriter, Content Creator|**60%**|**40%**|Skill utama penting, tapi kreativitas dan fleksibilitas (soft skill) juga berperan besar.|
|**Keuangan / Akuntansi**|Akuntan, Analis Keuangan, Auditor|**65%**|**35%**|Kompetensi teknis dan akurasi menjadi inti utama, sedangkan komunikasi mendukung koordinasi dan laporan.|
|**Pendidikan / Pelatihan**|Guru, Dosen, Trainer|**55%**|**45%**|Kompetensi akademik penting, namun kemampuan komunikasi, empati, dan motivasi juga krusial.|
|**Pelayanan Publik / Kesehatan**|Perawat, Petugas Layanan, Dokter|**60%**|**40%**|Kompetensi teknis medis penting, tapi empati, komunikasi, dan etika menjadi faktor pendukung utama.|
|**Eksekutif / Strategis Tinggi**|Direktur, CEO, Head of Division|**50%**|**50%**|Keputusan strategis memerlukan keseimbangan antara kemampuan analitis dan keterampilan interpersonal.|

---
   
### 📚 Referensi Teoretis dari Literatur Akademik

Beberapa sumber teori dan penelitian yang sering digunakan:

|Sumber / Peneliti|Tahun|Keterangan Penting|
|:--|:--|:--|
|Kusrini, _Konsep dan Aplikasi Sistem Pendukung Keputusan (Decision Support System)_|**2007**|Menyebutkan bahwa dalam metode Profile Matching, faktor penilaian dibagi menjadi _Core Factor (CF)_ dan _Secondary Factor (SF)_, dan bobot **60% : 40%** sering digunakan sebagai **standar umum** untuk memprioritaskan faktor inti.|
|Marimin & Maghfiroh, _Aplikasi Teknik Pengambilan Keputusan dalam Manajemen Rantai Pasok_|**2010**|Menyatakan bahwa proporsi CF dan SF dapat **disesuaikan dengan tingkat pengaruh masing-masing faktor terhadap keberhasilan kerja**. Tidak baku, namun sering menggunakan **60–70% CF** untuk posisi teknis.|
|Turban, Efraim et al., _Decision Support and Business Intelligence Systems_|**2011**|Menjelaskan bahwa dalam DSS, bobot harus ditentukan berdasarkan **analisis prioritas atau expert judgment**. CF dan SF dalam Profile Matching dapat dianggap sebagai _criteria weight_ yang diperoleh dari analisis ahli.|
|Pratiwi, D. A. (Jurnal Ilmiah, _Profile Matching untuk Seleksi Karyawan_, Universitas Gunadarma)|**2013**|Menggunakan **bobot CF:SF = 60% : 40%** sebagai pembobotan umum yang dianggap representatif bagi kebanyakan posisi administrasi dan teknis.|
|Yulianti, L., _Penerapan Metode Profile Matching pada Penilaian Kinerja Karyawan_|**2018**|Menguatkan bahwa bobot CF yang lebih besar (60%–70%) **mencerminkan faktor inti yang lebih berpengaruh terhadap performa kerja**.|

### Dasar Praktis (Empiris)

Penentuan bobot 60:40, 70:30, atau 50:50 bukan angka kaku, tetapi:

- **Ditentukan berdasarkan expert judgment**, yaitu hasil diskusi atau wawancara dengan pakar HRD, manajer lini, atau pimpinan departemen.
    
- **Berdasarkan Analisis Jabatan (Job Analysis)** dan **Profil Kompetensi Jabatan (Competency Profile)**.
    
- **Disesuaikan dengan karakteristik pekerjaan**:
    
    - Semakin teknis → CF lebih dominan
        
    - Semakin berorientasi komunikasi / interpersonal → SF lebih tinggi

### Pedoman Umum Penetapan Bobot (dalam DSS)

|Jenis Pekerjaan|Dasar Penetapan|Kisaran Bobot Umum|
|:--|:--|:-:|
|**Teknis**|Berdasarkan keahlian, keterampilan teknis dominan|70% CF : 30% SF|
|**Administratif**|Keseimbangan antara ketelitian dan komunikasi|60% CF : 40% SF|
|**Manajerial**|Seimbang antara kepemimpinan dan interpersonal|55% CF : 45% SF|
|**Sales / Komunikatif**|Hubungan interpersonal dominan|50% CF : 50% SF|

---
## Kelebihan & Kekurangan PM
### 🎯 Kelebihan 

- Metode Profile Matching merupakan sebuah metode yang paling tepat digunakan dalam proses membandingkan antar kompetensi individu ke dalam kompetensi suatu jabatan sehingga dapat di ketahui perbedaan kompetensi nya.

- Profile Matching merupakan metode yang sangat sesuai di gunakan untuk pengambilan keputusan yang berhubungan semakin besar. dengan nilai prestasi jabatan dan kompetensi karena perhitungan yang di lakukan dengan pembobotan dan perhitungan gap dengan demikian untuk calon kandidat yang memiliki gap lebih kecil maka nilai bobotnya akan

- Profile Matching mempertimbangkan konsistensi yang logis dalam penilaian yang di gunakan untuk menentukan prioritas sehingga menghasilkan alternatif yang tidak banyak

- Cocok untuk seleksi berbasis kompetensi (SDM, penerimaan mahasiswa, promosi jabatan).    

- Mampu memperlihatkan tingkat kesesuaian secara kuantitatif.    

### ⚠️ Kelemahan

- Penentuan bobot dan nilai gap bersifat subjektif.

- Tidak mempertimbangkan hubungan antar kriteria.

- Hanya cocok jika kriteria bersifat terukur dan terstandar.

- Profile Matching tidak memperhitungkan daya tahan atau ketahanan output analisis sensitivitas pengambilan Keputusan.

- Profile Matching tidak mempunyai kemampuan untuk memecahkan masalah yang diteliti multi objek dan multi kriteria yang berdasar pada perbandingan preferensi dari tiap elemen dalam hierarki.
    
---

## Contoh Kasus — Seleksi Karyawan menggunakan Profile Matching

Kita akan memilih **4 kandidat (A, B, C, D)** berdasarkan 5 kriteria.

Tiap kriteria diberi label **Core Factor (CF)** atau **Secondary Factor (SF)**. 

Langkah: tentukan profil ideal → kumpulkan skor aktual → hitung _gap_ → konversi _gap_ ke _nilai bobot_ → hitung rata-rata CF & SF → gabungkan (CF 60% : SF 40%) → ranking.

---

### 1) Kriteria, bobot CF/SF, dan profil ideal

- **Kriteria (skala 1–5)**:    
    1. Education (Pendidikan) — **SF** — _Ideal = 4_        
    2. Experience (Pengalaman) — **CF** — _Ideal = 5_        
    3. Technical Skill (Keterampilan Teknis) — **CF** — _Ideal = 5_        
    4. Communication (Komunikasi) — **SF** — _Ideal = 4_        
    5. Leadership (Kepemimpinan) — **CF** — _Ideal = 4_        

CF total akan dikombinasi menjadi skor CF_avg, SF menjadi SF_avg.

---

### 2) Data skor aktual kandidat

| Kandidat | Education | Experience | Technical | Communication | Leadership |
| -------: | :-------: | :--------: | :-------: | :-----------: | :--------: |
|    **A** |     4     |     5      |     4     |       3       |     3      |
|    **B** |     3     |     4      |     5     |       4       |     4      |
|    **C** |     4     |     3      |     4     |       5       |     5      |
|    **D** |     5     |     5      |     3     |       4       |     2      |

---

### 3) Hitung _Gap_ (Actual − Ideal)

Contoh: Kandidat A, Education gap = 4 − 4 = 0.

|Kandidat|Edu_gap|Exp_gap|Tech_gap|Comm_gap|Lead_gap|
|--:|:-:|:-:|:-:|:-:|:-:|
|**A**|0|0|-1|-1|-1|
|**B**|-1|-1|0|0|0|
|**C**|0|-2|-1|1|1|
|**D**|1|0|-2|0|-2|

---

### 4) Konversi _Gap_ → _Nilai Bobot_ (tabel konversi yang digunakan)

Untuk contoh ini kita gunakan tabel konversi (biasa dipakai di Profile Matching):

|Gap|Nilai Bobot|
|:-:|:-:|
|0|5.0|
|1|4.5|
|-1|4.0|
|2|3.5|
|-2|3.0|
|3|2.5|
|-3|2.0|

(Catatan: tabel ini harus distandarisasi di organisasi — pilih salah satu versi dan konsisten.)

Mengonversi setiap gap ke bobot:

|Kandidat|Edu_w|Exp_w|Tech_w|Comm_w|Lead_w|
|--:|:-:|:-:|:-:|:-:|:-:|
|**A**|5.0|5.0|4.0|4.0|4.0|
|**B**|4.0|4.0|5.0|5.0|5.0|
|**C**|5.0|3.0|4.0|4.5|4.5|
|**D**|4.5|5.0|3.0|5.0|3.0|

---

### 5) Hitung rata-rata CF dan SF per kandidat

- **CF** = rata dari kriteria bertipe CF (Experience, Technical, Leadership).
    
- **SF** = rata dari kriteria bertipe SF (Education, Communication).
    
- Kombinasi akhir: **Final Score = (CF_avg × 60%) + (SF_avg × 40%)**
    

Perhitungan:

#### Kandidat A

- CF_avg = (Experience_w + Technical_w + Leadership_w) / 3  
    = (5.0 + 4.0 + 4.0) / 3 = 13.0 / 3 = **4.333**
    
- SF_avg = (Education_w + Communication_w) / 2  
    = (5.0 + 4.0) / 2 = **4.5**
    
- Final = 4.333×0.6 + 4.5×0.4 = 2.5998 + 1.8 = **4.3998 ≈ 4.40**
    

#### Kandidat B

- CF_avg = (4.0 + 5.0 + 5.0) / 3 = 14.0 / 3 = **4.667**
    
- SF_avg = (4.0 + 5.0) / 2 = **4.5**
    
- Final = 4.667×0.6 + 4.5×0.4 = 2.8002 + 1.8 = **4.6002 ≈ 4.60**
    

#### Kandidat C

- CF_avg = (3.0 + 4.0 + 4.5) / 3 = 11.5 / 3 = **3.833**
    
- SF_avg = (5.0 + 4.5) / 2 = **4.75**
    
- Final = 3.833×0.6 + 4.75×0.4 = 2.2998 + 1.9 = **4.1998 ≈ 4.20**
    

#### Kandidat D

- CF_avg = (5.0 + 3.0 + 3.0) / 3 = 11.0 / 3 = **3.667**
    
- SF_avg = (4.5 + 5.0) / 2 = **4.75**
    
- Final = 3.667×0.6 + 4.75×0.4 = 2.2002 + 1.9 = **4.1002 ≈ 4.10**
    

---

### 6) Tabel Hasil Akhir & Ranking

|Kandidat|CF_avg|SF_avg|Final Score|Ranking|
|--:|:-:|:-:|:-:|:-:|
|**B**|4.667|4.50|**4.60**|**1**|
|**A**|4.333|4.50|**4.40**|2|
|**C**|3.833|4.75|**4.20**|3|
|**D**|3.667|4.75|**4.10**|4|

**Rekomendasi**: Pilih **Kandidat B** (skor tertinggi 4.60). Jika diperlukan wawancara lanjutan, prioritaskan B lalu A.

---

### 7) Interpretasi singkat

- Kandidat **B** unggul pada Technical & Leadership (CF tinggi) sehingga meskipun Education agak lebih rendah, **CF** yang lebih penting (60%) membuat B terbaik.
    
- Kandidat **C** dan **D** punya SF yang baik (pendidikan/komunikasi) tetapi CF yang menurun menurunkan total akhir.
    
- Profile Matching membantu memisahkan kandidat yang “cukup” pada SF tetapi kurang pada CF (faktor inti pekerjaan).   

* Bobot **CF:SF** dapat disesuaikan berdasarkan **profil kompetensi jabatan** (Job Competency Profile) yang sudah ditetapkan organisasi.
    
- Semakin **teknis** suatu posisi, semakin **besar bobot CF**.
    
- Semakin **berorientasi manusia/komunikasi**, semakin **besar bobot SF**.
    
- Gunakan **uji sensitivitas (sensitivity analysis)** dalam sistem DSS untuk melihat bagaimana perubahan bobot memengaruhi peringkat akhir.

---
## 📁 Template Spreadsheet 

Untuk kemudahan perhitungan, gunakan spreadsheet berikut:
* [Template spreadsheet](https://docs.google.com/spreadsheets/d/1I1PZ5qshDRGVLP2XKLYClqfwdP73H2Q9tuPY5Aytz94/edit?usp=sharing) ([sumber](https://www.kodingbuton.com/2022/04/spk-metode-profile-matching.html))

Modifikasi sheet sesuai kebutuhan

---

## Referensi

- [Materi Profile Matching by Feri Alpiyasin, M.Kom](https://www.canva.com/design/DAG1vOzTgow/U4ww5PpgXPyTatvgAc7wzg/edit)