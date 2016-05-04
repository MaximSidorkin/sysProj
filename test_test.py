import unittest, inspect, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from xmlrunner import xmlrunner

from selenium import selenium

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in driver.page_source
        elem.send_keys(Keys.RETURN)
        spin = driver.find_element_by_class_name('fa fa-spinner fa-spin fa-2x') # or css selector is 'i.fa fa-spinner fa-spin fa-2x'
        if spin.size == 0:
            print('True')
        else:
            print('False')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
