from selenium import webdriver
import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys

class FunctionalTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(10)
		

	def tearDown(self):
		self.browser.quit()

	def test_open_browser(self):
		self.browser.get(self.live_server_url)
		self.assertIn( 'ITR Form' , self.browser.title)
		inputbox = self.browser.find_element_by_id('id_pan_number')
		inputbox.send_keys('a')