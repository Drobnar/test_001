import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: Chrome or Firefox")	
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en or ru")				 
					 
@pytest.fixture(scope="function")
def browser(request):
	browser_name = request.config.getoption("browser_name")
	user_language = request.config.getoption("language")
	if(browser_name == "chrome"):
		options = Options()
		options.add_experimental_option('prefs', \
										{'intl.accept_languages': user_language})
		print("\n\nStart Chrome browser fot test...")
		browser = webdriver.Chrome(options=options)
	elif(browser_name == "firefox"):
		fp = webdrider.FirefoxProfile()
		fp.set_preference('intl.accept_languages', user_language)	
		print("\n\nStart Firefox browser fot test...")
		browser = webdriver.Firefox(options=options)
	else:
		print("Browser <browser name> still is not implemented")
	yield browser
	print("\nQuit browser...")
	time.sleep(10)
	browser.quit()