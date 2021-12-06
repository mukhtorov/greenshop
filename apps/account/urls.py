from django.urls.conf import path, include
from .views import *

app_name = 'account'
urlpatterns = [
    path('logout/', test_logout, name='logout'),
    path('social/', include('social_django.urls', namespace='social')),
    
]
