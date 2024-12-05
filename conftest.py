# Import necessary modules for logging, environment variable management, JSON handling, testing, 
# and Playwright for browser automation.
import logging
import os
import json
import pytest
from playwright.sync_api import sync_playwright
from pages.base import Base

# Define a fixture for logging that persists throughout the entire session.
@pytest.fixture(scope="session")
def logger():
    """
    Initializes and configures a logger to log test information into a file.

    Returns:
        logging.Logger: Configured logger instance.
    """
    # Create a logger with the name 'test_logger'.
    logger = logging.getLogger("test_logger")
    # Set the logging level to INFO to capture info, warning, and error logs.
    logger.setLevel(logging.INFO)

    # Create a handler to write log messages to a file.
    file_handler = logging.FileHandler("test_logs.log")
    # Define the format for the log messages.
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    # Attach the formatter to the file handler.
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger.
    logger.addHandler(file_handler)
    return logger

# Define a fixture for fetching and storing environment variables.
@pytest.fixture(scope="session")
def get_vars():
    """
    Retrieves necessary environment variables for test execution.

    Returns:
        dict: Dictionary containing environment variables (e.g., BASE_URL, USERNAME, PASSWORD).
    """
    vars = {}
    vars["BASE_URL"] = os.getenv("BASE_URL")  # Base URL of the application under test.
    vars["USERNAME"] = os.getenv("USERNAME")  # Username for login/authentication.
    vars["PASSWORD"] = os.getenv("PASSWORD")  # Password for login/authentication.
    return vars

# Define a fixture to manage the browser and page instance using Playwright.
@pytest.fixture(scope="session")
def page():
    """
    Sets up the browser and returns a new page instance for test interaction.

    Returns:
        playwright.sync_api.Page: Page object for interacting with the browser.
    """
    # Start the Playwright engine.
    playwright = sync_playwright().start()
    # Launch a new Chromium browser instance (set `headless=False` for debugging with browser UI).
    browser = playwright.chromium.launch()
    #browser = playwright.chromium.launch(headless=False)
    # Create a new browser context to maintain isolation between tests.
    context = browser.new_context()
    # Open a new page (tab) in the browser.
    page = context.new_page()
    return page

# Define a fixture for initializing the webpage and setting up test credentials.
@pytest.fixture
def webpage(page, get_vars):
    """
    Initializes the Base page object with the browser page and environment variables.

    Args:
        page (playwright.sync_api.Page): Browser page object.
        get_vars (dict): Dictionary containing environment variables.

    Returns:
        pages.base.Base: Base page object for test interactions.
    """
    # Create an instance of the Base class, passing in the browser page and test credentials.
    webpage = Base(
        page=page, 
        base_url=get_vars["BASE_URL"], 
        username=get_vars["USERNAME"], 
        password=get_vars["PASSWORD"]
    )
    return webpage
