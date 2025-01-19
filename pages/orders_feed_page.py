from pages.base_page import BasePage
import locators.orders_feed_page_locators as locators


class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self):
        return self.get_text_from_element(locators.ORDERS_FEED_TITLE)

    def wait_orders_feed(self):
        return self.find_element_with_wait(locators.ORDERS_FEED_TITLE)

    def click_on_first_order(self):
        return self.click_to_element(locators.FIRST_ORDER_CARD)

    def wait_order_details_window(self):
        return self.find_element_with_wait(locators.ORDER_DETAILS_WINDOW)

    def get_today_counter(self):
        return int(self.get_text_from_element(locators.ORDER_COUNTER_TODAY))

    def get_all_time_counter(self):
        return int(self.get_text_from_element(locators.ORDER_COUNTER_ALL_TIME))

    def find_order_id_text(self, order_id):
        locator = self.format_locator(locators.ORDER_ID_ELEMENT, order_id)
        return self.get_text_from_element(locator)

    def find_order_id_in_work_list(self, order_id):
        locator = self.format_locator(locators.ORDER_ID_IN_WORK, order_id)
        return self.find_element_with_wait(locator, 30).text