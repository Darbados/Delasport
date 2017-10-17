# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-12 00:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bowling', '0002_auto_20171012_0323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attempt1', models.CharField(default='', max_length=1)),
                ('attempt2', models.CharField(default='', max_length=1)),
                ('attempt3', models.CharField(default='', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='frame1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame4',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame5',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame6',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame7',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame8',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='game',
            name='frame9',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='frame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bowling.Game'),
        ),
    ]