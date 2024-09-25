# -*- coding: utf-8 -*-
"""Andy Nova Winasis_Tugas Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VtCDFlYL9e4ktRzCp2tmcsTpxdqQQh0w
"""

# File ini Punya Andy Nova Winasis 4101421130
# Import library yang dibutuhkan
import pandas as pd
import numpy as np

# Membaca dataset yang upload
readData = pd.read_csv('movie_sample_dataset.csv')

#Menampilkan beberapa baris 5 pertama dari dataset.
readData.head()

#Ganti ? dengan NaN
readData.replace("?", np.nan, inplace=True)

#Memeriksa jumlah missing value di setiap kolom
print(readData.isnull().sum())

# Menghapus baris yang memiliki nilai kosong
forCleansingData = readData.dropna(subset=['gross', 'budget','color','director_name','genres'])
#str.capitalize() digunakan untuk mengubah huruf pertama menjadi kapital agar konsisten antara "Color" dan "color".
forCleansingData['color'] = forCleansingData['color'].str.lower()

# Hitung rata-rata gross dan budget dan mengisi sel kosong dengan rata-rata
colsToReplace = ['gross', 'budget']
for col in colsToReplace:
  avg_value=readData[col].astype(float).mean()
  readData[col].replace(np.nan, avg_value, inplace=True)
  print(f"Rata-rata {col}: {avg_value}")

# Mencari modus (nilai yang sering muncul) pada kolom director_name, color, genres
modusDirectorName = readData["director_name"].value_counts().idxmax()
modusColor = readData["color"].value_counts().idxmax()
modusGenres = readData["genres"].value_counts().idxmax()

# mengisi sel kosong nilai modus
readData["director_name"].replace(np.nan, modusDirectorName, inplace=True)
readData["color"].replace(np.nan, modusColor, inplace=True)
readData["genres"].replace(np.nan, modusGenres, inplace=True)

# Melihat modus di setiap kolom yang dibutuhkan
print(f"Nilai modus director_name: {modusDirectorName}")
print(f"Nilai modus color: {modusColor}")
print(f"Nilai modus genres: {modusGenres}")

# Membuat variabel forCleansingData sebagai salinan dari DataFrame asli (readData)
forCleansingData = readData.copy()

# Menghapus baris yang memiliki NaN di kolom gross dan budget
forCleansingData = forCleansingData.dropna(subset=['duration', 'imdb_score'])

# Filter baris dengan nilai budget dan gross yang bernilai negatif
forCleansingData = forCleansingData[(forCleansingData['duration'] >= 0) & (forCleansingData['imdb_score'] >= 0)]

# Mengubah tipe data kolom yang diperlukan
readData[["color", "director_name", "genres"]]=readData[["color", "director_name", "genres"]].astype(str)
readData[["budget", "gross"]]=readData[["budget", "gross",]].astype(float)

# Normalisasi teks ke huruf kecil
forCleansingData['color'] = forCleansingData['color'].str.lower()
forCleansingData['director_name'] = forCleansingData['director_name'].str.lower()
forCleansingData['genres'] = forCleansingData['genres'].str.lower()
forCleansingData['language'] = forCleansingData['language'].str.lower()
forCleansingData['country'] = forCleansingData['country'].str.lower()
forCleansingData['actors'] = forCleansingData['actors'].str.lower()

# Cek kapitalisasi data huruf
print(forCleansingData['color'].head())

# Menyimpan data yang telah diproses ke dalam file CSV baru
forCleansingData.to_csv('movie_dataset_cleaned.csv', index=False)