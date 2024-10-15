"""Define Url Patterns For User Accounts"""

from django.urls import path, include
from . import views 

app_name = 'accounts'
urlpatterns = [
    # include default auth urls
    path('', include('django.contrib.auth.urls')),
    # Registration Page
    path('register/', views.register, name='register'),
]