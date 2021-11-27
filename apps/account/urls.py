from django.urls.conf import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('logout/', test_logout, name='logout')
]
