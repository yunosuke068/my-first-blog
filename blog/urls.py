from django.urls import path # djangoのpath関数のインポート
from . import views # blogアプリの全てのビューをインポート

urlpatterns = [
    path('', views.post_list, name='post_list'), # post_listをrootURLに割り当てる
]