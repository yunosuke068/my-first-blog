from django.urls import path # djangoのpath関数のインポート
from . import views # blogアプリの全てのビューをインポート

urlpatterns = [
    path('', views.post_list, name='post_list'), # post_listをrootURLに割り当てる
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]