from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class AppUser(models.Model):
    user = models.ForeignKey(User)
    profileImage = models.ImageField(upload_to = settings.MEDIA_ROOT + "images")
class OfferedService(models.Model):
    seviceID = models.AutoField(primary_key = True)
    user_email = models.ForeignKey(User)
    title = models.CharField(max_length = 45)
    service_type = models.CharField(max_length = 45)
    account = models.BigIntegerField()
    company = models.BooleanField()
    company_name = models.CharField(max_length = 45)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_delimiter = models.CharField(max_length = 45)
    state = models.CharField(max_length =45)
    city = models.CharField(max_length = 45)
    service_image = models.IntegerField()
    brief_description = models.CharField(max_length = 140)
    descripton = models.TextField()
    service_email = models.EmailField(max_length = 70)
    telephone = models.CharField(max_length = 15)
    rating = models.IntegerField(blank = True, null = True)
class PurchasedService(models.Model):
    purchased_service_id = models.AutoField(primary_key = True)
    client_email =  models.ForeignKey(User)
    seller_email =  models.ForeignKey(OfferedService)
    date =  models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=7, decimal_places=2)
    ORDER = 0
    SHIPPED = 1
    DELIVERED = 2
    CLOSED = 3
    VALID_STATES_OPTIONS = (
        (ORDER, 'Comprado'),
        (SHIPPED, 'Enviado'),
        (DELIVERED, 'Entregado'),
        (CLOSED, 'Cerrado'),
    )
    status = models.IntegerField(choices = VALID_STATES_OPTIONS, default=ORDER)
    rating = models.IntegerField(blank = True, null = True)
