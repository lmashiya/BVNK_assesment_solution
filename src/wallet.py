
class Wallet:
    def __init__(self, api_client,logger):
        self.api_client = api_client
        self.logger = logger

    def list_wallets(self):
        self.logger.info("Listing all wallets")
        endpoint = "/api/wallet"
        response = self.api_client.send_request("GET", endpoint)

        self.logger.info(f"Listed wallets with response: {response}")

        return response

    def get_wallet(self, wallet_id):
        self.logger.info(f"Getting details for wallet ID: {wallet_id}")
        endpoint = f"/api/wallet/{wallet_id}"
        response = self.api_client.send_request("GET", endpoint)

        self.logger.info(f"Retrieved wallet details with response: {response}")

        return response

    def get_wallet_balance(self, wallet_id):
        self.logger.info(f"Getting balance for wallet ID: {wallet_id}")
        response = self.get_wallet(wallet_id)

        balance = response["balance"]
        self.logger.info(f"Wallet ID: {wallet_id} has balance: {balance}")

        return balance

    def get_wallet_id(self, currency):
        self.logger.info(f"Getting wallet ID for currency: {currency}")
        ids = {}
        response = self.list_wallets()

        for wallet in response:
            ids[wallet["currency"]["code"]] = int(wallet["id"])

        wallet_id = ids.get(currency, None)
        self.logger.info(f"Wallet ID for currency {currency}: {wallet_id}")

        return wallet_id
