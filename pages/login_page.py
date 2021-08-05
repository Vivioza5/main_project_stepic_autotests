from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url=self.browser.current_url
        assert 'login' in cur_url,  "Login link is not opened"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self,email,password):
        input_email=self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        input_email.clear()
        input_email.send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).clear()
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT).clear()
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_INPUT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
