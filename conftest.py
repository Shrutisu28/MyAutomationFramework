import json

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--mybrowser",
        action="store",
        default="chromium"
    )

@pytest.fixture
def page(playwright, request):

    browser_name = request.config.getoption("--mybrowser")

    if browser_name == "chromium":
     browser = playwright.chromium.launch(headless=False)

    elif browser_name == "firefox":
     browser = playwright.firefox.launch(headless=False)

    elif browser_name == "webkit":
     browser = playwright.webkit.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    yield page

    context.close()
    browser.close()

@pytest.fixture(scope="session")
def test_data():

    with open("Data/test_data.json") as file:
        return json.load(file)