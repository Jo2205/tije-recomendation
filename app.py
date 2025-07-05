import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from utils.rekomendasi import normalisasi_data, hitung_similarity, rekomendasikan_trayek
import os
import base64

# Judul aplikasi
st.title("Sistem Rekomendasi Trayek Transjakarta")

# Langkah 1: Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/penumpang_2021.csv")
    # Tambahkan kolom bulan dari periode_data
    df["bulan"] = df["periode_data"].astype(str).str[-2:].astype(int)
    return df

data = load_data()

# Buat dictionary: kode_trayek -> nama trayek
trayek_dict = (
    data.drop_duplicates(subset=["kode_trayek"])
    .set_index("kode_trayek")["trayek"]
    .to_dict()
)

# Langkah 2: Buat pivot table (trayek sebagai baris, bulan sebagai kolom)
pivot_penumpang = data.pivot_table(
    index="kode_trayek",
    columns="bulan",
    values="jumlah_penumpang",
    aggfunc="sum"
)

st.subheader("Contoh Data Penumpang")
st.dataframe(data.head())

st.subheader("Pivot Jumlah Penumpang per Bulan")
st.dataframe(pivot_penumpang.head())

# Langkah 3: Normalisasi data
pivot_normalized = normalisasi_data(pivot_penumpang)

# Langkah 4: Hitung similarity
similarity_df = hitung_similarity(pivot_normalized)

# Langkah 5: Dropdown untuk pilih trayek dengan label lengkap
st.subheader("Pilih Trayek untuk Rekomendasi")
kode_options = sorted(pivot_penumpang.index)
trayek_labels = [f"{kode} - {trayek_dict.get(kode, '')}" for kode in kode_options]
selected_label = st.selectbox("Kode Trayek:", options=trayek_labels)
selected_trayek = selected_label.split(" - ")[0]

# Tampilkan rekomendasi jika trayek dipilih
if selected_trayek:
    rekomendasi = rekomendasikan_trayek(selected_trayek, similarity_df, n=5)
    st.write(f"### Rekomendasi trayek yang mirip dengan {selected_label}:")
    st.dataframe(rekomendasi)

    # Visualisasi perbandingan trayek utama dan rekomendasi
    st.subheader("Visualisasi Perbandingan Jumlah Penumpang")
    fig, ax = plt.subplots(figsize=(10, 5))

    # Trayek utama
    ax.plot(
        pivot_penumpang.columns,
        pivot_penumpang.loc[selected_trayek],
        label=f"Trayek {selected_trayek} - {trayek_dict.get(selected_trayek, '')} (Utama)",
        linewidth=3,
        color='blue'
    )

    # Trayek rekomendasi
    for trayek_id in rekomendasi.index:
        ax.plot(
            pivot_penumpang.columns,
            pivot_penumpang.loc[trayek_id],
            label=f"Trayek {trayek_id} - {trayek_dict.get(trayek_id, '')}",
            linestyle='--'
        )

    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Penumpang")
    ax.set_title("Perbandingan Jumlah Penumpang Tiap Bulan")
    ax.legend(loc='upper right')
    ax.grid(True)
    st.pyplot(fig)

    # Simpan grafik ke file PNG
# Setelah menyimpan file ke PNG
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
filename = f"{output_dir}/rekomendasi_{selected_trayek}.png"
fig.savefig(filename, dpi=300)
st.success(f"Grafik disimpan sebagai {filename}")

# Tombol download PNG
with open(filename, 'rb') as f:
    img_bytes = f.read()
    b64 = base64.b64encode(img_bytes).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="rekomendasi_{selected_trayek}.png">📥 Download Grafik sebagai PNG</a>'
    st.markdown(href, unsafe_allow_html=True)

