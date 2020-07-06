import urllib.request, json
from .models import newsArticles


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
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_BASE_URL']

def get_news(category):
    '''
    Gets API response from the news API
    '''

    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url_resp:
        get_news_data = url_resp.read()
        get_news_response = json.loads(get_news_data)

        news_data = None

        if get_news_response['articles']:
            news_data_list = get_news_response['articles']
            news_data = process_results(news_data_list)
    
    return news_data

def process_results(news_list):
    '''
    Transforms received data to list of objects
    '''

    news_data = []
    for news in news_list:
        source = news.get('source.name')
        author = news.get('source.name')
        title = news.get('title')
        description = news.get('description')
        url = news.get('url')
        imageUrl = news.get('urlToImage')
        publish_time = news.get('publishedAt')
        content = news.get('content')

        if url:
            news_object = newsArticles(source, author, title, description, url, imageUrl, publish_time, content)
            news_data.append(news_object)
    
    return news_data