from selenium import webdriver
import pytest
import allure

import api
import data
import helpers

from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from pages.password_recovery_page import PasswordRecoveryPage
from pages.orders_feed_page import OrdersFeedPage
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = Options()
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--incognito')
        driver = webdriver.Chrome(options=options)
    elif driver_class == webdriver.Firefox:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--width=1920')
        firefox_options.add_argument('--height=1080')
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
    driver.get(data.BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def header_page(driver):
    return HeaderPage(driver)


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture
def orders_feed_page(driver):
    return OrdersFeedPage(driver)


@pytest.fixture
def password_recovery_page(driver):
    return PasswordRecoveryPage(driver)


@pytest.fixture
def user_credentials():
    credentials = helpers.generate_new_user_credentials()
    api.new_user(credentials)

    yield credentials

    api.remove_user(credentials)