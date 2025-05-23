from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver, timeout=60):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открытие страницы")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента с локатором")
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск множества элементов с локатором")
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание видимости элемента с локатором")
    def wait_for_element_to_be_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента с локатором")
    def wait_for_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Получение текста элемента")
    def get_text(self, *locator):
        element = self.find_element(*locator)
        return element.text

    @allure.step("Клик по элементу")
    def click(self, *locator):
        self.wait_for_element_to_be_visible(locator)
        element = self.driver.find_element(*locator)
        element.click()

    @allure.step("Ввод текста в элемент")
    def send_keys(self, locator, text):
        self.wait_for_element_to_be_visible(locator)
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Клик по элементу с ожиданием видимости")
    def click_with_wait(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Получить текст с элемента")
    def get_text_with_wait(self, locator):
        self.wait_for_element_to_be_visible(locator)
        return self.get_text(*locator)

    @allure.step("Поиск элемента с ожиданием видимости")
    def find_element_with_wait(self, locator):
        self.wait_for_element_to_be_visible(locator)
        return self.find_element(*locator)

    @allure.step("Проверка отображения элемента")
    def check_displaying_of_element(self, locator):
        element = self.find_element(*locator)
        assert element.is_displayed(), f"Элемент {locator} не отображается"

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Переключение на следующую вкладку")
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Ожидание URL")
    def wait_url_to_be(self, url):
        return self.wait.until(EC.url_to_be(url))