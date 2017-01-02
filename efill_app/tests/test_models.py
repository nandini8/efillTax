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
		personal_obj_1 = PersonalInfo.objects.create(pan_number = 'AAAPL1234C', last_name='macintosh')
		try:
			personal_obj_2 = PersonalInfo.objects.create(pan_number = 'AAAPL1234C', last_name='macintosh')
		except IntegrityError as e:
			error = "Pan number should be unique"

		self.assertEqual(error, "Pan number should be unique")

	def test_pan_characters_should_be_valid(self):
		personal_obj = PersonalInfo.objects.create(pan_number = 'AAAPL1234C', last_name='macintosh')
		self.assertRegex(personal_obj.pan_number, '^[A-Z]{5}[0-9A-Z]{5}$')

		try:
			personal_obj = PersonalInfo.objects.create(pan_number = '1A34254VC4K', last_name='macintosh')
			self.assertNotRegex(personal_obj.pan_number, '^[A-Z]{5}[0-9A-Z]{5}$')
		except DataError:
			error = "Invalid PAN number"

	def test_fname_mname_lname_should_be_valid(self):

		personal_obj = PersonalInfo.objects.create(pan_number = 'AAAPL1234C', first_name="Penny", middle_name="lucifer",last_name="macintosh")
		self.assertRegex(personal_obj.first_name,'^[A-Za-z]{2,25}$')
		self.assertRegex(personal_obj.middle_name,'^[A-Za-z]{2,25}$')
		self.assertRegex(personal_obj.last_name,'^[A-Za-z]{2,25}$')

	def test_last_name_cannot_be_empty(self):
		error = None
		try:
			personal_obj = PersonalInfo.objects.create(pan_number = 'AAAPL1234C',last_name="")
			personal_obj.full_clean()
		except ValidationError:
			personal_obj.delete()
			error = "Last name cannot be empty"

		self.assertEqual(error,"Last name cannot be empty")

	def test_flat_number_can_not_be_empty(self):
		error = None
		flat_number = "54-C"
		assertNotEqual(flat_number, "")
		flat_number = ""
		assertEqual(flat_number, "")
		error = "Flat/ Building/ Door can not be empty"

		assertEqual(error.tests, "Flat/ Building/ Door can not be empty")







