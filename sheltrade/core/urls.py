from django.urls import path
from .views import home, aboutus, bills, buycrypto,  dashboard, sellcrypto

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', aboutus, name='aboutus'),
    path('bills/', bills, name='bills'),
    path('buycrypto/', buycrypto, name='buycrypto'),
    path('buycrypto/', buycrypto, name='buycrypto'),
    path('dashboard/', dashboard, name='dashboard'),
    path('sellcrypto/', sellcrypto, name='sellcrypto'),
]
