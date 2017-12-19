# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-18 23:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt1', models.IntegerField(default=0)),
                ('attempt2', models.IntegerField(blank=True, default=0)),
                ('attempt3', models.IntegerField(blank=True, default=0)),
                ('total_score_in_frame', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_score', models.IntegerField(default=0)),
                ('player', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='frame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frames', to='bowlingREST.Game'),
        ),
    ]