from time import sleep


def test_valid_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    try:
        button_basket = browser.find_element_by_class_name('btn-add-to-basket')
    except:
        print('something wrong. later try again')
    if button_basket:
        print('Congrats!')
    sleep(10)
