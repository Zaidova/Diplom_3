import data
import allure


class TestTransitions:
    @allure.title('Переход на страницу заказов')
    def test_go_to_orders_feed(self, header_page, orders_feed_page):
        header_page.move_to_orders_feed()
        assert orders_feed_page.get_title_text() == data.ORDERS_FEED_HEADER_TEXT

    @allure.title('Переход в Конструктор')
    def test_go_to_constructor(self, header_page, main_page, orders_feed_page):
        header_page.move_to_orders_feed()
        assert orders_feed_page.get_title_text() == data.ORDERS_FEED_HEADER_TEXT

        header_page.move_to_constructor()
        assert main_page.get_title_text() == data.CONSTRUCTOR_HEADER_TEXT

    @allure.title('Переход по клику в "Личный Кабинет"')
    def test_go_to_account(self, header_page, account_page):
        header_page.move_to_account()
        assert account_page.get_login_form_text() == data.LOGIN_FORM_TITLE