import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, driver):
        self.driver = driver


    '''Метод возврата URL'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    '''Метод проверки слов'''

    @staticmethod
    def text_checking(word, result):
        value_word = word.text
        assert value_word == result, 'Данный товар не найден'
        print("Good value_word:" + value_word)

    '''Метод Screenshot'''

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\admin\\Desktop\\QA\\автоматизация_тест\\main_project\\screen\\' + name_screenshot)

    '''Метод проверки URL'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    '''Метод навигации на элемент'''

    def hover_to_element(self, element):
        try:
            # Наведение на элемент с использованием ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print(f"Наведение на элемент после прокрутки: {element.text}")

        except Exception as e:
            print(f"Произошла ошибка при наведении на элемент: {e}")

    '''Метод навигации на элемент'''

    def hover_and_click_to_element(self, element):
        try:
            # Прокручиваем элемент в зону видимости
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

            # Наведение на элемент с использованием ActionChains
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            print(f"Наведение на элемент после прокрутки: {element.text}")
            time.sleep(3)

            # Клик на элемент
            element.click()
            print("Элемент успешно кликнут.")

        except Exception as e:
            print(f"Произошла ошибка при наведении на элемент или клике: {e}")
