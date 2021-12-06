from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import (authenticate, login, logout)
from django.contrib.auth.models import User

from apps.shop.models import Plant, Category
from apps.account.forms import *


class HomeHandlerView(TemplateView):
    pass


def home(request):
    categories = Category.objects.all()
    data = dict()
    for category in categories:
        data[str(category)] = Plant.objects.filter(category__name=category).count()
    context = {
        'data': data,
        'formreg': NewUserForm(),
        'formlog': LoginForm(),
    }
    return render(request, 'greenshop/base.html', context)

