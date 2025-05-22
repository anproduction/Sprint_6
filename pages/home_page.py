import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from urls import URLs


class HomePage(BasePage):
    locators = HomePageLocators
    @allure.step('Нажатие кнопки "Заказать" в хедере')
    def click_order_button_header(self):
        self.click_with_wait(HomePageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Скролл до кнопки "Заказать" в теле страницы')
    def scroll_to_order_button_body(self):
        self.scroll_to_element(HomePageLocators.HOW_IT_WORKS_BLOCK)
        self.wait_for_element_to_be_visible(HomePageLocators.ORDER_BUTTON_BODY)

    @allure.step('Нажатие кнопки "Заказать" в теле страницы')
    def click_order_button_body(self):
        self.click_with_wait(HomePageLocators.ORDER_BUTTON_BODY)

    @allure.step('Закрытие окна куки')
    def close_cookie_window(self):
        self.click_with_wait(HomePageLocators.ACCEPT_COOKIE_BUTTON)

    @allure.step('Скролл до блока "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(HomePageLocators.FAQ_ITEMS[7]["question"])
        self.wait_for_element_to_be_visible(HomePageLocators.FAQ_ITEMS[7]["question"])

    @allure.step('Нажатие на вопрос')
    def click_the_question(self, question_locator):
        self.click_with_wait(question_locator)

    @allure.step('Получение текста ответа')
    def get_the_answer_text(self, answer_locator):
        return self.get_text_with_wait(answer_locator)

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_logo_yandex_open_dzen_page(self):
        self.click_with_wait(HomePageLocators.LOGO_YANDEX)
        self.switch_to_next_tab()
        self.wait_url_to_be(URLs.YANDEX_URL)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_logo_open_home_page(self):
        self.click_with_wait(HomePageLocators.LOGO_SAMOKAT)
