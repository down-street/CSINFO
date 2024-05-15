from django.contrib import admin
from .models import Team, Player, News, Image, Match

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'coach_name', 'ranking')
    search_fields = ('name', 'coach_name')
    list_filter = ('ranking',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'full_name', 'ranking', 'team')
    search_fields = ('nickname', 'full_name')
    list_filter = ('ranking', 'team')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_name_big', 'team1', 'team2', 'score_1', 'score_2', 'time', 'state')
    search_fields = ('match_name_big', 'match_name_small', 'team1__name', 'team2__name')
    list_filter = ('state', 'time')
    date_hierarchy = 'time'  # Adds a convenient navigation by date

    # Optionally, customize the form layout
    fieldsets = (
        (None, {
            'fields': ('match_name_big', 'match_name_small', 'state', 'link')
        }),
        ('Teams and Scores', {
            'fields': (('team1', 'score_1'), ('team2', 'score_2'))
        }),
        ('Match Details', {
            'fields': ('time',)
        }),
    )

    # Enhance user experience by sorting matches by date by default
    ordering = ('-time',)

    # This method can be used to display team names in the list_display if needed
    def team_names(self, obj):
        return f"{obj.team1.name} vs {obj.team2.name}"
    team_names.short_description = 'Match'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'team', 'player', 'news')
    list_filter = ('team', 'player', 'news')

    def image_tag(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'
