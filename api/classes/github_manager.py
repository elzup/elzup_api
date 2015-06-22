import feedparser

class GithubManager:

    RSS_URL = 'https://github.com/elzzup.atom'

    def __init__(self):
        pass

    def get(self):
        # TODO: rss manage
        feed = feedparser.parse(self.RSS_URL)
        for item in feed['entries']:
            # NOTE: 完全な判別が出来ていなくて少々危ない
            if 'pushed' in item.title:
                print(item)
                v = item.value
                # TODO: commit の分解
                print(type(v))
                print(v)

