class newsArticles:
    '''
    Class defining articles
    '''
    
    def __init__(self, source, author, title, description, url, image_url, publish_time, content):
        self.source = source # Name of the source of news
        self.author = author # Author of the news article
        self.title = title # Title of the news article
        self.description = description # Snippet of the news article
        self.url = url # URL to the news article
        self.image_url = image_url # URL for the news article image
        self.publish_time = publish_time # Publication date of the news article
        self.content = content # Content of the article

class newsSource:
    '''
    Class defining news sources
    '''
    pass