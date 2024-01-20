import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.doper.ba")
    driver.maximize_window()  
    yield driver
    driver.quit()
    
@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    yield wait