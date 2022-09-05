# =========================================
# Transformer translation en-est (frontend)
# Author: Anastasia Korobkina
# Last Modified: 5 Sep 2022
# =========================================
# Command to execute script locally: streamlit run app.py
# Command to run Docker image: docker run -d -p 8501:8501 <streamlit-app-name>:latest

import streamlit as st
import requests
import pandas as pd
import io
import json

st.title('Translator v 0.19')

# Set FastAPI endpoint
# endpoint = 'http://localhost:8000/predict'
endpoint = 'http://host.docker.internal:8000/predict' # Specify this path for Dockerization to work

user_input_string = st.text_input(label='Insert your sentence in English', value='Hello fuck brother')

if user_input_string:
    file_dict = {'text': user_input_string}
    files = json.dumps(file_dict)

    if st.button('Translate'):
        if len(user_input_string) == 0 or len(user_input_string.strip()) == 0:
            st.write("Please insert a valid text")  
        else:
            with st.spinner('Translation in progress. Please wait...'):
                output = requests.post(endpoint, 
                                       json=files,
                                       timeout=8000)
            st.write('Success! Super translation is here')
            st.success(output.json())
