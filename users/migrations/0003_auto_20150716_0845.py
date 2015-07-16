# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150716_0728'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='boss',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
