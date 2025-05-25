from selenium.webdriver.common.by import By


class HomePageLocators:
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_BODY = (By.CLASS_NAME, 'Button_Middle__1CSJM')

    # Основные элементы страницы
    HOW_IT_WORKS_BLOCK = (By.XPATH, '//div[text()="Как это работает"]')
    ACCEPT_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    # FAQ (вопросы и ответы)

    # Вопросы
    QUESTION_FAQ_1 = (By.XPATH, ".//div[@id='accordion__heading-0']")
    QUESTION_FAQ_2 = (By.XPATH, ".//div[@id='accordion__heading-1']")
    QUESTION_FAQ_3 = (By.XPATH, ".//div[@id='accordion__heading-2']")
    QUESTION_FAQ_4 = (By.XPATH, ".//div[@id='accordion__heading-3']")
    QUESTION_FAQ_5 = (By.XPATH, ".//div[@id='accordion__heading-4']")
    QUESTION_FAQ_6 = (By.XPATH, ".//div[@id='accordion__heading-5']")
    QUESTION_FAQ_7 = (By.XPATH, ".//div[@id='accordion__heading-6']")
    QUESTION_FAQ_8 = (By.XPATH, ".//div[@id='accordion__heading-7']")

    # Ответы
    ANSWER_FAQ_1 = (By.XPATH, ".//div[@id='accordion__panel-0']")
    ANSWER_FAQ_2 = (By.XPATH, ".//div[@id='accordion__panel-1']")
    ANSWER_FAQ_3 = (By.XPATH, ".//div[@id='accordion__panel-2']")
    ANSWER_FAQ_4 = (By.XPATH, ".//div[@id='accordion__panel-3']")
    ANSWER_FAQ_5 = (By.XPATH, ".//div[@id='accordion__panel-4']")
    ANSWER_FAQ_6 = (By.XPATH, ".//div[@id='accordion__panel-5']")
    ANSWER_FAQ_7 = (By.XPATH, ".//div[@id='accordion__panel-6']")
    ANSWER_FAQ_8 = (By.XPATH, ".//div[@id='accordion__panel-7']")

    # Логотипы
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
