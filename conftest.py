import pytest
import time
from selenium import webdriver

@pytest.fixture(scope="module")

def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
