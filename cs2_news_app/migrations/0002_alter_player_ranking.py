# Generated by Django 5.0.4 on 2024-05-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cs2_news_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="ranking",
            field=models.IntegerField(blank=True),
        ),
    ]
