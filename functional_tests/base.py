from selenium import webdriver
import unittest

class FunctionalTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		

	def tearDown(self):
		self.browser.quit()

	def test_start_browser(self):
		self.browser.get('http://localhost:8000/')
		self.browser.implicitly_wait(10)
