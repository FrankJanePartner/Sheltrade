import requests
from decouple import config

def validate_gift_card(card_number, card_pin):
    headers = {
        'Authorization': f'Bearer {config("ZENDIT_API_KEY")}',
        'Content-Type': 'application/json'
    }
    url = f'{config("ZENDIT_API_BASE_URL")}/giftcards/validate'

    response = requests.post(url, json={
        'card_number': card_number,
        'card_pin': card_pin
    }, headers=headers)

    return response.json()  # Returns gift card validation status
