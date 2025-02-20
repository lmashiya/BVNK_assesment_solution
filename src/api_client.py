import requests
import logging

logger = logging.getLogger("e2e_api_tests")

class APIClient:
    def __init__(self, auth):
        # self.base_url = read_config("API","base_url")
        self.base_url = 'http://bvnksimulator.pythonanywhere.com'
        self.auth = auth

    def send_request(self, method, endpoint, params=None, data=None):
        headers = self.auth.get_headers()
        url = f"{self.base_url}{endpoint}"

        logger.info(f"Making {method} request to {url}")
        response = requests.request(method, url, headers=headers, params=params, json=data)

        if response.status_code == 403:
            logger.warning("Token expired, refreshing token...")
            self.auth.refresh_token()
            headers = self.auth.get_headers()
            response = requests.request(method, url, headers=headers, params=params, json=data)

        response.raise_for_status()
        return response.json()