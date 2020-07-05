import urllib.request, json
from .models import newsSource

'''
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key='0ffd6c1788664312bcf394317d938e5e')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin', sources='bbc-news,the-verge', category='business', language='en', country='us')

# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin', sources='bbc-news,the-verge', domains='bbc.co.uk,techcrunch.com', from_param='2017-12-01', to='2017-12-12', language='en', sort_by='relevancy', page=2)

# /v2/sources
sources = newsapi.get_sources()
'''

api_key = None
base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['MOVIE_API_KEY']
    base_url = app.config['MOVIE_API_BASE_URL']