import json
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import News, Match,Team,Player
from django.core import serializers
from django.db.models import Q
import re
def index(request):
    news_ids = range(1, 7)  # Adjust numbers as necessary
    news_items = News.objects.filter(id__in=news_ids)
    news_dict = {f'news_{news.id}': news for news in news_items}

    matches = list(Match.objects.all().order_by('time'))
    today = timezone.now()
    initial_match_index = next((i for i, match in enumerate(matches) if match.time >= today), 0)
    initial_group_index = initial_match_index // 4
    grouped_matches = [matches[i:i + 3] for i in range(0, len(matches), 3)]

    # Combine news dictionary with other context
    player=Player.objects.order_by('-rating')[:10]
    team = Team.objects.order_by('ranking')[:8]
    team_s=serializers.serialize('json',team)
    context = {**news_dict, 'grouped_matches': grouped_matches, 'initial_group_index': initial_group_index,'player':player,'team':team,'teamx':team_s}
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

def escape_control_characters(json_string):
    # 定义一个替换函数，将非法字符替换为合法的转义字符
    def replace_match(match):
        char = match.group(0)
        # 转义特定控制字符
        if char == '\b':
            return '\\b'
        elif char == '\f':
            return '\\f'
        elif char == '\n':
            return '\\n'
        elif char == '\r':
            return '\\r'
        elif char == '\t':
            return '\\t'
        else:
            # 使用 Unicode 转义序列
            return '\\u{0:04x}'.format(ord(char))
    
    # 匹配所有控制字符
    return re.sub(r'[\x00-\x1F\x7F]', replace_match, json_string)

def team_ranking(request):
    news_1 = News.objects.filter(id=1).first()
    news_2 = News.objects.filter(id=2).first()
    news_3 = News.objects.filter(id=3).first()
    news_4 = News.objects.filter(id=4).first()
    team = Team.objects.order_by('ranking')[:10]
    teamc = Team.objects.order_by('ranking')[3:10]
    players = Player.objects.all()
    ret_players=[]
    for i in range(0,10):
        team_players=[]
        print(team[i].name)
        for player in players:
            if player.team.name== team[i].name:
                team_players.append(player)
                
        ret_players.append(team_players)
    team_s=serializers.serialize('json',team)
    team_s= escape_control_characters(team_s)
    try:
        team_data = json.loads(team_s)
        print("Parsed JSON data:", team_data)
    except json.JSONDecodeError as e:
        print("JSON decode error:", e)
    return render(request, 'team_ranking.html', { 'news_1': news_1,'news_2': news_2,'news_3': news_3,'news_4': news_4,'players':ret_players,'team':team,'teamlft':teamc,'teamx':team_s})

def player_ranking(request):
    news_1 = News.objects.filter(id=1).first()
    news_2 = News.objects.filter(id=2).first()
    news_3 = News.objects.filter(id=3).first()
    news_4 = News.objects.filter(id=4).first()
    player = Player.objects.order_by('-rating')[:30]
    lft=Player.objects.order_by('-rating')[3:30]
    return render(request, 'player_ranking.html', { 'news_1': news_1,'news_2': news_2,'news_3': news_3,'news_4': news_4,'players':player, 'playerslft':lft})

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

def team_detail(request, team_name):
    team = get_object_or_404(Team, name=team_name)
    players = Player.objects.filter(team=team)
    news_1 = News.objects.filter(id=1).first()
    news_2 = News.objects.filter(id=2).first()
    news_3 = News.objects.filter(id=3).first()
    news_4 = News.objects.filter(id=4).first()
    matches = Match.objects.filter(Q(team1__name=team_name) | Q(team2__name=team_name))
    return render(request, 'team_detail.html', {
        'news_1': news_1,
        'news_2': news_2,
        'news_3': news_3,
        'news_4': news_4,
        'team': team,
        'players':players,
        'matches':matches
    })

def player_detail(request, nickname):

    players = Player.objects.all().order_by('-rating')
    for index, player in enumerate(players):
        player.ranking = index + 1  # Rankings start from 1
        player.save()
    player = get_object_or_404(Player, nickname=nickname)
    team=get_object_or_404(Team, name=player.team.name)
    news_1 = News.objects.filter(id=1).first()
    news_2 = News.objects.filter(id=2).first()
    news_3 = News.objects.filter(id=3).first()
    news_4 = News.objects.filter(id=4).first()
    return render(request, 'player_detail.html', {
        'player':player,
        'team':team,
        'news_1': news_1,
        'news_2': news_2,
        'news_3': news_3,
        'news_4': news_4,
    })
