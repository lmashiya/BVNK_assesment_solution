import pytest

@pytest.mark.parametrize(
    "amount, from_currency, to_currency",
    [
        (1, "ETH", "TRX"),
        (420, "TRX", "USDT"),
        (987, "TRX", "ETH")
    ],
)
def test_convert_from_currency_to_currency(api_client, quote_api, wallet_api, amount, from_currency
                                           , to_currency,logger):

    logger.info(f"Starting {from_currency} to {to_currency} conversion test")
    from_currency_id = wallet_api.get_wallet_id(from_currency)
    to_currency_id = wallet_api.get_wallet_id(to_currency)
    eth_before = wallet_api.get_wallet_balance(from_currency_id)
    trx_before = wallet_api.get_wallet_balance(to_currency_id)

    logger.info(f"Creating quote {from_currency} to {to_currency}")
    quote_response = quote_api.create_quote(amount, from_currency, to_currency, from_currency_id, to_currency_id)
    quote_uuid = quote_api.get_quote_uuid(quote_response)
    logger.info(f"Accepting quote {from_currency} to {to_currency} with uuid : {quote_uuid}")
    accept_quote_response = quote_api.accept_quote(quote_uuid)

    eth_after = wallet_api.get_wallet_balance(from_currency_id)
    trx_after = wallet_api.get_wallet_balance(to_currency_id)

    assert trx_after > trx_before
    assert eth_after < eth_before

    assert accept_quote_response["from"] == from_currency
    assert accept_quote_response["to"] == to_currency
    assert float(accept_quote_response["amountIn"]) == amount
    assert float(accept_quote_response["amountOut"]) > 0

    assert quote_uuid == accept_quote_response["uuid"]

    fee = accept_quote_response["fee"]
    fee_calculation = amount * 0.01/100
    assert float(fee) == round(fee_calculation,5)

    assert accept_quote_response["quoteStatus"] == "PAYMENT_OUT_PROCESSED"
    assert accept_quote_response["paymentStatus"] == "SUCCESS"
    logger.info(f"{from_currency} to {to_currency} conversion test passed ✅")
