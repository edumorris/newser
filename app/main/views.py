from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news
from ..models import newsArticles

# Views
@main.route('/')
def index():
    '''
    View to return the homepage
    '''

    # Get Local Kenyan news
    local_news = get_news('Kenya')
    print(local_news)

    title = "All News"
    return render_template('index.html', title = title, news = local_news)

