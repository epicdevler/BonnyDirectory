# Generated by Django 3.2.2 on 2021-07-12 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_name', models.CharField(max_length=300)),
                ('position', models.CharField(max_length=250)),
                ('body', models.TextField(null=True)),
                ('testimonial_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
