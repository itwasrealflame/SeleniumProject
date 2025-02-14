from selenium import webdriver
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def page_open(self,url):
        self.driver.get(url)

    def element_find(self,value):
        self.driver.find_element(By.XPATH,value)

    def element_click(self, value):
        self.driver.find_element(By.XPATH,value).click()

    def text_send(self,value,value1):
        self.driver.find_element(By.XPATH,value).send_keys(value1)

    def driver_close(self):
        self.driver.quit()
