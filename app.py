import nltk
import streamlit as st
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from langid.langid import LanguageIdentifier, model
import langid

nltk.download("all")
nltk.download("averaged_perceptron_tagger")

st.set_page_config(
    page_title="Analisis TF-TDF",
    initial_sidebar_state="expanded",
)


def deteksi_bahasa(text):
    lang, _ = langid.classify(text)
    return lang


def extract_tfidf_features(text):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text])
    feature_names = vectorizer.get_feature_names_out()
    tfidf_values = tfidf_matrix.todense().tolist()[0]

    features = dict(zip(feature_names, tfidf_values))
    sorted_features = dict(sorted(features.items(), key=lambda x: x[1], reverse=True))

    return sorted_features


st.title(" Analisis TF_idf ")

st.caption(
    """ Analisis Sentimen adalah teknik pemrosesan bahasa alami yang digunakan untuk mendeteksi sentimen negatif, positif dan netral.
Simak terus ya fren, agar tidak terjadi kesalahpahaman.
"""
)

text = st.text_input("Masukan teks", "semoga saya bisa, aamiinallahumaaamiin")

bahasa = deteksi_bahasa(text)

if bahasa == "en":
    st.warning(f"Deteksi bahasa: {bahasa}. Hanya mendukung bahasa Indonesia.")
else:
    blob = TextBlob(text)

    st.subheader("TF-IDF Features:")
    tfidf_features = extract_tfidf_features(text)
    st.write(tfidf_features)

    word_counts = blob.word_counts

    # Menampilkan jumlah kemunculan setiap kata
    st.subheader("Jumlah Kemunculan Setiap Kata:")
    st.write(word_counts)
