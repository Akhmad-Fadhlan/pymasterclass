import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data contoh
x = np.linspace(0, 10, 100)
y = np.sin(x)

showPyplotGlobalUse = false
# Fungsi untuk membuat grafik garis
def create_line_chart():
    plt.plot(x, y)
    plt.xlabel("Sumbu X")
    plt.ylabel("Sumbu Y")
    plt.title("Contoh Grafik Garis")
    st.pyplot()


# Fungsi untuk membuat grafik scatter
def create_scatter_chart():
    plt.scatter(x, y, color="red")
    plt.xlabel("Sumbu X")
    plt.ylabel("Sumbu Y")
    plt.title("Contoh Grafik Scatter")
    st.pyplot()


# Fungsi untuk membuat grafik batang
def create_bar_chart():
    categories = ["Kategori A", "Kategori B", "Kategori C", "Kategori D", "Kategori E"]
    values = [3, 7, 1, 8, 4]

    plt.bar(categories, values, color="green")
    plt.xlabel("Kategori")
    plt.ylabel("Nilai")
    plt.title("Contoh Grafik Batang")
    st.pyplot()


# Aplikasi Streamlit
def main():
    st.title("Aplikasi Streamlit dengan Matplotlib")

    st.write("Pilih model grafik untuk ditampilkan:")
    chart_type = st.selectbox("Model Grafik:", ["Garis", "Scatter", "Batang"])

    if chart_type == "Garis":
        create_line_chart()
    elif chart_type == "Scatter":
        create_scatter_chart()
    elif chart_type == "Batang":
        create_bar_chart()


if __name__ == "__main__":
    main()
