from django.db import models
import uuid


def generate_unique_seat_number():
    return str(uuid.uuid4())[:4]

class Flight(models.Model):
    flight_name = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    # Add more fields as needed

    def __str__(self):
        return self.flight_name

class Passenger(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    seat_number = models.CharField(max_length=10, unique=True, default=generate_unique_seat_number)
    # Add more fields as needed

    def __str__(self):
        return self.seat_number
    
    def save(self, *args, **kwargs):
        if not self.seat_number:
            self.seat_number = generate_unique_seat_number()
        super(Passenger, self).save(*args, **kwargs)