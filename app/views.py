from flask import Flask,render_template
from app import app

@app.route('/')
def index():
    '''
    my index page
    '''
    return render_template('index.html')
     