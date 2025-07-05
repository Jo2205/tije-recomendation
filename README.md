# Sistem Rekomendasi Trayek Transjakarta
Proyek ini merupakan sistem rekomendasi trayek Transjakarta berbasis data jumlah penumpang selama tahun 2021. Sistem ini dibangun menggunakan Python dan Streamlit, dengan pendekatan machine learning (cosine similarity) untuk menemukan trayek-trayek yang memiliki pola penumpang bulanan yang mirip.

# Tujuan
Membantu Dinas Perhubungan atau operator Transjakarta dalam:
1. Mengidentifikasi trayek dengan pola penumpang yang serupa.
2. Memberikan rekomendasi trayek alternatif.
3. Menjadi dasar pertimbangan untuk optimalisasi armada dan perencanaan rute.

# Dataset
Data yang digunakan adalah data internal jumlah penumpang Transjakarta tahun 2021, dengan kolom:
* `periode_data`: format YYYYMM
* `jenis`: jenis angkutan
* `kode_trayek`: kode unik trayek
* `trayek`: nama rute trayek
* `jumlah_penumpang`: jumlah penumpang pada periode tersebut

# Fitur Aplikasi
* Visualisasi data mentah dan pivot tabel
* Normalisasi jumlah penumpang per bulan untuk tiap trayek
* Perhitungan kemiripan trayek berdasarkan pola penumpang (Cosine Similarity)
* Sistem rekomendasi: pengguna dapat memilih satu trayek dan mendapatkan rekomendasi trayek lain yang memiliki pola serupa
* Visualisasi grafik perbandingan trayek utama dan trayek yang direkomendasikan
* Fitur download grafik sebagai PNG

# Struktur Folder
```
├── app.py                        # Aplikasi utama Streamlit
├── data/
│   └── penumpang_2021.csv       # Dataset input
├── utils/
│   └── rekomendasi.py           # Fungsi bantu: normalisasi, similarity, rekomendasi
├── output/
│   └── rekomendasi_*.png        # Hasil grafik yang disimpan
└── README.md                    # Dokumentasi proyek
```

# Instalasi dan Menjalankan
# 1. Clone Repository dan Masuk Folder
```bash
git clone https://github.com/Jo2205/tije-recomendation.git
cd tije-recomendation
```

# 2. Install Library
```bash
pip install -r requirements.txt
```

# 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

# Output
* Visualisasi interaktif rekomendasi trayek
* Grafik perbandingan jumlah penumpang antar trayek
* File PNG yang bisa diunduh oleh pengguna

# Contoh Tampilan Aplikasi


Proyek ini saya kembangkan sebagai bagian dari portofolio data science dan dapat dijadikan referensi dalam pengembangan sistem berbasis data untuk transportasi publik.
