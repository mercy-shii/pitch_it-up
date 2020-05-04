from flask import Flask

@app.route('/')
def index():
    '''
    my index page
    '''
    title = 'Pitch It Up'
    return render_template('index.html',title=title)

    