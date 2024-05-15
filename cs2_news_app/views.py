from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import News, Match

def index(request):
    news_ids = range(1, 7)  # Adjust numbers as necessary
    news_items = News.objects.filter(id__in=news_ids)
    news_dict = {f'news_{news.id}': news for news in news_items}

    matches = list(Match.objects.all().order_by('time'))
    today = timezone.now()
    initial_match_index = next((i for i, match in enumerate(matches) if match.time >= today), 0)
    initial_group_index = initial_match_index // 4
    grouped_matches = [matches[i:i + 3] for i in range(0, len(matches), 3)]

    context = {**news_dict, 'grouped_matches': grouped_matches, 'initial_group_index': initial_group_index}
    
    return render(request, 'main.html', context)

def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    recommended_1 = news.recommended_news_1 if hasattr(news, 'recommended_news_1') else None
    recommended_2 = news.recommended_news_2 if hasattr(news, 'recommended_news_2') else None

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
    
    dates = News.objects.dates('date', 'month', order='DESC')

    return render(request, 'all_news.html', {'all_news': all_news, 'dates': dates})

def player_ranking(request):
    return render(request, 'player_ranking.html')

def team_ranking(request):
    news_1 = News.objects.filter(id=1).first()
    news_2 = News.objects.filter(id=2).first()
    news_3 = News.objects.filter(id=3).first()
    news_4 = News.objects.filter(id=4).first()

    return render(request, 'team_ranking.html', 
        {    
            'news_1': news_1,
            'news_2': news_2,
            'news_3': news_3,
            'news_4': news_4
        }
    )

def all_matches(request):
    matches = Match.objects.all().order_by('time')
    today = timezone.now().date()
    dates = sorted(set(match.time.date() for match in matches))
    context = {
        'matches': matches,
        'dates': dates,
        'today': today
    }
    return render(request, 'all_matches.html', context)
