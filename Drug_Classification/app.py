import streamlit as st
import pandas as pd
import pickle
st.title("MEDICINE PREDICTION")

st.image('medicine.jfif', use_column_width=True)

with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

feature_names = ['Age','Sex','BP','Cholesterol','Na_to_K']
selected_age = st.number_input('Please Enter Age (in yrs):', min_value=0)
selected_sex = st.selectbox('Sex:', ['Male', 'Female'])
selected_BP = st.selectbox('BP Level',['Low','Normal','High'])
selected_cholesterol = st.selectbox('Cholesterol Level',['High','Normal'])
selected_Na_to_K = st.number_input('Please Enter the Na_to_K level (from 5 to 40)', min_value =5,max_value=40)

input_data= {
    'Age': selected_age,
    'Sex': selected_sex,
    'BP': selected_BP,
    'Cholesterol': selected_cholesterol,
    'Na_to_K': selected_Na_to_K
}

input_df = pd.DataFrame([input_data])

input_df['Sex'] = input_df['Sex'].map({'Male': 1, 'Female': 0})
input_df['BP'] = input_df['BP'].map({'Low':0,'Normal':1,'High':2})
input_df['Cholesterol'] = input_df['Cholesterol'].map({'High':1,'Normal':0})

predictions = loaded_model.predict(input_df)

st.write('Estimates Drug:', predictions[0])