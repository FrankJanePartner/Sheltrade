from .models import Profile
from django.contrib.auth.models import User
from forex_python.converter import CurrencyCodes


def get_currency_symbol(currency_code):
    c = CurrencyCodes()
    return c.get_symbol(currency_code)


def currency(request):
    user = request.user
    if user.is_authenticated:
        profile = Profile.objects.filter(user=user).first()  # Retrieve the profile
        if profile:  # Check if profile exists
            currency_code = profile.preferredCurrency
            currency_symbol = get_currency_symbol(currency_code)
        else:
            currency_symbol = '₦'  # Fallback if no profile exists
    else:
        currency_symbol = '₦'  # Fallback for unauthenticated users

    context = {
        "currency_symbol": currency_symbol,
    }
    return context



def UserProfile(request):
    user = request.user
    if not user.is_authenticated:
        return {'profile': None}  # Return an empty profile context for unauthenticated users
    
    profile = Profile.objects.filter(user=user).first()  # Retrieve the profile if authenticated
    return {'profile': profile}
