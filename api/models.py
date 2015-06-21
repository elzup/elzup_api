from django.db import models


class Log(models.Model):
    """ログ"""
    created_at = models.DateTimeField(auto_now_add=True, unique=True)
    type = models.SmallIntegerField()
    value = models.TextField()
    timestamp = models.DateTimeField()