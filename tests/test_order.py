import pytest
from pages.home_page import HomePage
from pages.order_form_page import OrderFormPage
from data import ORDER_USERS
from urls import URLs


class TestSuccessfulOrder:

    @pytest.mark.parametrize("user_data", ORDER_USERS)
    def test_successful_order_from_header(self, driver, user_data):
        home_page = HomePage(driver)
        order_form = OrderFormPage(driver)

        home_page.open(URLs.BASE_URL)
        home_page.close_cookie_window()
        home_page.click_order_button_header()

        order_form.personal_information_input(
            name=user_data[0],
            last_name=user_data[1],
            address=user_data[2],
            station=user_data[3],
            number=user_data[4]
        )
        order_form.rental_information_input(comment=user_data[5])
        order_form.click_yes_button_confirmation_pop_up()
        order_form.check_displaying_of_confirm_window()
        order_form.close_complete_order_popup()

        home_page.click_logo_open_home_page()
        home_page.wait_url_to_be(URLs.BASE_URL)
        assert home_page.get_current_url() == URLs.BASE_URL, "Переход по логотипу Самоката на главную страницу"

        home_page.click_logo_yandex_open_dzen_page()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        home_page.wait_url_to_be(URLs.YANDEX_URL)
        assert home_page.get_current_url() == URLs.YANDEX_URL, "Переход по логотипу Яндекса на страницу Дзена"
        driver.close()
        driver.switch_to.window(handles[0])

    @pytest.mark.parametrize("user_data", ORDER_USERS)
    def test_successful_order_from_body(self, driver, user_data):
        home_page = HomePage(driver)
        order_form = OrderFormPage(driver)

        home_page.open(URLs.BASE_URL)
        home_page.close_cookie_window()
        home_page.scroll_to_order_button_body()
        home_page.click_order_button_body()

        order_form.personal_information_input(
            name=user_data[0],
            last_name=user_data[1],
            address=user_data[2],
            station=user_data[3],
            number=user_data[4]
        )
        order_form.rental_information_input(comment=user_data[5])
        order_form.click_yes_button_confirmation_pop_up()
        order_form.check_displaying_of_confirm_window()
        order_form.close_complete_order_popup()

        home_page.click_logo_open_home_page()
        home_page.wait_url_to_be(URLs.BASE_URL)
        assert home_page.get_current_url() == URLs.BASE_URL, "Переход по логотипу Самоката на главную страницу"

        home_page.click_logo_yandex_open_dzen_page()
        handles = driver.window_handles
        driver.switch_to.window(handles[-1])
        home_page.wait_url_to_be(URLs.YANDEX_URL)
        assert home_page.get_current_url() == URLs.YANDEX_URL, "Переход по логотипу Яндекса на страницу Дзена"
        driver.close()
        driver.switch_to.window(handles[0])
