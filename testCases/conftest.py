import os
from datetime import datetime
import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "edge":
        browser = webdriver.Edge()
        print("--------------launching Edge browser-------------------")
    elif browser == "firefox":
        browser = webdriver.Firefox()
        print("----------------launching Firefox browser-----------------")
    else:
        browser = webdriver.Chrome()
        print("------------------launching Chrome browser-------------------")
    return browser


def pytest_addoption(parser):  # used to define custom command-line options that can be accessed within your tests.
    parser.addoption("--browser")  # This line adds a new option named --browser to the command-line parser. When
    # running pytest, you can now specify a browser value using this option.


@pytest.fixture()  # this will return the browser to setup method
def browser(request):  # This fixture function serves two purposes. 1st fetch cli values of -- browser
    return request.config.getoption("--browser")  # returns the retrieved browser value, making it available to any
    # test that uses this fixture.


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config.stash[metadata_key]["Tester"] = "Manoj Das"
    session.config.stash[metadata_key]["Module Name"] = "Registration"
    session.config.stash[metadata_key]["Project Name"] = "Nopcommerce"


def pytest_metadata(metadata):  # remove extra environment table data
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


# specifying the report folder location nad save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%d-%m-%Y %H-%M-%S") + ".html"
# pytest -s -v --html=reports\reports.html --capture=tee-sys .\testCases\test_001_accountregistration.py --browser edge  ( used to run on specific browser )

# pytest -s -v .\testCases\test_001_accountregistration.py --browser edge  ( used to run on specific browser )
