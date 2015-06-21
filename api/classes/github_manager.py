import feedparser

class GithubManager:

    RSS_URL = 'https://github.com/elzzup.atom'

    def __init__(self):
        pass

    def get(self):
        # TODO: rss manage
        feed = feedparser.parse(self.RSS_URL)
        print(feed.feed.title)
