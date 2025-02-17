from django.urls import path
from .views import home, aboutus,  dashboard, profile, preferred_currency, notification, settings, notification_detail, mark_all_as_read

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('about/', aboutus, name='aboutus'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path("preferred_currency/", preferred_currency, name="preferred_currency"),
    path('notification/', notification, name='notification'),
    path('notification_detail/<slug:slug>', notification_detail, name='notification_detail'),
    path('notifications/read/all/', mark_all_as_read, name='mark_all_as_read'),
    path('settings/', settings, name='settings'),
]
