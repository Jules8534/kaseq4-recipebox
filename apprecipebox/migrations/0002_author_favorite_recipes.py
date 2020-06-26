# Generated by Django 3.0.5 on 2020-06-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apprecipebox', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='favorite_recipes',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='apprecipebox.Recipe'),
        ),
    ]