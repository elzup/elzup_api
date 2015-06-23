import feedparser
from bs4 import BeautifulSoup

class GithubManager:

    RSS_URL = 'https://github.com/elzzup.atom'

    def __init__(self):
        self.feed = feedparser.parse(self.RSS_URL)
        pass

    def get(self):
        # TODO: rss manage
        for item in self.feed.entries:
            # NOTE: 完全な判別が出来ていなくて少々危ない
            # NOTE: rss のHTML構造が変わらない限り有効
            if 'pushed' in item.title:
                print(item)
                text = item.description
                soup = BeautifulSoup(text)
                li = soup.find(class_='more')
                if not li:
                    return
                GithubManager.crawl_commits(li.a['href'])

    @staticmethod
    def crawl_commits(url):
        # TODO: commit page のスクレイプ
        print(url)
