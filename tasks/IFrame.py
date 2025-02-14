from SeleniumProject.selenium_init.Consts import UrlPageFirst, IFRAME_CONST_FIRST, XPATH1
from SeleniumProject.selenium_init.Driver import Driver



class IFrame:

    def __init__(self,driver):
        self.driver = driver

    def get_page(self):
        self.driver.page_open(UrlPageFirst)

    def text_input(self):
        self.driver.driver_switch(IFRAME_CONST_FIRST)
        self.driver.driver_element_clear(XPATH1)