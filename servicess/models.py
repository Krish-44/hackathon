from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    alt_text = models.CharField(max_length=255)

    def __str__(self):
        return self.title


#Import your ServiceProvider model

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"Booking for {self.service.title} by {self.user_name}"
