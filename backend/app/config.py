import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


class BaseConfig:
    """ this base class contains settings that are common to all configurations.
    Additional configurations can be added by subclasses as needed.
    """

    ENV = "development"

    # Flask configuration
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess"
    

class DevelopmentConfig(BaseConfig):
    """Configuration for the dev (and local) environment."""

    CORS_ORIGINS = ["http://localhost:3000"]

class TestConfig(BaseConfig):
    """Configuration for the test environment."""

    ENV = "test"

class ProductionConfig(BaseConfig):
    """Configuration for the prod environment."""

    ENV = "production"

class UnitTestConfig(BaseConfig):

    ENV = "unit_test"

    TESTING = True