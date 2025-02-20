import logging

logger = logging.getLogger("e2e_api_tests")


class Quote:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_quote(self, amount, from_currency, to_currency, from_wallet, to_wallet):
        logger.info(f"Creating quote: {amount} {from_currency} to {to_currency}")
        endpoint = "/api/v1/quote"
        data = {
            "from": from_currency,
            "to": to_currency,
            "fromWallet": from_wallet,
            "useMinimum": True,
            "useMaximum": True,
            "reference": "string",
            "toWallet": to_wallet,
            "amountIn": amount,
            "amountOut": 0,
            "payInMethod": "wallet",
            "payOutMethod": "wallet"
        }

        response = self.api_client.send_request("POST", endpoint, data=data)

        # Log the response status
        logger.info(f"Quote created with response: {response}")

        return response

    def accept_quote(self, quote_uuid):
        logger.info(f"Accepting quote with UUID: {quote_uuid}")
        endpoint = f"/api/v1/quote/accept/{quote_uuid}"
        response = self.api_client.send_request("PUT", endpoint)

        # Log the response status
        logger.info(f"Quote accepted with response: {response}")

        return response

    def get_quote(self, quote_uuid):
        logger.info(f"Retrieving quote with UUID: {quote_uuid}")
        endpoint = f"/api/v1/quote/{quote_uuid}"
        response = self.api_client.send_request("GET", endpoint)

        # Log the response status
        logger.info(f"Retrieved quote with response: {response}")

        return response

    def get_quote_uuid(self, response):
        logger.info(f"Extracting UUID from quote response")
        quote_uuid = response.get("uuid")
        logger.info(f"Extracted UUID: {quote_uuid}")
        return quote_uuid

