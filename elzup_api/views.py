from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from elzup_api.models import Log


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
        pos = Log.objects.get(type=type, value=value, timestamp=timestamp)
        return False
    except ObjectDoesNotExist:
        pos = Log(type=type, value=value, timestamp=timestamp)
        pos.save()
    return True


def job(request):
    """クロールしてログデータベースの更新, 定期的に行うメインのジョブ"""
    # TODO:
    return HttpResponse(u'ok job page')


def udpate_github():
    """
    コミットログの更新
    :return:
    """
    # TDOO: ログ
    pass
