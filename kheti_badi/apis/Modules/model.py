import pickle
import numpy as np
import pandas as pd
from sklearn import *
import os 

pd.set_option('display.max_columns', None)
path=os.path.join(os.path.dirname(os.path.dirname(__file__)),
                           'Modules/knn_model.pkl')
clf=pickle.load(open(path, 'rb'))


def predict(in_data):

    soil_arr=pd.DataFrame(["sandy","loamy","black","red","clayey"])
    soil_arr.loc[len(soil_arr.index)] = in_data[3].lower()
    # print(soil_arr)
    crop_arr=pd.DataFrame(["maize","sugarcane","cotton","tobacco","paddy","barley","wheat","millets","oil seeds","pulses","ground nuts"])
    crop_arr.loc[len(crop_arr.index)] = in_data[4].lower()
    # print(crop_arr)
    soil_encoded=pd.get_dummies(soil_arr)
    crop_encoded=pd.get_dummies(crop_arr)
    soil_encoded=soil_encoded.drop([0,1,2,3,4],axis=0)
    soil_encoded=soil_encoded.reset_index()
    soil_encoded=soil_encoded.drop(['index'],axis=1)
    crop_encoded=crop_encoded.drop([0,1,2,3,4,5,6,7,8,9,10],axis=0)
    crop_encoded=crop_encoded.reset_index() 
    crop_encoded=crop_encoded.drop(['index'],axis=1)
    print(crop_encoded)

    df=pd.DataFrame(columns=['Temp','Humidity','Moisture','soil_type','crop_type','Nitrogen','Potassium','Phosphorous'])
    print(df)
    df.loc[len(df.index)] = in_data
    print(df)
    df=df.join(soil_encoded)
    print(df.head())
    df=df.join(crop_encoded)
    df=df.drop(['soil_type','crop_type'],axis=1)
    print(df.head())

    pr=clf.predict(df)
    map={'10-26-26': 0, '14-35-14': 1, '17-17-17': 2, '20-20': 3, '28-28': 4, 'DAP': 5, 'Urea': 6}
    prediction=list(map.keys())[list(map.values()).index(pr)]   
    return prediction
