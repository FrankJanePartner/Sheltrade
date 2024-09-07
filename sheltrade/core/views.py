from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def bills(request):
    return render(request, 'bills.html')

def buyairtime(request):
    return render(request, 'buyairtime-data.html')

def buycrypto(request):
    return render(request, 'buycrypto.html')

def buygiftcard(request):
    return render(request, 'buygiftcard.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def forgotpassword(request):
    return render(request, 'forgotpassword.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def sellcrypto(request):
    return render(request, 'sellcrypto.html')

def sellgiftcard(request):
    return render(request, 'sellgiftcard.html')