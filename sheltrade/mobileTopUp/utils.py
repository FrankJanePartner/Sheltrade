import json
import requests
from requests import Session
from pprint import pprint as pp
import random
import string
from datetime import datetime
import pytz

API_KEY = "801ea9e2f2d9234d3437de7074ad4af6"
PUBLIC_KEY = "PK_1308d86a660b71f64597ccb8f270255fd2d351c88ac"
SECRET_KEY = "SK_7156ade0433533ed8d9fc07942ed18ba2aad86ff532"
BASE_URL = "https://sandbox.vtpass.com/api/"

class VTUAPI:
    def __init__(self, api_key, public_key, secret_key):
    
        self.base_url = BASE_URL
        self.headers = {
            "Accept": "application/json",
            "api-key": api_key,
            "Public-Key": public_key,
            "Secret-key": secret_key,
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def get_balance(self):
        url = f"{self.base_url}balance"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
        
    def get_service_categories(self):
        url = f"{self.base_url}service-categories"
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.status_code, "message": response.text}
        

    @staticmethod
    def generate_request_id(suffix_length=10):
        lagos_tz = pytz.timezone('Africa/Lagos')
        now = datetime.now(lagos_tz)
        timestamp = now.strftime('%Y%m%d%H%M')
        suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=suffix_length))
        request_id = f"{timestamp}{suffix}"
        return request_id
    
    def buyairtime(self, request_id, serviceID, amount, phone):
        url = f"{self.base_url}pay"
        payload = {
            "request_id": request_id,
            "serviceID": serviceID,
            "amount": amount,
            "phone": phone,
        }
        response = self.session.post(url, json=payload)
        return response.json()
    
    def getDataPlan(self, serviceID):
        url = f"{self.base_url}service-variations?serviceID={serviceID}-data"
        response = self.session.get(url)
        return response.json()
    
    def buydata(self, request_id, serviceID, billersCode, variation_code, amount, phone):
        url = f"{self.base_url}pay"
        payload = {
            "request_id": request_id,
            "serviceID": serviceID,
            "billersCode":billersCode,
            "variation_code":variation_code,
            "amount": amount,
            "phone": phone,
        }
        response = self.session.post(url, json=payload)
        return response.json()



# Instantiate the VTUAPI class with both API_KEY and PUBLIC_KEY
