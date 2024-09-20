from django.urls import path
from .views import home, bills, buyairtime, buycrypto, buygiftcard, dashboard, sellcrypto, sellgiftcard

app_name='core'
urlpatterns = [
    path('', home, name='home'),
    path('bills/', bills, name='bills'),
    path('buyairtime/', buyairtime, name='buyairtime'),
    path('buycrypto/', buycrypto, name='buycrypto'),
    path('buyairtime/', buyairtime, name='buyairtime'),
    path('buycrypto/', buycrypto, name='buycrypto'),
    path('buygiftcard/', buygiftcard, name='buygiftcard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('sellcrypto/', sellcrypto, name='sellcrypto'),
    path('sellgiftcard/', sellgiftcard, name='sellgiftcard'),
]
