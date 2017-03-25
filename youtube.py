from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def search(keyword):
    driver = webdriver.Chrome()
    driver.get('http://www.pandora.com/')
    search_bar = driver.find_element_by_id('masthead-search-term')
    search_bar.send_keys(keyword + " music playlist")
    search_bar.send_keys(Keys.ENTER)
    links = driver.find_elements_by_xpath('//*[@href]')
    links.click()
    time.sleep(3000)
    #driver.quit()


search("happy")
