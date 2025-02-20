
def test_quote(quote_api, wallet_api, logger):
    from_currency = "ETH"
    to_currency = "TRX"

    logger.info(f"Starting quote creation from {from_currency} to {to_currency}")

    from_currency_id = wallet_api.get_wallet_id(from_currency)
    to_currency_id = wallet_api.get_wallet_id(to_currency)

    logger.info(f"Wallet IDs - From: {from_currency_id}, To: {to_currency_id}")

    response = quote_api.create_quote(1, from_currency, to_currency, from_currency_id, to_currency_id)
    logger.info(f"Quote created successfully with response: {response}")

    assert "uuid" in response
    assert float(response["amountIn"]) == 1
    assert response["from"] == from_currency
    assert response["to"] == to_currency

    uuid = quote_api.get_quote_uuid(response)
    logger.info(f"Quote UUID obtained: {uuid}")
    accept_quote_response = quote_api.accept_quote(uuid)
    logger.info(f"Quote accepted with response: {accept_quote_response}")

    assert accept_quote_response["paymentStatus"] == "SUCCESS"
    assert accept_quote_response["uuid"] == response["uuid"]

    get_quote_response = quote_api.get_quote(uuid)
    logger.info(f"Get quote response: {get_quote_response}")

    assert get_quote_response["paymentStatus"] == "SUCCESS"
    assert get_quote_response["uuid"] == response["uuid"]
    assert get_quote_response["acceptanceDate"] == accept_quote_response["lastUpdated"]
    assert get_quote_response["amountIn"] == response["amountIn"]

    logger.info(f"Quote test from {from_currency} to {to_currency} completed successfully ✅")

