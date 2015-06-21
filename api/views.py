from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from api.models import Log
import datetime


def regist_log(type, value, timestamp):
    """
    log の登録
    :param type: int
    :param value: str
    :param timestamp: int
    :return: bool 登録出来たか
    """
    try:
        # ユニークなレコードであることの保証
        log = Log.objects.get(type=type, value=value, timestamp=timestamp)
        return False
    except ObjectDoesNotExist:
        log = Log(type=type, value=value, timestamp=timestamp)
        log.save()
    return True


def job(request):
    """クロールしてログデータベースの更新, 定期的に行うメインのジョブ"""
    logs = Log.objects.all()
    regist_log(type=1, value='foo bar', timestamp=datetime.datetime.now())
    for log in logs:
        print(log.id, log.timestamp, log.created_at)
    return HttpResponse(u'ok job page')


def udpate_github():
    """
    コミットログの更新
    :return:
    """
    # TDOO: ログ
    pass

