from pyexpat import model
from statistics import mode
from django.db import models
from users.models import User

class Seat(models.Model):
    seat_no = models.CharField(max_length=10)
    

class Seat_details(models.Model):
    seat_no = models.CharField(max_length=10)
    passenger_name = models.CharField(max_length=100,blank=True,null=True)
    seat_available = models.BooleanField(default=True)
    seta_book_by = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE)
    seat_booked_time = models.DateTimeField(blank=True,null=True)

busname_choise = (
    ("Volvo","Volvo"),
    ("Kartar","Kartar"),
    ("Mercedez-benz","Mercedez-benz"),
    ("Roadways","Roadways"),    
)

bustype_choise = (
    ("Regualar","Regualar"),
    ("AC","AC"),  
    )

seat_choise =(
    
)

# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(choices=busname_choise, max_length=60,default='test',null=True)
    bus_type = models.CharField(choices=bustype_choise, max_length=60,default='test',null=True)
    date = models.DateField()
    time = models.TimeField()
    seat = models.ManyToManyField(Seat_details,blank=True,null=True)
    available_seats = models.IntegerField(default=60)
    destination_from = models.CharField(max_length=50,blank=False)
    destination_to = models.CharField(max_length=50,blank=False)
    price = models.IntegerField(null=True)
    