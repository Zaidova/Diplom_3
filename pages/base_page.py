from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ищем элемент')
    def find_element_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                locator))
        self.driver.find_element(*locator).click()

    @allure.step('Вводим текст')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @staticmethod
    def format_locator(locator, value):
        return locator[0], locator[1].format(value)

    @allure.step('Прокручиваем страницу до нужного элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Переключение на другую вкладку')
    def change_tab(self, tab_number):
        self.driver.switch_to.window(self.driver.window_handles[tab_number])

    @allure.step('Перетаскиваем элемент')
    def drag_and_drop(self, src_locator, dst_locator):
        src_element = self.find_element_with_wait(src_locator)
        dst_element = self.find_element_with_wait(dst_locator)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(src_element, dst_element).perform()

    @allure.step('Получаем значение атрибута элемента')
    def get_attribute(self, locator, attribute):
        return self.find_element_with_wait(locator).get_attribute(attribute)

    @allure.step('Ожидание видимости элемента')
    def wait_invisibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Ожидание номера заказа')
    def wait_correct_order_number(self, number_locator):
        WebDriverWait(self.driver, 30).until_not(
            lambda driver: driver.find_element(*number_locator).text == "9999"
        )
        return self.get_text_from_element(number_locator)