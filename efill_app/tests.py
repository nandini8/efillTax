from django.test import TestCase
from django.http import HttpRequest
from efill_app.views import itr_form_view

# Create your tests here.

class HomePageView(TestCase):

	def test_home_page_template_rendered(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'ITRform.html')

	def test_can_save_POST_requests(self):
		request = HttpRequest()
		request.method = 'POST'
		request.POST['pan_number'] = '1234567890'
		response = itr_form_view(request)
		self.assertIn('1234567890', response.content.decode())