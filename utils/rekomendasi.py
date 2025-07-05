# utils/rekomendasi.py

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity

# Fungsi normalisasi data

def normalisasi_data(df):
    scaler = MinMaxScaler()
    data_normalized = pd.DataFrame(
        scaler.fit_transform(df.fillna(0)),  # isi NaN dengan 0
        index=df.index,
        columns=df.columns
    )
    return data_normalized

# Fungsi menghitung similarity antar trayek

def hitung_similarity(df_normalized):
    similarity_matrix = cosine_similarity(df_normalized)
    similarity_df = pd.DataFrame(similarity_matrix, index=df_normalized.index, columns=df_normalized.index)
    return similarity_df

# Fungsi rekomendasi trayek paling mirip

def rekomendasikan_trayek(trayek_id, similarity_df, n=5):
    if trayek_id not in similarity_df.columns:
        raise ValueError(f"Trayek {trayek_id} tidak ditemukan dalam data")
    return similarity_df[trayek_id].drop(trayek_id).sort_values(ascending=False).head(n)
