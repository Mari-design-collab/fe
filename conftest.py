import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default=None, help="Choose language for testing"
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = webdriver.ChromeOptions()
    if language is not None:
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
    
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
