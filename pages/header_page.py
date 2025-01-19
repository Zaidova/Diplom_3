from pages.base_page import BasePage
import locators.header_page_locators as locators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def move_to_orders_feed(self):
        self.click_to_element(locators.ORDERS_FEED_HEADER)

    def move_to_constructor(self):
        self.click_to_element(locators.CONSTRUCTOR_BUTTON)

    def move_to_account(self):
        self.click_to_element(locators.ACCOUNT_BUTTON)