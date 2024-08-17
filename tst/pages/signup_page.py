import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tst.base.base_class import Base


class Signup_page(Base):
    """ Класс содержащий локаторы и методы для страницы поиск и выбор товара"""


    # Локаторы

    first_name_field = '//input[@id="edit-firstname"]'
    last_name_field = '//input[@id="edit-lastname"]'
    email_field = '//input[@id="edit-email"]'
    phone_field = '//input[@id="edit-phone"]'
    company_field = '//input[@id="edit-company"]'
    country_field = '//select[@name="country"]'
    option_country = '//option[@value="Russian Federation"]'
    submit_button = '//input[@data-drupal-selector="edit-submit"]'



    # Getters - методы, которые будут осуществлять поиск элементов, по локаторам, используя определенные условия поиска, и возвращающие результат данного поиска.

    def get_first_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_field)))

    def get_company_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.company_field)))

    def get_country_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country_field)))

    def get_option_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.option_country)))

    def get_submit_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))

    # Actions - методы, которые будут принимать результат поиска от Getters и производить требуемое действие, например кликать или вводить требуемую информацию.


    def input_first_name_field(self):
        self.get_first_name_field().send_keys("Ivan")
        print("Input name")

    def input_last_name_field(self):
        self.get_last_name_field().send_keys("Ivanov")
        print("Input surname")

    def input_email_field(self):
        self.get_email_field().send_keys("puk.kak.03@mail.ru")
        print("Input email")

    def input_phone_field(self):
        self.get_phone_field().send_keys("111")
        print("Input phone")

    def input_company_field(self):
        self.get_company_field().send_keys("Roga and copita")
        print("input company")

    def input_country_field(self):
        self.get_country_field().click()
        time.sleep(3)
        print("input country")

    def click_option_country(self):
        self.get_option_country().click()
        print("Click choose country")

    def click_submit_button(self):
        self.get_submit_button().click()
        print("Click submit")
        time.sleep(20)


    # Methods - метод, содержащий список Actions, представленных в виде действий, например один метод может включать в себя несколько действий: вести логин, ввести пароль, нажать кнопку "Войти".

    def input_signup(self):
        """Заполнение полей регистрации"""
        with allure.step("Input data user"):
            self.input_first_name_field()
            self.input_last_name_field()
            self.input_email_field()
            self.input_phone_field()
            self.input_company_field()
            self.input_country_field()
            self.click_option_country()
            self.scroll_page(0, 100)
            self.click_submit_button()