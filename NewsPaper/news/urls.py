from django.urls import path
from .views import (
    NewsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, ArticleCreate, ArticleUpdate, ArticleDelete,
    subscriptions
)
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', PostSearch.as_view()),
    path('', cache_page(60*1)(NewsList.as_view())),
    path('<int:pk>', cache_page(60*5)(PostDetail.as_view()), name='post_detail'),

    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('articles/create/', ArticleCreate.as_view(), name='article_create'),
    path('articles/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
    path('articles/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('subscriptions/', subscriptions, name='subscriptions'),
]