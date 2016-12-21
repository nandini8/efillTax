from .base import FunctionalTest
from unittest import skip
import time

class PanFieldTest(FunctionalTest):

	def test_open_browser(self):
		self.browser.get(self.live_server_url)
		self.assertIn( 'ITR Form' , self.browser.title)
		inputbox = self.get_element('id_pan_number')
		inputbox.send_keys('AAAPL1234C\n')

		time.sleep(5)

	def test_pan_number_should_be_unique(self):
		self.browser.get(self.live_server_url)
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAAPL1234C\n')
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAAPL1244C\n')
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAAPL1234C\n')
		error = self.get_error_by_css_selector()
		self.assertEqual(error.text, "Pan number should be unique")

	def test_pan_number_has_right_characters(self):
		self.browser.get(self.live_server_url)
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAA2345ASE\n')
		error = self.get_error_by_css_selector()
		self.assertEqual(error.text, "Invalid PAN number")