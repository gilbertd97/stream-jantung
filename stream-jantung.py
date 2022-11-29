import pickle
import streamlit as st 


#membaca model
model = pickle.load(open('penyakit_jantung.sav', 'rb'))


#judul web
st.title('Data Mining Prediksi Penyakit Jantung')

#columns
col1, col2 = st.columns(2)

#kriteria
with col1 :
    age = st.number_input ('Input nilai Age')
with col1 :
    anaemia = st.number_input ('Input nilai Anaemia')
with col1 :
    creatinine_phosphokinase = st.number_input ('Input nilai Creatinine Phosphokinase')
with col1 :
    diabetes = st.number_input ('Input nilai Diabetes')
with col1 :
    ejection_fraction = st.number_input ('Input nilai Ejection Fraction')
with col1 :
    high_blood_pressure = st.number_input ('Input nilai High Blood Pressure')
with col2 :
    platelets = st.number_input ('Input nilai Platelets')
with col2 :
    serum_creatinine = st.number_input ('Input nilai Serum Creatinine')
with col2 :
    serum_sodium = st.number_input ('Input nilai Serum Sodium')
with col2 :
    sex = st.number_input ('Input nilai Sex (0 = Laki Laki, 1 = Perempuan)')
with col2 :
    smoking= st.number_input ('Input nilai Smoking (0 = Merokok, 1 = Tidak Merokok)')
with col2 :
    time = st.number_input ('Input nilai Time')

#prediksi 
heart_diag = ''

#tombol prediksi
if st.button ('Test Prediksi Penyakit Jantung'):
    heart_prediction = model.predict([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])

    if (heart_prediction[0] == 1):
            heart_diag = 'Pasien Terkena Penyakit Jantung' 
    else :
            heart_diag = 'Pasien Tidak Terkena Penyakit Jantung'

st.success(heart_diag)
