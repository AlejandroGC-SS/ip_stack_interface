from constants import API_STACK_BASE_URL
import requests
import sys

class IpStack:
    def __init__(self, api_token: str, base_url: str):
        if base_url is None or base_url == '':
            base_url = API_STACK_BASE_URL

        self.api_token = api_token
        self.base_url = base_url


    def get_ip_location(self, ip_address: str) -> tuple[str,str]:
        endpoint = f"{self.base_url}/{ip_address}?access_key={self.api_token}"
        try:
            response = requests.get(endpoint, timeout=60)
            json_response = response.json()
        except requests.exceptions.RequestException as error:
            print(f"Error: The request could not be resolved")
            print(f"Provided base url: {self.base_url}")
            if 'doc' in error.__dict__:
                print(error.__dict__['doc'])
            sys.exit(1)
        if 'error' in json_response:
            error_code = json_response['error']['code']
            error_mesage = json_response['error']['info']
            print(f"Error {error_code}: {error_mesage}")
            sys.exit(1)
        latitude = json_response['latitude']
        longitude = json_response['longitude']
        if latitude == 0 and longitude == 0:
            print("Location not found")
            sys.exit(1)
        return latitude, longitude
