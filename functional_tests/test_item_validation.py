from .base import FunctionalTest
from unittest import skip
import time

class PanFieldTest(FunctionalTest):

	def test_open_browser(self):
		self.browser.get(self.live_server_url)
		self.assertIn( 'ITR Form' , self.browser.title)
		inputbox = self.get_element('id_pan_number')
		inputbox.send_keys('AAAPL1234C\n')

	'''def test_pan_number_should_be_unique(self):
		self.browser.get(self.live_server_url)
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAAPL1234C\n')
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAAPL1244C\n')
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAAPL1234C\n')
		error = self.get_element('pan_div')
		self.assertEqual(error.text, "Invalid PAN number")'''

	def test_pan_number_has_right_characters(self):
		self.browser.get(self.live_server_url)
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('AAA2345ASE\n')
		error = self.get_element('pan_div')
		self.assertEqual(error.text, "Invalid PAN number")

class LastNameFeildTest(FunctionalTest):

	def test_names_should_be_characters_only_and_last_name_should_not_be_null(self):
		self.browser.get(self.live_server_url)
		name_inputbox = self.get_element('id_first_name')
		name_inputbox.send_keys('Raj12\n')
		error = self.get_element('first_name_div')
		self.assertEqual(error.text, "Enter a valid first name")

		self.browser.get(self.live_server_url)
		name_inputbox = self.get_element('id_middle_name')
		name_inputbox.send_keys('Kumar.3\n')
		error = self.get_element('middle_name_div')
		self.assertEqual(error.text, "Enter a valid middle name")
	
		self.browser.get(self.live_server_url)
		name_inputbox = self.get_element('id_last_name')
		name_inputbox.send_keys('Koothrapa65lli\n')
		error = self.get_element('last_name_div')
		self.assertEqual(error.text, "Enter a valid last name")

class FlatNumberFieldTest(FunctionalTest):

	def test_flat_number_is_not_empty(self):
		self.browser.get(self.live_server_url)
		flat_inputbox = self.get_element('id_flat_number')
		flat_inputbox.send_keys('\n')
		error = self.get_element('flat_number_div')
		self.assertEqual(error.text, "Flat/ Building/ Door can not be empty")

