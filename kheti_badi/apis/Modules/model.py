import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
model=pickle.dumps("knn_model.pkl")
clf=pickle.loads(model)
def predict(soil_type,crop_type):
    soil_arr=pd.DataFrame(["sandy","loamy","black","red","clayey"])
    soil_arr.loc[len(soil_arr.index)] = soil_type.lower()
    print(soil_arr)
    crop_arr=pd.DataFrame(["maize","sugarcane","cotton","tobacco","paddy","barley","wheat","millets","oil seeds","pulses","ground nuts",crop_type])
    print(crop_arr)
    soil_encoded=pd.get_dummies(soil_arr)
    crop_encoded=pd.get_dummies(crop_arr)

    soil_type=soil_encoded.loc[len(soil_encoded.index)-1]
    crop_type=crop_encoded.loc[len(soil_encoded.index)-1]
predict("abc","abc")