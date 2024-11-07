from django.shortcuts import render

# Create your views here.
def sellcrypto(request):
    return render(request, 'core/sellcrypto.html')

def buycrypto(request):
    return render(request, 'core/buycrypto.html')
