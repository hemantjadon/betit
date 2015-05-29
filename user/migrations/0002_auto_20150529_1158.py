# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betituser',
            name='dob',
            field=models.DateField(default=datetime.datetime(2015, 5, 29, 11, 58, 6, 715830)),
        ),
    ]
