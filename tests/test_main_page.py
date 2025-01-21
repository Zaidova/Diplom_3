import data
import allure


class TestsMainPage:
    @allure.title('Открытие окна информации об ингредиенте')
    def test_open_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_HASH)

        assert main_page.get_ingredient_details_header() == data.INGREDIENT_DETAILS_HEADER_TEXT

    @allure.title('Закрытие окна информации об ингредиенте')
    def test_close_ingredient_details_window(self, main_page):
        main_page.click_on_ingredient(data.INGREDIENT_HASH)

        main_page.wait_ingredient_details_window()
        main_page.close_ingredient_details_window()

        assert main_page.wait_ingredient_details_window_is_closed()

    @allure.title('Увеличение счётчика ингредиента')
    def test_increase_ingredient_counter(self, main_page):
        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_HASH)
        assert counter == 0

        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)

        counter = main_page.get_ingredient_counter_value(data.INGREDIENT_HASH)
        assert counter == 2  # верх и низ бургера

    @allure.title('Оформление заказа')
    def test_make_order(self, header_page, main_page, account_page, user_credentials):
        header_page.move_to_account()
        account_page.wait_login_form()

        account_page.fill_login_form(user_credentials['email'], user_credentials['password'])
        main_page.wait_page_loading()

        main_page.add_ingredients_to_order(data.INGREDIENT_HASH)

        main_page.click_order_button()

        assert main_page.get_order_finish_id_header() == data.ORDER_FINISH_WINDOW_HEADER