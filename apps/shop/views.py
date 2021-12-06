from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Plant, Category


class PlantListView(ListView):
    model = Plant
    context_object_name = 'plant_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plant_list'] = Plant.objects.filter(available=True)


def plant_detail(request, id, slug):
    plant_view = get_object_or_404(Plant, id=id, slug=slug, available=True)
    return render(request, 'shop/detail_view.html', {'plant': plant_view})
