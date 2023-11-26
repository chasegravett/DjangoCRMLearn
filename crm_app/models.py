from django.db import models


class Customer(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=10)


    def __str__(self):
        return (f"{self.first_name} {self.last_name}")