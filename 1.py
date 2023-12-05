import streamlit as st
from textblob import TextBlob
import langid

st.set_page_config(
    page_title="Analisis Sentimen",
    page_icon="😀",
    initial_sidebar_state="expanded"
)

d1 = "saya pergi kekampus"
d2 = "menggunakan motor"
d3 = "saya pergi jam 7.40"
d4 = "saya sampai jam 7.55"
d5 = "setelah itu masuk ke ruang kelas"
d6 = "dan saya duduk"
d7 = "lalu membeli pempek kiran"
d8 = "karena saya tdk sarapan"
d9 = "jadi saya kelaparan"
d10 = "saya membeli 3 bijiii"
d_string = f"{d1} {d2} {d3} {d4} {d5} {d6} {d7} {d8} {d9} {d10}"
print(d_string)

d_semua = d1.split() + d2.split() + d3.split() + d4.split() + d5.split() + d6.split() + d7.split() + d8.split() + d9.split() + d10.split()
d_list = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
print (d_semua)

kamus_kata ={}
for data in d_semua :
  kamus_kata[data] = d_string.count (data)
  print(kamus_kata)

#Tf
data_dict = {}
data_list = []
for kalimat in d_list :
  for kata in d_semua :
    data_dict[kata] = kalimat.count(kata)
  data_list.append(data_dict)
  data_dict = {}
  print (data_list)
  
print("Term frequency")
for i in range(len (data_list)):
  print(f"data {i} : {data_list[i]}")

print("Term frequency")
for i in range(len (data_list)):
  print(f"Data {i+1} : {data_list[i]}")

#IDF
import math
data_idf = {}
for kata in kamus_kata :
  hitung = math.log(len(d_list)/kamus_kata[kata],10)
  data_idf[kata] = hitung
print(data_idf)

#TFIDF
hasil = []
data_sementara = {}
for index in range (len(data_list)):
  for i in data_list[index] :
    hitung = data_list [index] [i] * data_idf[i]
    data_sementara[i] = round (hitung, 3)
  hasil.append(data_sementara)
  data_sementara = {}
print(hasil)
