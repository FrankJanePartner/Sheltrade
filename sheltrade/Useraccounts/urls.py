from django.urls import path
from .views import forgotpassword, signin, signup, signout

app_name='account'
urlpatterns = [
    path('forgotpassword/', forgotpassword, name='forgotpassword'),
    path('login/', signin, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', signout, name='logout'),
]
