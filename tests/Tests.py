import pytest
from SeleniumProject.selenium_init.Consts import RAND_STRING
from SeleniumProject.selenium_init.Driver import Driver
from SeleniumProject.tasks.IFrame import IFrame
import time

class Tests:

    @pytest.fixture()
    def driver(self):
        driver = Driver()
        yield driver
        driver.driver_close()

    def test_iframe(self,driver):
        iframe = IFrame(driver)
        iframe.get_page()
        iframe.text_input()
        text = iframe.get_text()
        assert text == RAND_STRING, "string is not send to block"







