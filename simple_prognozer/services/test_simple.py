from unittest import TestCase
from echo.simple_method import *


class UtilsTestCase(TestCase):
    def test_country(self):
        r = simple_method()
        self.assertTrue(r.srartswith("US"))

if __name__ == '__main__':
    unittest.main()