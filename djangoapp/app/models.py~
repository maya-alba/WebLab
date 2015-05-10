# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

SERVICE_TYPES = (
    ("LO", "Limpieza del hogar"),
    ("JA", "Jardinería"),
    ("SN", "Servicios de Niñería"),
    ("MA", "Mascotas"),
    ("CO", "Comida"),
    ("OT", "Otros servicios"),
)

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

PRICE_DELIMITER = (
    ("D", "Día"),
    ("H", "Hora"),
    ("U", "Unidad"),
    ("S", "Servicio"),
)

STATE = (
    ("JAL", "Jalisco"),
)

CITY = (
    ("ZAP", "Zapopan"),
    ("TON", "Tonala"),
    ("GDL", "Guadalajara"),
)


class AppUser(models.Model):
    user = models.ForeignKey(User)
    profileImage = models.ImageField(upload_to = settings.MEDIA_ROOT + "images")
class OfferedService(models.Model):
    seviceID = models.AutoField(primary_key = True)
    user_email = models.ForeignKey(User)
    title = models.CharField(max_length = 45)
    service_type = models.CharField(choices = SERVICE_TYPES, max_length = 45)
    account = models.BigIntegerField(max_length=16)
    company = models.BooleanField()
    company_name = models.CharField(null=True, blank=True, max_length = 45, help_text="Use in case that company filled")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    price_delimiter = models.CharField(choices = PRICE_DELIMITER, max_length= 45)
    state = models.CharField(choices=STATE, max_length =45)
    city = models.CharField(choices=CITY, max_length = 45)
    service_image = models.ImageField(upload_to = settings.MEDIA_ROOT + "offered_service", blank=True)
    brief_description = models.CharField(max_length = 140)
    descripton = models.TextField()
    service_email = models.EmailField(max_length = 70)
    telephone = models.CharField(max_length = 15)
    rating = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.user_email.first_name + u" - " + self.title

    def get_image(self):
        return self.service_image.path.split("media")[1].replace("\\", "/")

class PurchasedService(models.Model):
    purchased_service_id = models.AutoField(primary_key = True)
    client_email =  models.ForeignKey(User)
    seller_email =  models.ForeignKey(OfferedService)
    date =  models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.IntegerField(choices = VALID_STATES_OPTIONS, default=ORDER)
    rating = models.IntegerField(blank = True, null = True)
