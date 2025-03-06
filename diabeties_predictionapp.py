
"""
Created on Thu Mar  6 20:10:18 2025

@author: ghora
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open("C:/Users/ghora/Desktop/cancer_prediction/trained_model (1).sav", 'rb'))

# creating a function for prediction

def diabeties_prediction(input_data):
    #input_data = (5,166,72,19,175,25.8,0.587,51)
    # changing the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    # now we need to standarize the input data



    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if prediction[0] == 0:
      return'The person is not diabetic'
    else:
      return'The person is diabetic'
      

def main():
    # giving a title
    st.title("diabeties prediction web app")
    
    # input part
    
    Pragnancies= st.text_input("number of pragnancies")
    Glucose= st.text_input("enter the glucose level")
    Bloodpressure= st.text_input("enter the blood pressure")
    Skinthickness= st.text_input("enter the slinthickness")
    Insulin= st.text_input("enter the insulin level")
    BMI= st.text_input("enter the bmi level")
    Diabetespedigreefunction= st.text_input("enter the DPF")
    Age= st.text_input("enter the age")
    
    # code for prediction 
    diagosis= ' '
    
    # creating a button for prediction
    if st.button('Diabetis test result'):
        diagosis= diabeties_prediction([Pragnancies,Glucose,Bloodpressure,Skinthickness,Insulin, BMI,Diabetespedigreefunction,Age])
        
    st.success(diagosis)
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
