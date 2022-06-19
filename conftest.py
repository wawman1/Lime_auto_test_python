import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language is real")
    parser.addoption('--server', action='store', default="dev",
                     help="Choose language is real")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1920,1080)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.set_window_size(1920,1080)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox or you have chosen a bad language")
    yield browser
    print("\nquit browser..")
    browser.quit()
    
@pytest.fixture(scope="function")    
def get_baseurl(request):
    server_name = request.config.getoption('server')
    if server_name == "dev":
        print("\nstart server dev for test..")
        base_url = 'https://vetin.front.eclipseds.ru'
        
    elif server_name == "stage":
        print("\nstart server stage for test..")
        base_url = 'http://vetin-prod-front.eclipseds.ru/'
    
    elif server_name == "prod":
        print("\nstart server prod for test..")
        base_url = 'https://limelove.ru'
        
    else:
        raise pytest.UsageError("in base_page.py invalid server name, it must be dev or stage or prod")
    return base_url
