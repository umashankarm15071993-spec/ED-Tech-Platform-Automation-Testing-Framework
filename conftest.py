from pathlib import Path
import pytest
from selenium import webdriver
import config


def pytest_addoption(parser):
    parser.addoption(
                    "--browser",
                     action="store",
                     default="chrome",
                     help="choose browser chrome,firefox, or edge",
                     choices=["chrome", "firefox", "edge"])

@pytest.fixture(scope="function")
def driver(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        raise ValueError(f"unsupported browser:{browser}")
    driver.maximize_window()
    driver.get(config.BASE_URL)
    driver.implicitly_wait(config.IMPLICITLY_WAIT)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    result=yield
    outcome=result.get_result()

    if outcome.when == "call" and outcome.failed:
        driver=item.funcargs["driver"]
        Path("screenshot").mkdir(exist_ok=True)

        driver.save_screenshot(f"screenshot/{item.name}.png")





