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
    ranking = models.IntegerField()
    description = models.TextField(blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    content = models.TextField()
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    recommended_news_1 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='primary_recommendation', blank=True)
    recommended_news_2 = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='secondary_recommendation', blank=True)
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    team = models.ForeignKey(Team, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    player = models.ForeignKey(Player, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE, null=True, blank=True)






