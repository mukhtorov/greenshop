from django.urls import re_path
from . import views

app_name = 'shop'
urlpatterns = [
    # переписать url реквестеры, для нормальной работы шаблонов
    re_path(r'^$', views.categories_count, name='plant_list'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.plant_list, name='plant_list_by_category'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.plant_detail, name='plant_detail'),

]
