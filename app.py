import datetime, math, decimal, pyrebase, urllib
import random
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session,g, abort
import pickle 
import nltkmodules

#Intento 4
from neural_network import *

unique_words_df = pd.read_csv('words.csv')
unique_words = Data.load_unique_words(unique_words_df)

with open('nn.pkl', 'rb') as output:
    nn = pickle.load(output)

myapp = Flask(__name__)



input_v = Data.get_inputs_count("PRIVATE! Your 2003 Account Statement for shows 800 un-redeemed S. I. M. points. Call 08718738002 Identifier Code: 48922 Expires 21/11/04",unique_words)


@myapp.route("/")
def hello():
    return render_template('index.html')

@myapp.route('/think', methods=['GET', 'POST'])
def think2():
    text = request.form['message']
    global unique_words
    global nn
    
    result = round(nn.feedforward(input_v)[0,0])
    if result == 0.0:
        result = 'ham'
    else: result = 'spam'
    return render_template('index.html', message=result)
