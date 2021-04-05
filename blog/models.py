from django.conf import settings
from django.db import models
from django.utils import timezone

# ブログの記事オブジェクト・Postオブジェクト。 models.ModelはDjano Modelだと言う意味。継承
class Post(models.Model):
    # フィールドリファレンス：https://docs.djangoproject.com/ja/2.2/ref/models/fields/#field-types
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 他のモデルへのリンク
    title = models.CharField(max_length=200) # 文字数が制限されたテキストを定義するフィールド
    text = models.TextField() # 文字数制限なしのテキストを定義するフィールド
    created_date = models.DateTimeField(default=timezone.now) # 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)
    
    # ブログを公開するメソッド
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title