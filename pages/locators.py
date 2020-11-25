from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_LINK = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    PASSWORD_LINK1 = (By.CSS_SELECTOR, "input#id_registration-password1")
    PASSWORD_LINK2 = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGIS_BTN = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    TOTAL_COST = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCES_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)") 


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT = (By.CSS_SELECTOR, "h2.col-sm-6.h3")
    MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")
