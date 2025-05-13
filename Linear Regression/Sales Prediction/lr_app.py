import streamlit as st
import pandas as pd
import numpy as np
import sklearn
import pickle

model = pickle.load(open('Linear_Regression_model.pkl', 'rb'))

st.title('Sales Prediction App')
st.markdown('This app predicts the sales of a product based on its advertisements.')

tv = st.number_input('TV Advertisement Budget', min_value=0, max_value=500, value=1, step=10)
radio = st.number_input('Radio Advertisement Budget', min_value=0, max_value=500, value=1, step=10)
newspaper = st.number_input('Newspaper Advertisement Budget', min_value=0, max_value=500, value=1, step=10)

if st.button('Predict Sales'):
    input_data = np.array([[tv, radio, newspaper]])
    prediction = model.predict(input_data)
    st.success(f'The predicted sales are: ${prediction[0]:,.2f}')
   # st.balloons()
  #  st.image('https://media.giphy.com/media/3o7aTnq2j0v1x4g5iY/giphy.gif', use_column_width=True)