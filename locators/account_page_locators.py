from selenium.webdriver.common.by import By


LOGIN_FORM_TITLE = (By.XPATH, "//h2[text()='Вход']")
LOGIN_FORM_EMAIL_INPUT = (By.NAME, 'name')
LOGIN_FORM_PASSWORD_INPUT = (By.NAME, 'Пароль')
LOGIN_FORM_BUTTON = (By.XPATH, "//button[text()='Войти']")
PASSWORD_RECOVERY_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
ACTIVE_ITEM = (By.XPATH, '//a[contains(@class, "Account_link_active")]')
HISTORY_LIST_ACTIVE_ITEM = (By.XPATH, '//a[contains(@class, "Account_link_active") and text()="История заказов"]')
HISTORY_LIST = (By.XPATH, '//div[contains(@class, "OrderHistory_orderHistory")]')
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
ORDER_ID = (By.XPATH, '//p[contains(@class, "text text_type_digits")]')