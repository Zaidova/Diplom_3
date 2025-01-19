from pages.base_page import BasePage
import locators.password_recovery_page_locators as locators
import allure


class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_title_text(self):
        return self.get_text_from_element(locators.PASSWORD_RECOVERY_TITLE)

    def wait_page_ready(self):
        self.find_element_with_wait(locators.PASSWORD_RECOVERY_TITLE)

    def fill_email_form(self, email):
        self.add_text_to_element(locators.EMAIL_FIELD, email)
        self.click_to_element(locators.PASSWORD_RECOVERY_BUTTON)

    def find_new_password_field(self):
        return self.find_element_with_wait(locators.NEW_PASSWORD_FIELD)

    def click_open_hide_password_button(self):
         self.click_to_element(locators.BUTTON_PASSWORD_SHOW)

    def is_password_field_active(self):
        return 'input_status_active' in self.get_attribute(locators.NEW_PASSWORD_PARENT_DIV, 'class')