import pytest

from SeleniumProject.selenium_init.Driver import Driver


class Tests:

    @pytest.fixture()
    def driver(self):
        driver = Driver()
        yield driver
        driver.driver_close()



