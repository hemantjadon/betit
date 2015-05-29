# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150529_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='hashTags',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='uploads/')),
                ('on', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, upload_to='profile_pics/')),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('user', models.ManyToManyField(to='user.UserProfile', related_name='work')),
            ],
        ),
        migrations.AlterField(
            model_name='betituser',
            name='dob',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 13, 35, 49, 649442)),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='photo',
            name='by',
            field=models.ForeignKey(related_name='uploaded_by', to='user.UserProfile'),
        ),
        migrations.AddField(
            model_name='photo',
            name='likers',
            field=models.ManyToManyField(to='user.UserProfile', related_name='liker'),
        ),
        migrations.AddField(
            model_name='photo',
            name='user_tags',
            field=models.ManyToManyField(to='user.UserProfile', related_name='tagged_in'),
        ),
    ]
