import pytest
from pool_object import pool_container

@pytest.mark.usefixtures('decoration')
class BaseTest:

    driver = None

    def setup(self):
        self.driver = pool_container.pool.get_driver().driver
        self.driver.maximize_window()

    def teardown(self):
        self.driver.close()
        self.driver.quit()
