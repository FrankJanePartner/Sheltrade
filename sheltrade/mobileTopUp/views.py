from django.shortcuts import render, redirect
from django.http import JsonResponse
from pprint import pprint as pp
from .utils import VTUAPI, API_KEY, PUBLIC_KEY, SECRET_KEY
from wallet.models import Transaction
from django.contrib.auth.decorators import login_required

# Initialize the VTUAPI with the necessary keys
vtu_api = VTUAPI(API_KEY, PUBLIC_KEY, SECRET_KEY)

@login_required
def buyairtime(request):
    requestID = vtu_api.generate_request_id()
    error_message = None

    if request.method == 'POST':
        network = request.POST.get('network')
        phone_number = request.POST.get('phone-number')
        amount = request.POST.get('amount')

        if not network:
            error_message = "Nework required."
        elif not phone_number:
            error_message = "Phone required."
        elif not amount:
            error_message = "Amount required."

        else:
            buy_airtime_response = vtu_api.buyairtime(requestID, network, amount, phone_number)

            if buy_airtime_response.get('code') == '000':  # Check for success
                return render(request, 'mobileTopup/success.html')
            else:
                error_message = buy_airtime_response.get('response_description', 'Failed to purchase airtime.')

    return render(request, 'mobileTopup/buyairtime-data.html', {'error': error_message})


@login_required
def buydata(request):
    requestID = vtu_api.generate_request_id()
    error_message = None

    if request.method == 'POST':
        serviceID = request.POST.get('serviceID')
        billersCode = request.POST.get('billersCode')
        variation_code = request.POST.get('variation_code')
        amount = request.POST.get('amount')
        phone = request.POST.get('phone')

        if not serviceID or not variation_code or not phone:
            error_message = "All fields are required."
        else:
            buy_data_response = vtu_api.buydata(requestID, serviceID, billersCode, variation_code, amount, phone)

            if buy_data_response.get('code') == '000':  # Check for success
                return render(request, 'mobileTopup/success.html')
            else:
                error_message = buy_data_response.get('response_description', 'Failed to purchase data.')

    return render(request, 'mobileTopup/buydata.html', {'error': error_message})


@login_required
def fetch_data_plans(request):
    service_id = request.GET.get('serviceID')
    
    if service_id:
        # Fetch the data plans from the API
        data_plans = vtu_api.getDataPlan(service_id)
        
        # Check for the correct key
        plans = data_plans.get('content', {}).get('varations') or []
        
        if plans:
            return JsonResponse({'content': {'variations': plans}}, status=200)  # Return the plans properly
        else:
            return JsonResponse({'error': 'No data plans available.'}, status=404)
    
    return JsonResponse({'error': 'Invalid service ID.'}, status=400)


