import nltk
import streamlit as st
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from langid.langid import LanguageIdentifier, model
import langid

nltk.download("all")
nltk.download("averaged_perceptron_tagger")

st.set_page_config(
    page_title="Analisis Sentimen",
    initial_sidebar_state="expanded",
)


def get_sentiment(value):
    if value > 0:
        return "😀 Positif"
    elif value < 0:
        return "😏 Negatif"
    else:
        return "😐 Netral"


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


st.title("😀 Analisis Sentimen 😒")

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

    st.subheader("Sentimen:")
    st.write(get_sentiment(blob.sentiment.polarity))

    if blob.sentiment.subjectivity > 0.5:
        st.write("Opini pribadi: ✅")
    else:
        st.write("Opini Pribadi: ❌")

    st.write(blob.sentiment)

    st.subheader(f"Kalimat: {len(blob.sentences)}")
    st.write(blob.sentences)

    st.subheader(f"Noun Phrase: {len(blob.noun_phrases)}")
    st.write(blob.noun_phrases)

    st.subheader(f"Kata: {len(blob.words)}")
    st.write(blob.words)

    st.subheader(f"Lematisasi: {len(blob.words)}")
    for item in blob.tags:
        if item[1] == "NN":
            st.write(item[0], "-->", item[1], "-->", item[0].pluralize())
        elif item[1] == "NNS":
            st.write(item[0], "-->", item[1], "-->", item[0].singularize())
        else:
            st.write(item[0], "-->", item[1], "-->", item[0].lemmatize())

    st.subheader(f"Tags:")
    st.write(blob.tags)

    st.subheader("Sentiment Berdasarkan Kalimat:")
    for sentence in blob.sentences:
        st.write(get_sentiment(sentence.sentiment.polarity), sentence)

    st.subheader(f"Koreksi ejaan:")
    st.write(blob.correct())

    st.subheader("TF-IDF Features:")
    tfidf_features = extract_tfidf_features(text)
    st.write(tfidf_features)
