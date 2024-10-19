from django.urls import path
from .views import contactus

app_name = 'contact'

urlpatterns = [
    path('', contactus, name='contact')
]
