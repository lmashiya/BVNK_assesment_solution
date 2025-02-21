
class Auth:
    def __init__(self, api_client,logger):
        self.api_client = api_client
        self.auth_token = None
        self.token_expiry_time = None
        self.logger = logger

    def setup_account(self):
        self.logger.info("Fetching new auth token...")
        response = self.api_client.send_request("GET", "/init",)
        self.auth_token = response.get("access_token")

    def refresh_token(self):
        self.logger.info("Refreshing auth token...")
        self.setup_account()

    def get_headers(self):
        headers = {}
        if not self.auth_token:
            headers = {
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
            self.logger.warning("Missing auth token, fetching new one...")
        else:
            headers["Authorization"] = f"Bearer {self.auth_token}"
        return headers

    def test_auth(self):
        self.logger.info("Testing auth token...")
        response = self.api_client.send_request("GET", "/echo",)
        return response
