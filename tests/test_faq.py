import pytest
from pages.home_page import HomePage
from data import expected_texts
from urls import URLs
from locators.home_page_locators import HomePageLocators as Loc


@pytest.mark.parametrize("question_locator, answer_locator, expected_text_key", [
    (Loc.QUESTION_FAQ_1, Loc.ANSWER_FAQ_1, 'faq1'),
    (Loc.QUESTION_FAQ_2, Loc.ANSWER_FAQ_2, 'faq2'),
    (Loc.QUESTION_FAQ_3, Loc.ANSWER_FAQ_3, 'faq3'),
    (Loc.QUESTION_FAQ_4, Loc.ANSWER_FAQ_4, 'faq4'),
    (Loc.QUESTION_FAQ_5, Loc.ANSWER_FAQ_5, 'faq5'),
    (Loc.QUESTION_FAQ_6, Loc.ANSWER_FAQ_6, 'faq6'),
    (Loc.QUESTION_FAQ_7, Loc.ANSWER_FAQ_7, 'faq7'),
    (Loc.QUESTION_FAQ_8, Loc.ANSWER_FAQ_8, 'faq8'),
])
def test_faq_dropdown(driver, question_locator, answer_locator, expected_text_key):
    page = HomePage(driver)
    page.open(URLs.BASE_URL)
    page.close_cookie_window()

    page.scroll_to_faq()
    page.click_the_question(question_locator)

    answer_text = page.get_the_answer_text(answer_locator)

    actual = ' '.join(answer_text.split())
    expected = ' '.join(expected_texts[expected_text_key].split())

    assert actual == expected, f"Текст ответа для вопроса {expected_text_key} не совпадает.\nОжидали: {expected}\nПолучили: {actual}"
