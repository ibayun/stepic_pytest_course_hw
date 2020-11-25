from .pages.locators import AddToBasket
from .pages.main_page import MainPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket(*AddToBasket.BASKET_BUTTON)
    page.is_not_element_present(*AddToBasket.SUCCESS_TEXT)


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
    page = MainPage(browser, link)
    page.open()
    page.is_not_element_present(*AddToBasket.SUCCESS_TEXT)


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/neuromancer_13/"
    page = MainPage(browser, link)
    page.open()
    page.add_to_basket(*AddToBasket.BASKET_BUTTON)
    page.is_disappeared(*AddToBasket.SUCCESS_TEXT)
