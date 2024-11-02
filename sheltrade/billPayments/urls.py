from django.urls import path
from .views import bills, get_tv_services, subscribe_tv, subscription_success, subs, pay_electricity

app_name = "billPayments"

urlpatterns = [
    path('', subs, name='subs'),
    path('get-services/', get_tv_services, name='get_tv_services'),
    path('subscribe/', subscribe_tv, name='subscribe_tv'),
    path('subscription_success/', subscription_success, name='subscription_success'),
    path('bills/', bills, name='bills'),
    path('pay-electricity/', pay_electricity, name='pay-electricity'),
]

