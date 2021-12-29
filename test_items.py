import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_find_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    button_busket = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    button_busket.click()