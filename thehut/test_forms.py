from django.test import TestCase
from .forms import BookingForm

# Create your tests here.


class TestBookingForm(TestCase):

    def test_booking_first_name_is_required(self):
        form = BookingForm({'first_name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors.keys())
        self.assertEqual(form.errors['first_name'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookingForm()
        self.assertEqual(form.Meta.fields, ['first_name', 'last_name', 'email', 'num_of_guests'])
