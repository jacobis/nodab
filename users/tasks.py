# encoding: utf-8

from __future__ import absolute_import

import requests
from celery import shared_task, chord
from bs4 import BeautifulSoup
from datetime import datetime

from .models import User, Boss, UserBoss

from utils import u_datetime


@shared_task
def crawl_user_task(from_the_beginning=False):
    server = 'SC'
    next_page = True

    url = 'http://maview.nexon.com/Rank/Character'
    last_crawled_user = User.objects.all().order_by('-rank').first()
    page = 1 if from_the_beginning is True else (last_crawled_user.rank / 10) + 1

    while (next_page is True):
        params = {'page': page}
        response = requests.get(url, params=params, allow_redirects=False)

        response_page = BeautifulSoup(response.text, 'html.parser')
        board = response_page.find('div', class_='board')

        uibs = board.tbody.find_all('tr') # user info boxes
        
        users = []

        for uib in uibs:
            rank = parser_rank(uib.find('td', class_='first_child').contents[0])
            character = uib.find('td', class_='character')
            name = character.contents[1]
            image = character.find('img')['src']
            trophy = uib.find('td', class_='last_child').string

            if not User.objects.filter(name=name, server=server).exists(): 
                users.append({'rank': rank, 'name': name, 'server': server, 'image': image, 'trophy': trophy})

        if users:
            massive_save.delay(User, users)

        next_page = True if len(uibs) == 10 else False
        page = page + 1

        raise Exception


@shared_task
def massive_save(model, objects):
    model.objects.bulk_create([model(**obj) for obj in objects])


def parser_rank(rank):
    try:
        rank = rank['alt'][0]
    except:
        pass

    return rank