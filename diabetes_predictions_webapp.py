# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 04:28:27 2023

@author: Bamise Omolaso
"""

# Ignore all warnings
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pickle 
import streamlit as st
import sklearn

with open('C:/Users/user/OneDrive/Documents/Everything AI/model_diabetesprediction (1).pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    
with open('C:/Users/user/OneDrive/Documents/Everything AI/quantile_transformer.pkl', 'rb') as file:
    transformer = pickle.load(file)    
    
def diabetes_prediction(input_data):
    
    #convert input data to float
    input_data_as_float = [float(value) for value in input_data]
    
    # changing the input_data to numpy array
    input_data_as_numpy_array_reshaped = np.array(input_data_as_float).reshape(1,-1)
    
    input_data_transformed = transformer.transform(input_data_as_numpy_array_reshaped)
    
    prediction = loaded_model.predict(input_data_transformed)
    
    print(prediction)
    
    if (prediction[0] == 0):
      print('The person is not diabetic')
    else:
      print('The person is diabetic')
      
      
def main():
    
    #Title
    st.title('Live Diabetes Prediction Web App')
    
    # get input data from user
    glucose = st.text_input("Glucose level (mg/dl)")
    
    bmi =  st.text_input("BMI value")
    
    age = st.text_input("Age (years)")
    
    #Code for prediction
    diagnosis = ''
    
    # create a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([glucose, bmi, age])
    
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()