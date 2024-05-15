from django.contrib import admin
from .models import Team, Player, News, Image

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
