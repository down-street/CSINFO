from django.db import models

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100, blank=True)
    ranking = models.IntegerField()
    description = models.TextField(blank=True)

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100, blank=True)
    ranking = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    rating = models.FloatField(blank=True,null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    nationality = models.CharField(max_length=20,null=True)

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    recommended_news_1 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='primary_recommendation', blank=True)
    recommended_news_2 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='secondary_recommendation', blank=True)
    


class Match(models.Model):
    match_name_big = models.CharField(max_length=255)
    match_name_small = models.CharField(max_length=255)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_matches')
    score_1 = models.IntegerField(default=0)
    score_2 = models.IntegerField(default=0)
    time = models.DateTimeField()
    state = models.CharField(max_length=100, choices=(('未开始', '未开始'), ('已结束', '已结束')))
    link = models.URLField(blank=True, null=True)



class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    team = models.ForeignKey(Team, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    player = models.ForeignKey(Player, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE, null=True, blank=True)






