import logging
# Import page classes for structured page object model
from .auth import Auth
from .dashboard import Dashboard


# Initialize logger for the class
logger = logging.getLogger(__name__)


class Base:
    """
    Base class for initializing page objects and providing shared attributes and methods.
    """

    def __init__(self, page, base_url, username, password):
        """
        Initializes the Base class with common attributes and page objects.

        :param driver: WebDriver instance for browser interactions.
        :param base_url: Base URL of the website to test.
        :param username: Username for login.
        :param password: Password for login.
        """
        # Logging initialization of the Base class
        logger.info("Initializing Base")

        self.page = page
        self.username = username
        self.password = password
        self.base_url = base_url

        # Initialize page objects
        self.auth = Auth(self.page, self.base_url,self.username,self.password)
        self.dash = Dashboard(self.page, self.base_url)

        # Logging successful initialization of page objects
        logger.info("Page objects initialized")