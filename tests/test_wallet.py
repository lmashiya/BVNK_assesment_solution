
def test_list_wallets(wallet_api, logger):
    logger.info("Starting test for listing wallets")

    response = wallet_api.list_wallets()

    logger.info(f"Received response: {response}")

    assert isinstance(response, list)
    assert response

    logger.info("List wallets test passed successfully ✅")


def test_get_wallet(wallet_api, logger):
    logger.info("Starting test for getting wallet by ID")

    wallet_id = wallet_api.get_wallet_id("ETH")
    logger.info(f"Wallet ID for ETH: {wallet_id}")

    response = wallet_api.get_wallet(wallet_id)
    logger.info(f"Received response: {response}")

    assert "id" in response
    assert response["id"] == wallet_id

    logger.info("Get wallet test passed successfully ✅")

