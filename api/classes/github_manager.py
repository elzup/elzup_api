import feedparser
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

class GithubManager:

    GITHUB_URL = 'https://github.com/'
    RSS_URL_FORMAT = GITHUB_URL + '{user}.atom'
    GITHUB_USER_NAME = 'elzzup'

    def __init__(self):
        self.feed = feedparser.parse(self.rss_url())

    def rss_url(self):
        return self.RSS_URL_FORMAT.format(user=self.GITHUB_USER_NAME)

    def get(self):
        all_commits = []
        for item in self.feed.entries:
            # NOTE: 完全な判別が出来ていなくて少々危ない
            # NOTE: rss のHTML構造が変わらない限り有効
            if 'pushed' in item.title:
                text = item.description
                soup = BeautifulSoup(text)
                li = soup.find(class_='more')
                if not li:
                    continue
                commits = GithubManager.crawl_commits(li.a['href'])
                all_commits.extend(commits)
        return all_commits

    @staticmethod
    def crawl_commits(url):
        commits = []
        soup = BeautifulSoup(urlopen(url))
        commit_list = soup.find(class_='commits-listing')
        for tr in commit_list.find_all('tr'):
            a = tr.find(class_='commit-id')
            commit = GithubManager.craw_commit(GithubManager.GITHUB_URL + a['href'])
            commits.append(commit)
            # hash値は取得しない
        # NOTE: 構造が抽象的なデータの受け渡しになっている
        return commits

    @staticmethod
    def craw_commit(url):
        soup = BeautifulSoup(urlopen(url))
        message = soup.find(class_='commit-title').text.strip()
        # NOTE: datetime の文字列に含まれる T, Z がなんなのかわからない
        datetime_ = datetime.strptime(soup.time['datetime'], '%Y-%m-%dT%H:%M:%SZ')
        # NOTE: 構造が抽象的なデータの受け渡しになっている
        return [url, message, datetime_]
