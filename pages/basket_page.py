from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):   
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), \
       "Product is in the basket, but should not be"
        
    def should_be_success_message_basket_is_empty(self):
        assert  self.is_element_present(*BasketPageLocators.MESSAGE), \
       "Basket is not empty"
