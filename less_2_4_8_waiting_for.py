import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/explicit_wait2.html'

browser.get(link)

button = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, 'price'), '100')
)
button = browser.find_element_by_class_name('btn.btn-primary')
button.click()

answer = browser.find_element_by_id('input_value')

price = calc(browser.find_element_by_id('input_value').text)
answer = browser.find_element_by_id('answer').send_keys(price)

button = browser.find_element_by_id('solve').click()

time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

