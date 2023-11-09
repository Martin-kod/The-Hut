from django.db import models

# Create your models here.


class Booking(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    num_of_guests = models.IntegerField()

    def __str__(self):
        return self.last_name
