# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Boss',
                'verbose_name_plural': 'Bosses',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('server', models.CharField(default=b'SC', max_length=2, choices=[(b'SC', b'Scania')])),
                ('rank', models.IntegerField()),
                ('trophy', models.IntegerField()),
                ('refresh_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='UserBoss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('defeat', models.IntegerField()),
                ('elapse_time', models.TimeField()),
                ('boss_id', models.ForeignKey(to='users.Boss')),
                ('user_id', models.ForeignKey(to='users.User')),
            ],
            options={
                'verbose_name': 'UserBoss',
                'verbose_name_plural': 'UserBosses',
            },
        ),
    ]
