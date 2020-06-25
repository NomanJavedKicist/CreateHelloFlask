from flask import Flask
from HelloFlask import app

@app.route('/')
@app.route('/home')
def home():
    return "Creating Branch!"
