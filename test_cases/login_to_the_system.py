import os
import time
import unittest

from selenium import webdriver

from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        self.user_login = LoginPage(self.driver)
        self.dashboard_page = Dashboard(self.driver)

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.check_title_of_header()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        time.sleep(5)

    def test_log_in_with_invalid_data(self):
        self.user_login.type_all_for_log_in('login', 'Pass123')
        self.user_login.log_in_with_invalid_data_message()
        self.user_login.title_of_page()
        time.sleep(5)

    def test_empty_password(self):
        self.user_login.type_all_for_log_in('login', '')
        self.user_login.empty_password_message()
        self.user_login.title_of_page()
        time.sleep(5)

    def test_log_out_from_the_system(self):
        self.user_login.type_all_for_log_in('user01@getnada.com', 'Test-1234')
        self.dashboard_page.check_sign_out_button()
        time.sleep(2)
        self.dashboard_page.click_on_the_sign_out_button()
        self.user_login.title_of_page()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()
