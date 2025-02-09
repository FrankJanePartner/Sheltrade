from django.urls import path
from .views import home, aboutus,  dashboard, profile, preferred_currency, notification, settings

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', aboutus, name='aboutus'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path("preferred_currency/", preferred_currency, name="preferred_currency"),
    path('notification/', notification, name='notification'),
    path('settings/', settings, name='settings'),
]
