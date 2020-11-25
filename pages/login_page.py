from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Cant find word login in url" 

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, x, y):
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL_LINK)
        input1.send_keys(x)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_LINK1)
        input2.send_keys(y)
        input3 = self.browser.find_element(*LoginPageLocators.PASSWORD_LINK2)
        input3.send_keys(y)
        reg_btn = self.browser.find_element(*LoginPageLocators.REGIS_BTN)
        reg_btn.click()
