import streamlit as st
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
# import seaborn as sns
# import matplotlib.pyplot as plt
# import warnings
# warnings.filterwarnings("ignore")
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
import pickle
st.title("House Price Prediction")

st.image('house.jfif', caption='Get your dream house', use_column_width=True)

# Load the model from model.pkl
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Define feature names (assuming the same order as in your original dataset)
feature_names = ['area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom',
                 'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 'furnishingstatus']

# Input fields for features
selected_area = st.number_input('Enter Area (sqft):', min_value=0.0, value=1000.0)
selected_bedrooms = st.selectbox('Select Bedrooms:', [1, 2, 3, 4, 5,6])
selected_bathrooms = st.selectbox('Select Bathrooms:', [1, 2, 3, 4])
selected_stories = st.selectbox('Select Stories:', [1, 2, 3, 4])
selected_mainroad = st.selectbox('Main Road:', ['Yes', 'No'])
selected_guestroom = st.selectbox('Guest Room:', ['Yes', 'No'])
selected_basement = st.selectbox('Basement:', ['Yes', 'No'])
selected_hotwaterheating = st.selectbox('Hot Water Heating:', ['Yes', 'No'])
selected_airconditioning = st.selectbox('Air Conditioning:', ['Yes', 'No'])
selected_parking = st.selectbox('Parking:', ['Yes', 'No'])
selected_prefarea = st.selectbox('Preferred Area:', ['Yes', 'No'])
selected_furnishingstatus = st.selectbox('Select Furnishing Status:', ['Semi-Furnished', 'Unfurnished', 'Fully Furnished'])

# Create a dictionary with selected feature values
input_data = {
    'area': selected_area,
    'bedrooms': selected_bedrooms,
    'bathrooms': selected_bathrooms,
    'stories': selected_stories,
    'mainroad': selected_mainroad,
    'guestroom': selected_guestroom,
    'basement': selected_basement,
    'hotwaterheating': selected_hotwaterheating,
    'airconditioning': selected_airconditioning,
    'parking': selected_parking,
    'prefarea': selected_prefarea,
    'furnishingstatus': selected_furnishingstatus
}

# Convert the input data into a DataFrame with appropriate data types
input_df = pd.DataFrame([input_data])

# Map selected values to match the original dataset
input_df['mainroad'] = input_df['mainroad'].map({'Yes': 1, 'No': 0})
input_df['guestroom'] = input_df['guestroom'].map({'Yes': 1, 'No': 0})
input_df['basement'] = input_df['basement'].map({'Yes': 1, 'No': 0})
input_df['hotwaterheating'] = input_df['hotwaterheating'].map({'Yes': 1, 'No': 0})
input_df['airconditioning'] = input_df['airconditioning'].map({'Yes': 1, 'No': 0})
input_df['parking'] = input_df['parking'].map({'Yes': 1, 'No': 0})
input_df['prefarea'] = input_df['prefarea'].map({'Yes': 1, 'No': 0})
input_df['furnishingstatus'] = input_df['furnishingstatus'].map({'Semi-Furnished': 1, 'Unfurnished': 2, 'Fully Furnished': 0})

# Make predictions using the loaded model
predictions = loaded_model.predict(input_df)

# Display the prediction
st.write('Estimates House Price:', predictions[0],"RS")

