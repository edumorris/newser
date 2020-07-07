from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news, search_news, get_news_category
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

    news_split = news_search.split(" ")
    news_format = "+".join(news_split)
    searched_news = search_news(news_format)
    title = f'News for {{ news_search }}'

    new_search = request.args.get('news_query')

    if new_search:
        return redirect(url_for('.search', news_search = new_search))
    else:
        # return render_template('index.html', title = title, news = local_news)
        return render_template('search.html', news = searched_news)

@main.route('/category/<topic>')
def news(topic):
    '''
    View function for different categories
    '''

    category = get_news_category(topic)
    title = f'Category: { topic }'

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('.search', news_search = search_news))
    else:
        # return render_template('index.html', title = title, news = local_news)
        return render_template('category.html', title = title, cat = category)

