# encoding: utf-8

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, render

import tasks

from .models import User, Boss, UserBoss


def index(request):
    pass


def crawl_users(request, from_the_beginning):
    tasks.crawl_user_task.delay()

    return render(request, 'users.html')