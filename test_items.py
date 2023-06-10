import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_button_add_cart(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
    assert button, "The Cart Button is not present!"
    