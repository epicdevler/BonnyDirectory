# Generated by Django 3.2.2 on 2021-10-04 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_tips', '0004_newspost_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
