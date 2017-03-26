from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = 0
open = 0
def init():
    global open 
    if open == False:
        global driver 
        driver = webdriver.Chrome()
        driver.get('http://www.pandora.com/')
        open = True
        time.sleep(2)

def search(keyword):
    init()
    driver.find_element_by_class_name('SearchField__placeholder').click()
    search_bar = driver.find_element_by_class_name('SearchField__input')
    search_bar.send_keys(keyword)
    time.sleep(3)
    search_bar.send_keys(Keys.ENTER)

    time.sleep(10)

