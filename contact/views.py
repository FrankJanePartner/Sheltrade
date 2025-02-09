from django.shortcuts import render

# Create your views here.
def contactus(request):
    if request.user.is_authenticated:
        base_template = "formBase.html"  # For authenticated users
    else:
        base_template = "core/base.html"  # For unauthenticated users

    context = {
        "user": request.user,  # No need to fetch from the database
        "base_template": base_template,
    }
    return render(request, 'core/contactus.html', context)
