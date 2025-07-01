import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler,LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

model= tf.keras.models.load_model("model.h5")
# Load the encoders and scaler
with open('label_encoder_gender.pkl','rb') as file:
    label_encoder_gender =pickle.load(file)
with open('b.pkl','rb') as file:
    b =pickle.load(file)
with open('scaler.pkl','rb') as file:
     scaler =pickle.load(file)

### Streamlit app
st.title("Customer Churn prediction")
### input data
geography=st.selectbox("Geography",b)