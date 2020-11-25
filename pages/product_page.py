from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage): 
    def go_to_product_page(self):
        busket_button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        busket_button.click()
   
    def should_be_add_product_to_basket(self):
        self.should_be_product_in_basket()
        self.should_be_basket_cost_equal_product_price()
        
    def should_be_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name in self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT).text, "Added to basket product and chosen one are different" 
        
    def should_be_basket_cost_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in self.browser.find_element(*ProductPageLocators.TOTAL_COST).text, "Basket price is not equal product cost"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
       "Success message is presented, but should not be"  
