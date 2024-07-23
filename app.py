import pickle
import streamlit as st
import numpy as np

# Function to load the model
def load_model():
    try:
        with open('model_file.pkl', 'rb') as model_file:
            model = pickle.load(model_file)
        # Ensure the loaded object is a model with a predict method
        if not hasattr(model, 'predict'):
            st.error("The loaded object is not a valid model. Please check the model file.")
            st.stop()
    except FileNotFoundError:
        st.error("Model not found, please ensure the model path is correct.")
        st.stop()
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        st.stop()
    return model

# Load the model
model = load_model()

# Streamlit app title
st.title('Prediksi Jumlah Produksi Padi di Sumatera dengan Algoritma Regresi')

# Input fields for user to provide the necessary data
provinsi = st.selectbox('Pilih Nama Provinsi', 
                        ('Aceh', 'Sumatera Utara', 'Sumatera Barat', 'Riau', 'Jambi', 
                         'Sumatera Selatan', 'Bengkulu', 'Lampung', 'Kepulauan Bangka Belitung', 
                         'Kepulauan Riau'))
tahun = st.number_input('Input Tahun Produksi yang akan Diprediksi', min_value=2000, max_value=2100, step=1)
luas_panen = st.number_input('Input Luas Panen Padi (hektar)', min_value=0.0, step=0.1)
curah_hujan = st.number_input('Input Curah Hujan (mm)', min_value=0.0, step=0.1)
kelembapan = st.number_input('Input Kelembapan (%)', min_value=0.0, max_value=100.0, step=0.1)
suhu_rata_rata = st.number_input('Input Suhu Rata-Rata (°C)', min_value=-50.0, max_value=50.0, step=0.1)

# Button to make prediction
if st.button('Prediksi'):
    # Prepare features for prediction
    try:
        features = np.array([[luas_panen, curah_hujan, kelembapan, suhu_rata_rata]])
        # Make prediction
        prediction = model.predict(features)
        # Display the prediction
        st.success(f'Prediksi Jumlah Produksi Padi di {provinsi} pada tahun {tahun} adalah {prediction[0]:.2f} ton')
    except Exception as e:
        st.error(f"Error during prediction: {e}")

# Information about the application
st.write("""
# Aplikasi Prediksi Jumlah Produksi Padi
Aplikasi ini menggunakan model regresi yang sudah dilatih untuk memprediksi jumlah produksi padi di berbagai provinsi di Sumatera berdasarkan data luas panen, curah hujan, kelembapan, dan suhu rata-rata.
""")
