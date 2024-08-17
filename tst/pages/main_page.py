import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tst.base.base_class import Base


class Main_page(Base):
    """ Класс содержащий локаторы и методы для страницы поиск и выбор товара"""

    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.driver = driver

    base_url = "https://www.blazemeter.com/university"


    # Локаторы

    start_testing_now_button = '//a[@class="try-for-free menu-item--collapsed"]'



    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_start_testing_now_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.start_testing_now_button)))

    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.


    def click_start_testing_now_button(self):
        self.get_start_testing_now_button().click()
        print("click button start testing now")

    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".

    def start_testing(self):
        """Нажатие кнопки start testing now"""
        with allure.step("Click start testing"):
            # self.get_current_url()
            # self.input_search_field()
            # self.scroll_page(0, 300)
            self.click_start_testing_now_button()
