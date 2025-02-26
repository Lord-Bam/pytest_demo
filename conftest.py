import pytest
from car import Car
import logging
import os

ENVIRONMENTS = {
    "localhost": {"url": "http://localhost:5000", "username": "localuser", "password": "localpass"},
    "dev": {"url": "https://dev.example.com", "username": "devuser", "password": "devpass"},
    "staging": {"url": "https://staging.example.com", "username": "staginguser", "password": "stagingpass"},
    "prod": {"url": "https://prod.example.com", "username": "produser", "password": "prodpass"},
}

def pytest_addoption(parser):
    """Add a command-line option to select an environment"""
    parser.addoption("--env", action="store", default="localhost", help="Specify the test environment")
    parser.addoption("--url", action="store", help="Override the URL")
    parser.addoption("--username", action="store", help="Override the username")
    parser.addoption("--password", action="store", help="Override the password")

@pytest.fixture
def env(request):
    env = request.config.getoption("--env")
    config = ENVIRONMENTS.get(env, ENVIRONMENTS["localhost"]).copy()

    # Override with CLI options or fallback to environment variables
    config["url"] = request.config.getoption("--url") or os.getenv("TEST_URL", config["url"])
    config["username"] = request.config.getoption("--username") or os.getenv("TEST_USERNAME", config["username"])
    config["password"] = request.config.getoption("--password") or os.getenv("TEST_PASSWORD", config["password"])

    return config


@pytest.fixture
def newcar():
    return Car()

@pytest.fixture
def setup_teardown(logger):
    logger.info("setup")
    yield
    logger.info("teardown")

@pytest.fixture
def logger():
    logger = logging.getLogger("pytest_logger")
    logger.setLevel(logging.INFO)
    return logger

