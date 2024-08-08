import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--remote-debugging-port=9222')
    chrome_options.binary_location = '/usr/bin/google-chrome'  # Caminho para o binário do Chrome
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
