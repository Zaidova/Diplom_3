from pages.base_page import BasePage
import locators.main_page_locators as locators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self):
        return self.get_text_from_element(locators.CONSTRUCTOR_TITLE)

    def wait_page_loading(self):
        self.find_element_with_wait(locators.CONSTRUCTOR_TITLE)

    def click_on_ingredient(self, ingredient_hash):
        locator = self.format_locator(locators.INGREDIENT_ELEM, ingredient_hash)
        self.click_to_element(locator)

    def get_ingredient_details_header(self):
        return self.get_text_from_element(locators.DETAILS_DIALOG_TITLE)

    def wait_ingredient_details_window(self):
        self.find_element_with_wait(locators.DETAILS_DIALOG_TITLE)

    def close_ingredient_details_window(self):
        self.click_to_element(locators.DETAILS_DIALOG_CLOSE_BUTTON)

    def wait_ingredient_details_window_is_closed(self):
        return self.wait_invisibility_of_element(locators.DETAILS_DIALOG_TITLE)

    def get_ingredient_counter_value(self, ingredient_hash):
        counter_locator = self.format_locator(locators.INGREDIENT_ELEM_COUNTER, ingredient_hash)
        return int(self.get_text_from_element(counter_locator))

    def add_ingredients_to_order(self, ingredient_hash):
        ingredient_locator = self.format_locator(locators.INGREDIENT_ELEM, ingredient_hash)
        self.drag_and_drop(ingredient_locator, locators.ORDER_BASKET)

    def click_order_button(self):
        self.click_to_element(locators.ORDER_BUTTON)

    def get_order_finish_id_header(self):
        return self.get_text_from_element(locators.ORDER_WINDOW_ID_HEADER)

    def wait_order_finish(self):
        self.wait_correct_order_number(locators.ORDER_NUMBER)

    def get_order_id(self):
        return self.wait_correct_order_number(locators.ORDER_NUMBER)

    def close_order_finish_window(self):
        self.click_to_element(locators.ORDER_FINISH_WINDOW_CLOSE_BUTTON)