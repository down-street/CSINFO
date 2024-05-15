# cs2_news_app/views.py
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import News, Player, Team, Image

def index(request):
    # 假设您想在不同块分别显示ID为1, 2, 3的新闻
    news_1 = News.objects.filter(id=1).first()
    news_2 = News.objects.filter(id=2).first()
    news_3 = News.objects.filter(id=3).first()
    news_4 = News.objects.filter(id=4).first()

    return render(request, 'main.html', 
        {    
        'news_1': news_1,
        'news_2': news_2,
        'news_3': news_3,
        'news_4': news_4
        }  
    )


def news_detail(request, news_id):
    # 根据新闻ID获取新闻实例，如果不存在则返回404
    news = get_object_or_404(News, id=news_id)
    # 尝试获取推荐新闻，如果没有设置，变量将为None
    recommended_1 = news.recommended_news_1 if hasattr(news, 'recommended_news_1') else None
    recommended_2 = news.recommended_news_2 if hasattr(news, 'recommended_news_2') else None

    # 将新闻对象传递给新闻详情模板
    return render(request, 'news_detail.html', {
        'news': news,
        'recommended_1': recommended_1,
        'recommended_2': recommended_2
    })

@csrf_exempt
def increment_up_votes(request, news_id):
    if request.method == 'POST':
        news = get_object_or_404(News, id=news_id)
        news.up_votes += 1
        news.save()
        return JsonResponse({'success': True, 'up_votes': news.up_votes})
    
@csrf_exempt
def increment_down_votes(request, news_id):
    if request.method == 'POST':
        news = get_object_or_404(News, id=news_id)
        news.down_votes += 1
        news.save()
        return JsonResponse({'success': True, 'down_votes': news.down_votes})



def all_news(request):
    search_query = request.GET.get('search', '')
    date_filter = request.GET.get('date', '')
    all_news = News.objects.all()

    if search_query:
        all_news = all_news.filter(title__icontains=search_query)
    
    if date_filter:
        year, month = date_filter.split('-')
        all_news = all_news.filter(date__year=year, date__month=month)
    
    # 获取数据库中所有新闻的年份和月份
    dates = News.objects.dates('date', 'month', order='DESC')

    return render(request, 'all_news.html', {'all_news': all_news, 'dates': dates})


def player_ranking(request):
    return render(request, 'player_ranking.html')
def team_ranking(request):
    return render(request, 'team_ranking.html')