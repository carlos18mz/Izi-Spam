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

def predict(message, unique_words, nn):
    input = Data.get_inputs_count(message, unique_words)
    return round(nn.feedforward(input)[0,0])


@myapp.route("/")
def hello():
    return render_template('index.html')

@myapp.route('/think', methods=['GET', 'POST'])
def think2():
    global unique_words
    global nn
    
    text = request.form['message']
    result = predict(text, unique_words, nn)

    if result == 0:
        result = 'ham'
    else: result = 'spam'
    return render_template('index.html', message=result)
