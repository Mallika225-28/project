# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

#loading the saved model
loaded_model = pickle.load(open('C:/Users/MALLIKA SANTRA/OneDrive/Desktop/DeployMachineLearning/trained_model.sav','rb'))

input_data = (38,1,2,138,175,0,1,173,0,0,2,4,2)
#change the input data into numpy array
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
  print("The person do not have hearst disease")
else:
  print("The person has Heart Disease ")