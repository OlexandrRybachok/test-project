# Generated by Django 5.0.6 on 2024-10-11 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierating', '0002_remove_movie_type_remove_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.TextField(blank=True, max_length=4),
        ),
    ]
