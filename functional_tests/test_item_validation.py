from .tests import FunctionalTest

class PanFieldTest(FunctionalTest):

	def test_pan_number_should_not_be_empty(self):
		pan_inputbox = self.get_element('id_pan_number')
		pan_inputbox.send_keys('\n')
		error = 



	def get_element(self,element_id):
		return self.find_element_by_id(element_id)