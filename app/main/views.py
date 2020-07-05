from flask import render_template, request, redirect, url_for
from . import main
# from ..requests import newsArticles, newsSource
from ..models import newsSource, newsArticles

# Views
@main.route('/')
def index():
    '''
    View to return the homepage
    '''

    return render_template('index.html')

