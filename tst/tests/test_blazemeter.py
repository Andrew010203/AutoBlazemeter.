import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tst.pages.main_page import Main_page
from tst.pages.signup_page import Signup_page

# @pytest.fixture
# def driver():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


base_url = "https://www.blazemeter.com/university"


# @pytest.fixture(scope="function", autouse=True)
# def driver(request):
#     options = Options()
#     options.add_argument('--headless')
#     options.add_argument('--no-sandbox')
#     options.add_argument('--window-size=1920,1080')
#     options.add_argument('--disable-dev-chm-usage')
#     driver = webdriver.Chrome(options=options)
#     request.cls.driver = driver
#     yield driver
#     driver.quit()


class Test_1:

    # @allure.description("Test registration")
    # def test_reg(self):
    #     options = Options()
    #     options.add_argument('--headless')
    #     service = Service(executable_path=ChromeDriverManager().install())
    #     driver = webdriver.Chrome(service=service)
    #     wait = WebDriverWait(driver, 30, poll_frequency=1)
    #     action: ActionChains = ActionChains(driver)
    #     driver.get(base_url)
    #     driver.set_window_size(1920, 1080)

    # def __init__(self):
    #     self.cls = None

    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('--disable-dev-chm-usage')
        driver = webdriver.Chrome(options=options)
        self.driver = driver
        driver.get(base_url)
        yield driver
        driver.quit()

    # @allure.description("Test registration")
    def test_reg(self, driver):
        print("start test")

        mp = Main_page(driver)
        mp.start_testing()

        sp = Signup_page(driver)
        sp.input_signup()


# test = Test_1()
# test.test_reg()