
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('news/<int:news_id>/upvote/', views.increment_up_votes, name='upvote_news'),
    path('news/<int:news_id>/downvote/', views.increment_down_votes, name='downvote_news'),
    path('all_news/', views.all_news, name='all_news'),
    path('team_ranking/', views.team_ranking, name='team_ranking'),
    path('player_ranking/', views.player_ranking, name='player_ranking'),
    path('all_matches/', views.all_matches, name='all_matches'),  # 新增的“所有比赛”页面
]
