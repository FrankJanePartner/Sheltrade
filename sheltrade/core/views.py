from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def bills(request):
    return render(request, 'bills.html')


def buycrypto(request):
    return render(request, 'buycrypto.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def sellcrypto(request):
    return render(request, 'sellcrypto.html')
