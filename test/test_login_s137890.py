import unittest
from selenium.webdriver import Chrome
from lib.ui.loginpage import Loginpage

class TestLoginS137890P1(unittest.TestCase):

    def setUp(self):
        self.driver = Chrome('./chromedriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("http://demo.actitime.com")
        self.login_page = Loginpage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_login_invalid_tc1238990(self):
        #go to login page
        self.login_page.wait_for_login_page_to_load()
        #enter username
        self.login_page.get_username_textbox().send_keys("admin")
        #enter password
        self.login_page.get_password_textbox().send_keys("invalid")
        #Click on login button
        self.login_page.get_login_button().click()
        #get error msg
        actual_error_msg = self.login_page.get_login_error_msg().text
        expected_error_msg = 'Username or Password is invalid. Please try again.'
        #verify error msg
        assert actual_error_msg == expected_error_msg