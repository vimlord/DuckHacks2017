from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search(keyword):
    driver = webdriver.Chrome()
    driver.get('http://www.pandora.com/')
    #time.sleep(10)
    driver.find_element_by_class_name('SearchField__placeholder').click()
    search_bar = driver.find_element_by_class_name('SearchField__input')
    search_bar.send_keys(keyword)
    time.sleep(5)
    search_bar.send_keys(Keys.ENTER)

    time.sleep(3000)
    driver.quit()


search("rock")
