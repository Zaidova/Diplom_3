from selenium.webdriver.common.by import By


CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
INGREDIENT_ELEM = (By.XPATH, ".//a[@href='/ingredient/{}']")
INGREDIENT_ELEM_COUNTER = (By.XPATH, ".//a[@href='/ingredient/{}']/div[contains(@class, 'counter_counter')]/p")
DETAILS_DIALOG_TITLE = (By.XPATH, './/h2[text()="Детали ингредиента"]')
DETAILS_DIALOG_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")
ORDER_BASKET = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list')]")
ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
ORDER_WINDOW_ID_HEADER= (By.XPATH, ".//div[contains(@class, 'Modal_modal__contentBox')]/p")
ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
ORDER_FINISH_WINDOW_CLOSE_BUTTON = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]")