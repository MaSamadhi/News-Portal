from django.urls import path
# Импортируем созданное нами представление
from .views import PostsList, PostDetail, PostUpdate, PostDelete, PostSearch, PostNewsCreate, PostArticlesCreate


urlpatterns = [
    path('', PostsList.as_view(), name='post_list'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostNewsCreate.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', PostUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
    path('articles/create/', PostArticlesCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
]

'''
/news/create/
/news/<int:pk>/edit/
/news/<int:pk>/delete/
/articles/create/
/articles/<int:pk>/edit/
/articles/<int:pk>/delete/
'''
