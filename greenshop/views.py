from django.shortcuts import render

from apps.shop.models import Plant, Category
from apps.account.forms import *


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

