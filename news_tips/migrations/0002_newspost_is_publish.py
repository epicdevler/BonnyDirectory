# Generated by Django 3.2.2 on 2021-10-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_tips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='is_publish',
            field=models.BooleanField(default=True),
        ),
    ]