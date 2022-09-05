# ===========================
# Transformer translation en-est (backend)
# Author: Anastasia Korobkina
# Last Modified: 5 Sep 2022
# ===========================
# Command to execute script locally: uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# Command to run Docker image: docker run -d -p 8000:8000 <fastapi-app-name>:latest

import pandas as pd
import io
from src.model import TransformerTranslator


from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, HTMLResponse

import json


# Create FastAPI instance
app = FastAPI()

model = TransformerTranslator()

@app.post("/predict")
async def predict(request: Request):
    str_input = json.loads(await request.json())['text']
    translated_text = model.translate(str_input)
    json_compatible_item_data = jsonable_encoder(translated_text)
    return JSONResponse(content=json_compatible_item_data)

@app.get("/")
async def main():
    content = """
    <body>
    <h2> Welcome to the project for english-estonian translation using Helsinki-NLP model</h2>
    <p> The transformer model and FastAPI instances have been set up successfully </p>
    <p> You can view the FastAPI UI by heading to localhost:8000 </p>
    <p> Proceed to initialize the Streamlit UI (frontend/app.py) to submit translation requests </p>
    </body>
    """
    # content = """
    # <body>
    # <form action="/predict/" enctype="multipart/form-data" method="post">
    # <input name="file" type="file" multiple>
    # <input type="submit">
    # </form>
    # </body>
    # """
    return HTMLResponse(content=content)