from django.urls import path
from .views import sellgiftcard, buygiftcard

app_name = 'giftcard'

urlpatterns = [
    path('', buygiftcard, name='buygiftcard'),
    path('sell/', sellgiftcard, name='sellgiftcard'),
]
