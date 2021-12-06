from django.urls.conf import path
from .forms_controllers import *


app_name = 'routes'
urlpatterns = [
    path('register-form/', register_view, name='register'),
    path('login-form/', login_view, name='login'),

]
