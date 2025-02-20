# BVNK API Testing

This repository contains E2E API tests for the BVNK simulated customer API, focusing on currency conversions/trades using Python.

## Directory Structure
── config.ini            
│── requirements.txt      
│── src/                  
│── tests/                
│── utils/                
── confest.py

## Setup

1. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Ensure your `config.ini` file contains the correct API base URL and any other necessary configurations.

## Running Tests

To run the tests:
```
pytest
```

This will automatically discover and execute all the tests in the `tests/` directory.

## Fixtures and Logging

- **Fixtures:** The tests use several fixtures defined in `conftest.py` to handle the setup of necessary components such as the API client, wallet API, and quote API.
- **Logging:** Logging is configured in `conftest.py` and is used across the tests to provide detailed logs during test execution.

## Tests Overview

- **Convert/trade Tests:** Tests for transer/trade between different currencies.
- **Wallet Tests:** Tests for wallet creation, balance retrieval, and more.
- **Quote Tests:** Tests for creating, accepting, and querying quotes for currency conversions.

D3d0<











