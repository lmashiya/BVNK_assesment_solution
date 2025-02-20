import logging

logger = logging.getLogger("e2e_api_tests")

class Wallet:
    def __init__(self, api_client):
        self.api_client = api_client

    def list_wallets(self):
        logger.info("Listing all wallets")
        endpoint = "/api/wallet"
        response = self.api_client.send_request("GET", endpoint)

        logger.info(f"Listed wallets with response: {response}")

        return response

    def get_wallet(self, wallet_id):
        logger.info(f"Getting details for wallet ID: {wallet_id}")
        endpoint = f"/api/wallet/{wallet_id}"
        response = self.api_client.send_request("GET", endpoint)

        logger.info(f"Retrieved wallet details with response: {response}")

        return response

    def get_wallet_balance(self, wallet_id):
        logger.info(f"Getting balance for wallet ID: {wallet_id}")
        response = self.get_wallet(wallet_id)

        balance = response["balance"]
        logger.info(f"Wallet ID: {wallet_id} has balance: {balance}")

        return balance

    def get_wallet_id(self, currency):
        logger.info(f"Getting wallet ID for currency: {currency}")
        ids = {}
        response = self.list_wallets()

        # Extract and log the wallet IDs
        for wallet in response:
            ids[wallet["currency"]["code"]] = int(wallet["id"])

        wallet_id = ids.get(currency, None)
        logger.info(f"Wallet ID for currency {currency}: {wallet_id}")

        return wallet_id
