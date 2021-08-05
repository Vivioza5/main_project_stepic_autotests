import time

import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.locators import MainLocators
from .pages.product_page import ProductPage
link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
# link = "http://selenium1py.pythonanywhere.com/"

email = (str(time.time())) + "@fakemail.org"
password=str((time.time()) +20)
@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
      self.browser = browser
      email = (str(time.time())) + "@fakemail.org"
      password=str((time.time()) +20)
      page = MainPage(browser, link)
      page.open()
      page.go_to_login_page()
      login_page = LoginPage(browser, browser.current_url)
      login_page.register_new_user(email, password)
      login_page.should_be_authorized_user()

    # @pytest.mark.main
    def test_user_cant_see_success_message(self, browser):
        product = ProductPage(browser, link)
        product.open()
        product.should_not_be_success_message()


    def test_guest_cant_see_success_message(self,browser):
        product=ProductPage(browser, link)
        product.open()
        product.should_not_be_success_message()

def test_user_can_add_product_to_basket(self,browser):
   link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
   product=ProductPage(browser, link)
   product.open()
   product.add_to_cart_foo()
   # product.solve_quiz_and_get_code()
   product.item_added_to_cart()
   product.item_added_to_cart_right()
   product.should_not_be_success_message()

def test_guest_can_add_product_to_basket(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        product=ProductPage(browser, link)
        product.open()
        product.add_to_cart_foo()
        product.solve_quiz_and_get_code()
        product.item_added_to_cart()
        product.item_added_to_cart_right()
        product.should_not_be_success_message()

def test_guest_cant_see_success_message_after_adding_product_to_basket(self,browser):
    product=ProductPage(browser, link)
    product.open()
    product.add_to_cart_foo()
    product.solve_quiz_and_get_code()
    product.should_not_be_success_message()



def test_message_disappeared_after_adding_product_to_basket(browser):
    product=ProductPage(browser, link)
    product.open()
    product.add_to_cart_foo()
    product.solve_quiz_and_get_code()
    product.should_not_be_success_message_visible()
@pytest.mark.new
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.new
def test_guest_can_go_login_link_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


    # Datas set for perametrize task
    # @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    #                       pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    #                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])