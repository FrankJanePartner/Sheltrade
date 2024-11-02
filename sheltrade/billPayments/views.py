from django.shortcuts import render, redirect
from django.http import JsonResponse
from pprint import pprint as pp
from .utils import VTUBILLSAPI, VT_EMAIL, VT_PASSWORD
from wallet.models import Transaction
from pprint import pprint as pp
import random
import string
from datetime import datetime
from requests.auth import HTTPBasicAuth
from django.views.decorators.http import require_http_methods
import pytz
from django.contrib.auth.decorators import login_required

# Initialize the VTUAPI with the necessary keys
vtu_api =   VTUBILLSAPI(VT_EMAIL, VT_PASSWORD)

@login_required
@require_http_methods(["GET"])
def get_tv_services(request):
    """Fetch available TV service providers."""
    service_id = request.GET.get('serviceID')
    if service_id:
        services = vtu_api.getServices(service_id)
        return JsonResponse(services, safe=False)
    return JsonResponse({'error': 'Service ID is required.'}, status=400)


@login_required
@require_http_methods(["POST"])
def subscribe_tv(request):
    """Handle TV subscription: Verify and process payment based on subscription type."""
    data = request.POST
    service_id = data.get('service-provider')
    # service_id = data.get('serviceID')
    billers_code = data.get('card-number')
    variation_code = data.get('service-plan')
    subscription_type = data.get('subscription-type')
    phone = data.get('phone')
    amount = data.get('amount')

    # Generate a request ID
    request_id = vtu_api.generate_request_id()

    # Step 1: Verify the smart card number
    verify_response = vtu_api.verifySCNumber(billers_code, service_id)
    print(verify_response)

    if 'error' in verify_response:
        return JsonResponse({'error': verify_response['error']}, status=400)

    # Step 2: Check the subscription type and make the appropriate API call
    if subscription_type == "renew":
        response = vtu_api.renewPlan(
            request_id, service_id, billers_code, variation_code, amount, phone, subscription_type, 1
        )
        return redirect('billPayments:subscription_success')  # URL name for success.html
    elif subscription_type == "change":
        response = vtu_api.changePlan(
            request_id, service_id, billers_code, variation_code, amount, phone, subscription_type, 1
        )
        return redirect('billPayments:subscription_success')  # URL name for success.html
    else:
        return JsonResponse({'error': 'Invalid subscription type.'}, status=400)
       

@login_required
def subscription_success(request):
    """Render the subscription success page."""
    return render(request, 'billPayment/success.html')

@login_required
def subs(request):
    return render(request, 'billPayment/subscriptions.html')


@login_required
@require_http_methods(["POST"])
def pay_electricity(request):
    """Handle electricity bill payment: Verify meter and process payment."""
    data = request.POST
    service_id = data.get('serviceID')  # Electricity provider
    meter_number = data.get('meter_number')
    meter_type = data.get('meter_type')  # Prepaid or Postpaid
    phone = data.get('phone')
    amount = data.get('amount')

    # Generate request ID
    request_id = vtu_api.generate_request_id()

    # Step 1: Verify meter number
    verify_response = vtu_api.verifyMeter(meter_number, service_id, meter_type)

    if 'error' in verify_response:
        return JsonResponse({'error': verify_response['error']}, status=400)

    # Step 2: Make payment based on meter type
    if meter_type == "prepaid":
        response = vtu_api.prepaidMeter(
            request_id, service_id, meter_number, "default", amount, phone
        )
    elif meter_type == "postpaid":
        response = vtu_api.postpaidMeter(
            request_id, service_id, meter_number, "default", amount, phone
        )
    else:
        return JsonResponse({'error': 'Invalid meter type.'}, status=400)

    # Check for payment errors
    if 'error' in response:
        return JsonResponse({'error': response['error']}, status=400)

    # On success, redirect to success page
    return redirect('billPayments:subscription_success')

@login_required
def bills(request):
    return render(request, 'billPayment/bills.html')