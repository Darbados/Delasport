# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-12 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0005_game_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]