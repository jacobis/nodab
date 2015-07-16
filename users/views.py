from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render

from .models import User, Boss


def index(request):
    pass


def users(request, name):
    try:
        user = User.objects.get(name=name)
        name = name
    except:
        user_info = fetch_user_info(name)
        context = user_info
    
    return render(request, 'users.html', context)
    

import requests
from bs4 import BeautifulSoup

def fetch_user_info(name):
    url = 'http://maview.nexon.com/Rank/Character'
    params = {'p': 'realtime', 'k': name}
    response = requests.get(url, params=params)

    page = BeautifulSoup(response.text, 'html.parser')
    uid = page.find('div', class_='board')

    rank = uid.find('td', class_='first_child').string
    name = uid.find('td', class_='character').contents[1]
    image = uid.find('img')['src']
    trophy = uid.find('td', class_='last_child').string

    user_info = {'rank': rank, 'name': name, 'image': image, 'trophy': trophy}

    return user_info