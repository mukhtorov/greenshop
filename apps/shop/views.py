from django.shortcuts import render, get_object_or_404
from .models import Plant, Category


def categories_count(request):
    categories = Category.objects.all()
    data = dict()
    for category in categories:
        data[str(category)] = Plant.objects.filter(category__name=category).count()
    return render(request, 'shop/shop.html', {'data': data})


def plant_list(request, category_slug=None):
    category = None
    plants = Plant.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        plants = plants.filter(category=category)
    return render(request, 'shop/list_view.html', {'plants': plants, })


def plant_detail(request, id, slug):
    plant_view = get_object_or_404(Plant, id=id, slug=slug, available=True)
    return render(request, 'shop/detail_view.html', {'plant': plant_view})
