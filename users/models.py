# encoding: utf-8

from django.db import models


class User(models.Model):
    SCANIA = 'SC'
    SERVERS = (
        (SCANIA, 'Scania'),
    )
    HEAVYGUNNER = 'HE'
    PRIEST = 'PR'
    WIZARD = 'WI'
    BERSERKER = 'BE'
    ASSASSIN = 'AS'
    THIEF = 'TH'
    KNIGHT = 'KN'
    RANGER = 'RA'
    CLASSES = (
        (HEAVYGUNNER, 'Heavygunner'),
        (PRIEST, 'Priest'),
        (WIZARD, 'Wizard'),
        (BERSERKER, 'Berserker'),
        (ASSASSIN, 'Assassin'),
        (THIEF, 'Thief'),
        (KNIGHT, 'Knight'),
        (RANGER, 'Ranger'),
    )

    name = models.CharField(max_length=30)
    server = models.CharField(max_length=2, choices=SERVERS, default=SCANIA)
    u_class = models.CharField(max_length=2, choices=CLASSES, blank=True)
    rank = models.IntegerField()
    trophy = models.IntegerField()
    image = models.URLField(blank=True)
    refresh_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        unique_together = ('name', 'server')

    def __str__(self):
        return unicode(self.name).encode('utf-8')


class Boss(models.Model):
    m_id = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    image = models.URLField(blank=True)

    class Meta:
        verbose_name = "Boss"
        verbose_name_plural = "Bosses"

    def __str__(self):
        return unicode(self.name).encode('utf-8')


class UserBoss(models.Model):
    user_id = models.ForeignKey(User)
    boss_id = models.ForeignKey(Boss)
    party_id = models.CharField(max_length=100)
    rank = models.IntegerField()
    elapse_time = models.TimeField()
    defeat_time = models.DateTimeField()

    class Meta:
        verbose_name = "UserBoss"
        verbose_name_plural = "UserBosses"
        unique_together = ('user_id', 'boss_id', 'party_id')

    def __str__(self):
        return "%s / %s" % (self.user_id, self.boss_id)