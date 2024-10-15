"""Define Url Patterns For User Accounts"""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # include default auth urls
    path('', include('django.contrib.auth.urls')),
]