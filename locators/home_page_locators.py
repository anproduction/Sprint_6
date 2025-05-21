from selenium.webdriver.common.by import By


class HomePageLocators:
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.CLASS_NAME, 'Button_Button__ra12g')
    ORDER_BUTTON_BODY = (By.CLASS_NAME, 'Button_Middle__1CSJM')

    # Основные элементы страницы
    HOW_IT_WORKS_BLOCK = (By.XPATH, '//div[text()="Как это работает"]')
    ACCEPT_COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    # FAQ (вопросы и ответы)
    FAQ_ITEMS = [
        {
            "question": (By.ID, f"accordion__heading-{i}"),
            "answer": (By.CSS_SELECTOR, f'div[aria-labelledby="accordion__heading-{i}"]:not([hidden]) p')
        }
        for i in range(8)
    ]

    # Логотипы
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    LOGO_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
