from django.test import TestCase
from django.http import HttpRequest
from efill_app.views import itr_form_view
from efill_app.models import PersonalInfo
from django.core.exceptions import ValidationError
from django.db import IntegrityError, DataError


# Create your tests here.

class PersonalInfoModelTest(TestCase):

	def test_pan_should_be_unique(self):
		error = None
		personal_obj_1 = PersonalInfo.objects.create(pan_number = 'AAAPL1234C')
		try:
			personal_obj_2 = PersonalInfo.objects.create(pan_number = 'AAAPL1234C')
		except IntegrityError as e:
			error = "Pan number should be unique"

		self.assertEqual(error, "Pan number should be unique")

	def test_pan_characters_should_be_valid(self):
		personal_obj = PersonalInfo.objects.create(pan_number = 'AAAPL1234C')
		self.assertRegex(personal_obj.pan_number, '^[A-Z]{5}[0-9A-Z]{5}$')

		try:
			personal_obj = PersonalInfo.objects.create(pan_number = '1A34254VC4K')
			self.assertNotRegex(personal_obj.pan_number, '^[A-Z]{5}[0-9A-Z]{5}$')
		except DataError:
			error = "Invalid PAN number"
		
