from selenium import webdriver
from selenium.webdriver.common.by import By

class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def page_open(self,url):
        self.driver.get(url)


    def element_find(self,value):
        return self.driver.find_element(By.XPATH,value)


    def element_click(self, value):
        return self.driver.find_element(By.XPATH,value).click()


    def text_send(self,value,value1):
        self.driver.find_element(By.XPATH,value).send_keys(value1)


    def driver_close(self):
        self.driver.quit()


    def driver_switch(self,value):
        self.driver.switch_to.frame(value)


    def driver_switch_to_original(self):
        self.driver.switch_to.default_content()


    def driver_element_clear(self,value):
        self.driver.find_element(By.XPATH,value).clear()