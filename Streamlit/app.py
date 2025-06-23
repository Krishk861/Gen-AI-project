import numpy as np
import pandas as pd
import streamlit as st
st.title("Hello Streamlit")
df=pd.DataFrame({"first column": [1,2,3,4]
                 ,"Second column": [20,25,40,37]
                 })
st.write(df)
st.write("The dataframe is displayed above")
#### Chart
chart_data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart_data)