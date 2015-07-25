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
                ('m_id', models.CharField(unique=True, max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('image', models.URLField(blank=True)),
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
                ('u_class', models.CharField(blank=True, max_length=2, choices=[(b'HE', b'Heavygunner'), (b'PR', b'Priest'), (b'WI', b'Wizard'), (b'BE', b'Berserker'), (b'AS', b'Assassin'), (b'TH', b'Thief'), (b'KN', b'Knight'), (b'RA', b'Ranger')])),
                ('rank', models.IntegerField()),
                ('trophy', models.IntegerField()),
                ('image', models.URLField(blank=True)),
                ('refresh_time', models.DateTimeField(auto_now=True)),
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
                ('party_id', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('elapse_time', models.TimeField()),
                ('defeat_time', models.DateTimeField()),
                ('boss_id', models.ForeignKey(to='users.Boss')),
                ('user_id', models.ForeignKey(to='users.User')),
            ],
            options={
                'verbose_name': 'UserBoss',
                'verbose_name_plural': 'UserBosses',
            },
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('name', 'server')]),
        ),
        migrations.AlterUniqueTogether(
            name='userboss',
            unique_together=set([('user_id', 'boss_id', 'party_id')]),
        ),
    ]
