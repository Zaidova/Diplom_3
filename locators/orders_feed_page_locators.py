from selenium.webdriver.common.by import By


ORDERS_FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
FIRST_ORDER_CARD = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")
ORDER_DETAILS_WINDOW = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]")
ORDER_COUNTER_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number')]")
ORDER_COUNTER_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number')]")
ORDER_ID_ELEMENT = (By.XPATH, "//p[text()='#{}' and contains(@class, 'text_type_digits')]")
ORDER_ID_IN_WORK = (By.XPATH, "//li[contains(text()[2], '{}')]")