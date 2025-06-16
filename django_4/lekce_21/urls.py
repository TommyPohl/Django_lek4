from django.urls import path
from .views import *


urlpatterns = [
    path('cookies_view', cookies_view, name="cookies_view"),
    path('set_cookie1', set_cookie1, name="set_cookie1"),
    path('set_cookie2', set_cookie2, name="set_cookie2"),
    path('delete_cookie', delete_cookie, name="delete_cookie"),
]