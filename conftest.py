import json
import os
import pytest


def pytest_addoption(parser):

    parser.addoption("--mybrowser", action="store", default="chromium")

    parser.addoption("--env", action="store", default="qa")


# Load environment configuration
@pytest.fixture(scope="session")
def env_config(request):

    env = request.config.getoption("--env")

    with open("Config/Config.json") as file:
        data = json.load(file)

    return data[env]


# Load test data
@pytest.fixture(scope="session")
def test_data():

    with open("Data/test_data.json") as file:
        return json.load(file)



# Create authenticated storage state once
@pytest.fixture(scope="session")
def authenticated_state(playwright, env_config, test_data):

    auth_file = "auth/user.json"
    # Reuse existing login session
    if os.path.exists(auth_file):
        return auth_file


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to login page
    page.goto(env_config["BASE_URL"])
    user = test_data["Valid_User"]
    page.get_by_placeholder("you@email.com").fill(user["Username"])


    page.get_by_placeholder("••••••").fill(user["Password"])
    page.get_by_role("button",name="Sign In").click()


    # Wait for homepage after login
    page.get_by_text("Discover & Book").wait_for(timeout=15000)


    # Save authentication
    os.makedirs(
        "auth",
        exist_ok=True
    )


    context.storage_state(
        path="auth/user.json"
    )


    context.close()
    browser.close()


    return "auth/user.json"



# Browser page fixture for tests
@pytest.fixture
def page(playwright, request, authenticated_state, env_config):


    browser_name = request.config.getoption(
        "--mybrowser"
    )


    if browser_name == "chromium":

        browser = playwright.chromium.launch(
            headless=False
        )


    elif browser_name == "firefox":

        browser = playwright.firefox.launch(
            headless=False
        )


    elif browser_name == "webkit":

        browser = playwright.webkit.launch(
            headless=False
        )


    else:
        raise Exception(
            f"Unsupported browser: {browser_name}"
        )



    context = browser.new_context(storage_state=authenticated_state)


    # Start tracing
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )


    page = context.new_page()


    # Open homepage with existing login
    page.goto(env_config["base_url"])


    yield page



    # Save trace
    os.makedirs(
        "traces",
        exist_ok=True
    )


    context.tracing.stop(
        path=f"traces/{request.node.name}.zip"
    )


    context.close()
    browser.close()



# Separate page for invalid login test
@pytest.fixture
def invalid_login_page(playwright):

    browser = playwright.chromium.launch(
        headless=False
    )


    context = browser.new_context()

    page = context.new_page()


    yield page


    context.close()
    browser.close()