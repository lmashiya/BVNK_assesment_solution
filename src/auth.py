import logging

logger = logging.getLogger("e2e_api_tests")

class Auth:
    def __init__(self, api_client):
        self.api_client = api_client
        self.auth_token = None
        self.token_expiry_time = None

    def setup_account(self):
        logger.info("Fetching new auth token...")
        response = self.api_client.send_request("GET", "/init",)
        self.auth_token = response.get("access_token")

    def refresh_token(self):
        logger.info("Refreshing auth token...")
        self.setup_account()

    def get_headers(self):
        headers = {}
        if not self.auth_token:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            logger.warning("Missing auth token, fetching new one...")
        else:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers
