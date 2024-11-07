from django.urls import path
from .views import home, aboutus,  dashboard, profile, notification, settings

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', aboutus, name='aboutus'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('notification/', notification, name='notification'),
    path('settings/', settings, name='settings'),
]
