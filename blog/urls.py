from django.urls import path
from .views import PostListView


# ビューにポストはまだ作成されていない
urlpatterns = [
    path('', PostListView.as_view(), name='post_list')
]