import pytest
from src.api_client import APIClient
from src.auth import Auth
from src.qoute import Quote
from src.wallet import Wallet
import logging


@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger("e2e_api_tests")
    return logger

@pytest.fixture(scope="session")
def auth(logger):
    auth_instance = Auth(None, logger)
    return auth_instance

@pytest.fixture(scope="session")
def api_client(auth,logger):
    client = APIClient(auth,logger)
    auth.api_client = client
    return client


@pytest.fixture(scope="session")
def quote_api(api_client,logger):
    return Quote(api_client=api_client,logger=logger)


@pytest.fixture(scope="session")
def wallet_api(api_client,logger):
    return Wallet(api_client=api_client,logger=logger)
