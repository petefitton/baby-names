from flask import Flask, render_template, request
import pandas as pd
import data_analysis as analysis

app = Flask(__name__)

data_file = './data/names.csv'

@app.route('/', methods=['GET', 'POST' ])
def baby_name():
  if request.method == 'GET':
    return render_template('index.html')
  else:
    return render_template('dataResults.html', data=analysis.export(data_file))