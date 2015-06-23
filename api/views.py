from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from api.models import Log
from api.classes.github_manager import GithubManager
from enum import Enum
# import datetime


class LogType(Enum):
    twitter = 0
    github = 1


GITHUB_LOG_VALUE_FORMAT = '{url},{message}'


def regist_log(type, value, timestamp):
    """
    log の登録
    :param type: int
    :param value: str
    :param timestamp: int
    :return: bool 登録出来たか
    """
    type = type.value
    try:
        # ユニークなレコードであることの保証
        log = Log.objects.get(type=type, timestamp=timestamp)
        return False
    except ObjectDoesNotExist:
        log = Log(type=type, value=value, timestamp=timestamp)
        log.save()
    return True


def job(request):
    """クロールしてログデータベースの更新, 定期的に行うメインのジョブ"""
    logs = Log.objects.all()
    # regist_log(type=1, value='foo bar', timestamp=datetime.datetime.now())
    # TODO: delete debug dump
    for log in logs:
        print(log.id, log.timestamp, log.created_at)
    update_github_log()
    return HttpResponse(u'ok job page')


def update_github_log():
    """
    コミットログの更新
    :return:
    """
    gm = GithubManager()
    commits = gm.get()

    for cm in commits:
        url, message, datetime_ = cm
        # print(url, message, datetime_)
        value = GITHUB_LOG_VALUE_FORMAT.format(url=url, message=message)
        regist_log(LogType.github, value, timestamp=datetime_)
