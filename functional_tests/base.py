from selenium import webdriver
import unittest, time, sys
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
#from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class FunctionalTest(LiveServerTestCase):

	'''
	@classmethod
	def setUpClass(cls):
		for arg in sys.argv:
			if 'liveserver' in arg:
				cls.server_url = 'http://' + arg.split('=')[1]
				return
		super().setUpClass()
		cls.server_url = cls.live_server_url

	@classmethod
	def tearDownClass(cls):
		if cls.server_url == cls.live_server_url:
			super().tearDownClass()
	'''

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(10)
		

	def tearDown(self):
		self.browser.quit()

	def get_element(self,element_id):
		return self.browser.find_element_by_id(element_id)

	def get_error_by_css_selector(self):
		return self.browser.find_element_by_css_selector('.has-error')