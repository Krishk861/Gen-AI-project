## loading the program
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model

word_index= imdb.get_word_index()
reverse_word_index = {value:key for key,value in word_index.items()}

model = load_model("SimpeRNN_imdb.h5")

 ###Function to preprocess user input
 ##helper functions

def decoded_review(encoded_review):
    return " ".join([reverse_word_index.get(i - 3, "?" ) for i in encoded_review])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word,2)+3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
    return padded_review

### Step 3: Creating prediction function

def predict_sentment(review):
    preprocessed_input=preprocess_text(review)

    prediction =model.predict(preprocessed_input)
    sentiment ="Postive" if prediction[0][0]> 0.5 else "Negative"

    return sentiment,prediction[0][0]

### Streamlit app
import streamlit as st
st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to classify it sas positive or negative")

##User input
user_input= st.text_area("Please give the movie review")
if st.button("Classify"):

    prepreocess_input=preprocess_text(user_input)

    prediction=model.predict(prepreocess_input)
    sentiment="Positive" if prediction[0][0] >0.5 else "negative"

    st.write(f"Sentiment: {sentiment}")
    st.write(f"Prediction score: {prediction[0][0]}")
else:
    st.write("please enter a movie review")