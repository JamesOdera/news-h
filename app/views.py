from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = 'WELCOME TO NEWS HIGHLIGHT APP'
    return render_template('index.html',message = message)

@app.route('/sources/<int:sources_id>')
def sources(sources_id):

    '''
    View sources page function that returns the sources details page and its data
    '''
    return render_template('sources.html',id = sources_id)