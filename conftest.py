import logging
import os
import json
import pytest
from playwright.sync_api import sync_playwright
from pages.base import Base


@pytest.fixture(scope="session")
def logger():
    # Initialize the logger with the name 'test_logger'
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)  # Set the logging level to INFO

    # Create a file handler that logs messages into 'test_output/test_logs.log'
    file_handler = logging.FileHandler("test_logs.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)  # Set the format of log messages

    # Attach the file handler to the logger
    logger.addHandler(file_handler)
    return logger

@pytest.fixture(scope="session")
def get_vars():
    vars={}
    vars["BASE_URL"] = os.getenv("BASE_URL")
    vars["USERNAME"] = os.getenv("USERNAME")
    vars["PASSWORD"] = os.getenv("PASSWORD")
    return vars



# Load test data


@pytest.fixture(scope="session")
def page():
    # Initialize Playwright and start it.
    playwright = sync_playwright().start()
    # Launch the Chromium browser, with headless mode set to False (browser UI will be visible).
    browser = playwright.chromium.launch()
    #browser = playwright.chromium.launch(headless=False)
    # Open a new page (tab) in the browser.
    context = browser.new_context()
    page = context.new_page()
    return page


@pytest.fixture
def webpage(page, get_vars):
    # Instantiate the Base page object with driver and credentials
    webpage = Base(
        page=page, base_url=get_vars["BASE_URL"], username=get_vars["USERNAME"], password=get_vars["PASSWORD"]
    )
    return webpage