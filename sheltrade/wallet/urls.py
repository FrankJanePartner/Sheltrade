from django.urls import path
from .views import wallet

app_name='wallet'

urlpatterns = [
    path('', wallet, name='wallet'),
]
