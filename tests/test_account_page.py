import data
import allure


class TestAccountPage:
    @allure.title('Переход к истории заказов')
    def test_go_to_orders_feed(self, header_page, main_page, account_page, user_credentials):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        header_page.move_to_account()

        account_page.go_to_orders_history()
        account_page.wait_orders_history_transition()

        assert account_page.get_active_item_text() == data.ORDERS_HISTORY_ITEM_TEXT

    @allure.title('Выход из аккаунта')
    def test_logout(self, header_page, main_page, account_page, user_credentials):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        header_page.move_to_account()
        account_page.logout()

        assert account_page.get_login_form_text() == data.LOGIN_FORM_TITLE