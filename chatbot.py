from flask import Flask, render_template, jsonify, request
import json
import os
import pandas as pd

df = pd.read_csv('finances.csv')
print(df)
#print(df.loc[0])

# Create a Flask application instance
# in web browser enter: localhost:5500
# created an instance of the class
#app = Flask(__name__)

# we use route() to tell Flask what URL should trigger our function
# Flask provides a render_template() function that allows use of the Jinja template engine 
#@app.route('/')
#def index():
    #return render_template('index.html')


def simple_chatbot():
    company_input = input("What company are you interested in?\n")
    year_input = input("What year are you interested in?\n")
    user_query = input("What is your question?\n")
    TotalRevenue = df.loc[(df['Company'] == company_input)  , 'Total Revenue']
    print(TotalRevenue)
    if user_query == "What is the Total Revenue?\n":
        return f"The total revenue is {TotalRevenue}.\n"
    elif user_query == "How has the net income changed over the last year?\n":
        return "The net income has [increased/decreased] by [percentage].\n"
    else: 
        return "I'm sorry, I don't have the answer to your question."


simple_chatbot()

