# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 12:43:50 2025

@author: MALLIKA SANTRA
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#loading the saved model
loaded_model = pickle.load(open('C:/Users/MALLIKA SANTRA/OneDrive/Desktop/DeployMachineLearning/trained_model.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', ['Heart Disease Prediction','Diabetes Prediction','Dengue Prediction'],
                           icons=['person-heart','activity','thermometer-half'],default_index=0)
    

#creating a function for prediction

def heartdiseases_prediction(input_data):
    
    #change the input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
     return "The person do not have Heart disease"
    else:
      return"The person has Heart Disease "
    
    
def main():
    
   #giving a title 
   st.title('Heart Diseases Prediction')
    
   #getting the input data from the user
   # age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,target
   
   col1,col2,col3 = st.columns(3)
   with col1:
       age = st.text_input("Age")
   with col2:
       sex = st.text_input("Sex(1 = male; 0 = female)")
   with col3:
       cp = st.text_input("chest pain type (4 values[0,1,2,3])")
   with col1:
       trestbps = st.text_input("resting blood pressure (in mm Hg)")
   with col2:
       chol = st.text_input("serum cholestoral in mg/dl")
   with col3:
       fbs = st.text_input("fasting blood sugar > 120 mg/dl")
   with col1:
       restecg = st.text_input("resting electrocardiographic results (values 0,1,2)")
   with col2:
       thalach = st.text_input("maximum heart rate achieved")
   with col3:
       exang = st.text_input("exercise induced angina (1 = yes; 0 = no)")
   with col1:
       oldpeak = st.text_input("ST depression induced by exercise ")
   with col2:
       slope = st.text_input("Slope of the peak exercise ST segment")
   with col3:
       ca = st.text_input("Major vessels colored by flourosopy")
   with col1:
       thal = st.text_input("thal:0=normal;1= fixed detect;2=reversable defect")
   
   
   #code for prediction
   diagnosis =''
   
   col4,col5,col6 = st.columns([1,1,1])
   with col5:
       
   # creating a button for prediction
       if st.button('Heart Diseases Test Result'):
           diagnosis = heartdiseases_prediction([float(age), int(sex), int(cp), float(trestbps), float(chol),
                  int(fbs), int(restecg), float(thalach), int(exang),
                  float(oldpeak), int(slope), int(ca), int(thal)])
           
   st.success(diagnosis)

if __name__=='__main__':
    main()
        
    