from .base import FunctionalTest
from unittest import skip
import time

class PanFieldTest(FunctionalTest):

	def test_open_browser(self):
		self.browser.get(self.live_server_url)
		self.assertIn( 'ITR Form' , self.browser.title)
		inputbox = self.get_element('id_pan_number')
		inputbox.send_keys('a\n')

		time.sleep(5)

	def test_pan_number_should_not_be_empty(self):
		self.browser.get(self.live_server_url)
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('\n')
		error = self.get_error_by_css_selector()
		self.assertEqual(error.text, "Pan number cannot be empty.")