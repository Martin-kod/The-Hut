from django.test import TestCase
from .models import Booking

# Create your tests here.


class TestViews(TestCase):

    def test_thehut_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thehut/thehut_home.html')

    def test_thehut_booking_page(self):
        response = self.client.get('/thehut_booking')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thehut/thehut_booking.html')

    def test_edit_booking_page(self):
        booking = Booking.objects.create(first_name='Martin', last_name='Lind', email='mail@mail.com', num_of_guests=2)
        response = self.client.get(f'/edit/{booking.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'thehut/edit_booking.html')

    def test_can_add_booking(self):
        response = self.client.post('/add', {'first_name': 'test', 'last_name': 'test', 'email': 'test@test.com', 'num_of_guests': 2})
        self.assertRedirects(response, '/')

    def test_can_delete_booking(self):
        booking = Booking.objects.create(
            first_name='Martin', last_name='Lind', email='mail@mail.com', num_of_guests=2)
        response = self.client.get(f'/edit/{booking.id}')
        self.assertRedirects(response, '/')
        existing_bookings = Booking.objects.filter(id=booking.id)
        self.assertEqual(len(exisisting_items), 0)
