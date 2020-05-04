from flask import Flask,render_template
from . import main

@main.route('/')
def index():
    '''
    my index page
    '''
    title = 'Pitch It UP'
    return render_template('index.html',title = title)
     