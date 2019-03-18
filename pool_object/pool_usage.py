from pool_object.base_test import BaseTest


class TestClass(BaseTest):

    def setup(self):
        super(TestClass, self).setup()

    def test_one(self):
        self.driver.get('https://newsilpo.iir.fozzy.lan')

    def test_two(self):
        self.driver.get('https://silpo.ua')
