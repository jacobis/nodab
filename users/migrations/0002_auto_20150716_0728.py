# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userboss',
            name='defeat',
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userboss',
            name='defeat_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 7, 28, 11, 445476, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='refresh_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
