# encoding: utf-8

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render

from .models import User, Boss, UserBoss


def index(request):
    return render('')
    # name = request.GET.get('name')
    # fetch_user_boss_info(name=name)


def users(request, name):
    try:
        user = User.objects.get(name=name)
    except:
        user = fetch_user_info(name)
        
    context = {'user': user}

    return render(request, 'users.html', context)
    

import requests
from datetime import datetime
from bs4 import BeautifulSoup


def fetch_user_info(name):
    url = 'http://maview.nexon.com/Rank/Character'
    params = {'p': 'realtime', 'k': name}
    response = requests.get(url, params=params)

    page = BeautifulSoup(response.text, 'html.parser')
    uid = page.find('div', class_='board') # user info division

    rank = uid.find('td', class_='first_child').string
    name = uid.find('td', class_='character').contents[1]
    image = uid.find('img')['src']
    trophy = uid.find('td', class_='last_child').string

    user_info = {'rank': rank, 'name': name, 'image': image, 'trophy': trophy}

    user = User.objects.create(**user_info)

    return user


def fetch_user_boss_info(name):
    user = get_or_create_user(name)
    bosses = Boss.objects.all()
    user_boss_infos = []

    url = 'http://maview.nexon.com/Rank/Boss1'
    test = []
    for boss in bosses:
        params = {'b': boss.m_id, 'k': name}
        response = requests.get(url, params=params)

        page = BeautifulSoup(response.text, 'html.parser')
        pnd = page.find('div', class_='paginate') # paginate division
        pages = len(pnd.find('span', class_='num').find_all('a'))

        for i in range(pages):
            if i != 1:
                params.update({'page': i})
                response = requests.get(url, params=params)
                page = BeautifulSoup(response.text, 'html.parser')

            bid = page.find('div', class_='board') # boss info division
            records = bid.tbody.find_all('tr')

            for record in records:
                try:
                    rank = record.find('td', class_='first_child').string
                    party_id = record.find('div', class_='party_list')['id']
                    defeat_time = record.find('td', class_='date').string
                    elapse_time = record.find('td', class_='record').string

                    if rank and defeat_time and elapse_time:
                        if not rank.isdigit():
                            rank = rank.img['alt'][0]

                        defeat_time = datetime_parser(defeat_time, '%Y년 %m월 %d일')
                        elapse_time = datetime_parser(elapse_time, '%M분 %S초')
                        
                        user_boss_info = {'user_id': user, 'boss_id': boss, 'party_id': party_id, 'rank': rank, 'defeat_time': defeat_time, 'elapse_time': elapse_time}
                        user_boss_infos.append(user_boss_info)
                
                except:
                    pass

    UserBoss.objects.bulk_create([UserBoss(**ubi) for ubi in user_boss_infos])


def datetime_parser(unicode_datetime, e_format):
    return datetime.strptime(unicode_datetime.encode('utf-8'), e_format)


def get_or_create_user(name):
    try:
        user = User.objects.get(name=name)
    except ObjectDoesNotExist:
        user = fetch_user_info(name)

    return user