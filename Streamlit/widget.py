import streamlit as st
import pandas as pd
st.title("Streamlit text input")
name=st.text_input("Enter your name :")
if name:
    st.write(f"How are you Mr./Mrs. {name}")
age=st.slider("Select your age",0,100,25)
st.write =({age})
df=pd.DataFrame({"Name":["Krish","SUnny","Ayush"],
                 "Marks obtained":[95,93,79]})
marks_obtained=st.write(df)