# Generated by Django 4.2.1 on 2023-07-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_remove_recipe_favorite_recipe_favorited_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='favorited_by',
        ),
        migrations.AddField(
            model_name='recipe',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
