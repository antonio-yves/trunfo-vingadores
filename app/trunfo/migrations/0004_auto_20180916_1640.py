# Generated by Django 2.1.1 on 2018-09-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trunfo', '0003_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score_one',
            field=models.IntegerField(default=0, verbose_name='Pontuação Jogador 1'),
        ),
        migrations.AddField(
            model_name='game',
            name='score_two',
            field=models.IntegerField(default=0, verbose_name='Pontuação Jogador 2'),
        ),
    ]