from django.contrib import admin
from .models import Post

# PostモデルをAdminページ（管理画面）上で見えるようにするために、『admin.site.register(Post)』でモデルを登録
admin.site.register(Post)