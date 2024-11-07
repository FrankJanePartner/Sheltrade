from django.urls import path
from .views import buycrypto, sellcrypto

app_name = 'core'

urlpatterns = [
    path('', buycrypto, name='buycrypto'),
    path('sellcrypto/', sellcrypto, name='sellcrypto'),
]
