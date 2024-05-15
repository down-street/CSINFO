from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # 应用的首页
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),  # 新闻详情页
    path('news/<int:news_id>/upvote/', views.increment_up_votes, name='upvote_news'),
    path('news/<int:news_id>/downvote/', views.increment_down_votes, name='downvote_news'),
    path('all_news/', views.all_news, name='all_news'),  # “所有新闻”页面
    path('team_ranking/',views.team_ranking,name='team_ranking'),
    path('player_ranking/',views.player_ranking,name='player_ranking'),
    path('team/<int:team_id>/', views.team_detail, name='team_detail')
]
