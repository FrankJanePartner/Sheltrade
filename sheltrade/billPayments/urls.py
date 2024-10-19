from django.urls import path
from .views import one

app_name = "billPayments"

urlpatterns = [
    path('', one, name='one')
]
