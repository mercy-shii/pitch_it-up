from flask import Flask,render_template,redirect,url_for
from . import main
from flask_login import login_required

@main.route('/')
def index():
    '''
    my index page
    '''
    title = 'Pitch It UP'
    return render_template('index.html',title = title)
     