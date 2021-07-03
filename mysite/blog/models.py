from django.db import models
from django.utils import timezone # djangoで日付を管理するためのモジュール

# Create your models here.
class Post(models.Model):
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    date = models.DateTimeField('日付', default=timezone.now)

    def __str__(self) -> str: # Postモデルが直接呼び出されたときに返す値を定義
        return self.title # 記事タイトルを返す