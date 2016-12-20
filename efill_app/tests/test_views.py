from django.test import TestCase

class HomePageTest(TestCase):

	def test_home_template_used(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'efill_app/home.html')