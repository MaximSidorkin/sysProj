import unittest

from Check500404_test import AASeleniumAutoTest_1
from Check500404_test import BBSeleniumOpenAllPjct_2
from Check500404_dev import ASeleniumAutoTest_1
from Check500404_dev import BSeleniumOpenAllPjct_2

tests_classes=[
    ASeleniumAutoTest_1,
    BSeleniumOpenAllPjct_2,
    AASeleniumAutoTest_1,
    BBSeleniumOpenAllPjct_2
]

if __name__ == '__main__':
    unittest.main()