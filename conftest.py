from selenium import webdriver
from selenium. webdriver.chrome.options import Options
from selene import Browser, Config



new
@pytest. fixture(scope=' function')
def setup_browser (request):
    options = Options)
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid: options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
options.capabilities.update(selenoid_capabilities)
driver = webdriver. Remote(
    command_executor=f"https://user1:1234@seLenoid.autotests.cloud/wd/hub", 
    options=options
)

browser = Browser(Config(driver))
yield browser

browser.quit()
