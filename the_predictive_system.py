# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# Loading the saved model
loaded_model = pickle.load(open('C:/Users/temp/AI Credit Card Fraud detection proj/trained_fraud_model.sav', 'rb'))

input_data = (15.0190426448825,0.0238643075434555,0.503276157986172,1,0,0,0)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
result = loaded_model.predict(input_data_reshaped)

if result[0] == 0:
    print("No Fraud")
elif result[0] == 1:
    print("Fraud")