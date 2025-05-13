import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("NumeraLab: Sayısal Analiz Asistanı")

feature = st.sidebar.radio("Bir özellik seçin:", ["Özellik 1: Denklemden Sayısal Çözüm",
                                                  "Özellik 2: Şekilden Denklem Üretimi"])

if feature == "Özellik 1: Denklemden Sayısal Çözüm":
    st.header("Denklemden Sayısal Çözüm")
    equation = st.text_input("Denkleminizi girin:")
    if st.button("Çözümle"):
        st.write(f"Girilen denklem: {equation}")
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        st.line_chart(y)

elif feature == "Özellik 2: Şekilden Denklem Üretimi":
    st.header("Şekilden Denklem Üretimi")
    uploaded_file = st.file_uploader("Bir görsel yükleyin", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Yüklenen Görsel")
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        st.line_chart(y)
        st.success("Örnek çıktı: y ≈ sin(x)")
