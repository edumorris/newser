from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, search_news
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

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.search', news_search = search_news))
    else:
        return render_template('index.html', title = title, news = local_news)

@main.route('/search/<news_search>')
def search(news_search):
    '''
    View function to display search results
    '''

    searched_news = get_news(news_search)
    title = f'News for {{ news_search }}'
    return render_template('search.html', news = searched_news)

