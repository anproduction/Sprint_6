from selenium.webdriver.common.by import By


class OrderFormLocators:
    # Экран "Для кого самокат"
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_LIST = (By.CLASS_NAME, 'select-search__select')
    SELECTED_STATION = (By.XPATH, ".//li[@class='select-search__row']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON = (By.XPATH, '//button[contains(text(), "Далее")]')


    # Экран "Про аренду"
    TITLE_ABOUT_RENT_FORM = (By.XPATH, "//div[contains(text(), 'Про аренду')]")
    RENTAL_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    CALENDAR = (By.CLASS_NAME, 'react-datepicker__month-container')
    TODAY_DATE = (By.CSS_SELECTOR, 'div.react-datepicker__day--today')
    TOMORROW_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='30']")
    RENTAL_DURATION_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_DURATION_LIST = (By.CLASS_NAME, 'Dropdown-menu')
    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='трое суток']")
    RENTAL_DURATION_AFTER_INPUT = (By.CLASS_NAME, 'Dropdown-placeholder is-selected')
    CHOOSE_COLOR_FIELD = (By.XPATH, '//div[text()="Цвет самоката"]')
    CHECKBOX_GREY = (By.ID, 'grey')
    COMMENT_FIELD = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    BUTTON_VIEW_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')

    # Попапы
    POP_UP_CONFIRM_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    YES_BUTTON_POP_UP_CONFIRM_ORDER = (By.XPATH, '//button[text()="Да"]')
    POP_UP_COMPLETE_ORDER = (By.XPATH, '//div[contains(@class, "Order_ModalHeader") and contains(text(), "Заказ оформлен")]')
