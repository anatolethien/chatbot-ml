from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import tomllib as toml
with open('config.toml', 'rb') as config_file:
    config = toml.load(config_file)

POSTGRES_DB = config.get('POSTGRES_DB')
POSTGRES_USER = config.get('POSTGRES_USER')
POSTGRES_PASSWORD = config.get('POSTGRES_PASSWORD')
SERVER = '127.0.0.1'
PORT = '5432'
CONNECTION_STRING = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{SERVER}:{PORT}/{POSTGRES_DB}'

engine = create_engine(CONNECTION_STRING)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/response', methods=['POST'])
def query():
    text = f'{request.form.get('prompt')}'
    return render_template('response.html', text=CONNECTION_STRING)
