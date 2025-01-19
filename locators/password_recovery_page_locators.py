from selenium.webdriver.common.by import By

PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
PASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]")
EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')
BUTTON_PASSWORD_SHOW = (By.XPATH, "//div[@class='input__icon input__icon-action']")
NEW_PASSWORD_FIELD = (By.XPATH, '//input[@name="Введите новый пароль"]')
NEW_PASSWORD_PARENT_DIV = (By.XPATH, '//div[input[@name="Введите новый пароль"]]')