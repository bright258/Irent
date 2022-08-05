# in buiilt django dependencies

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# python dependencies
import datetime

# others

from .enums import (
    Currency,
    HouseStatus,
    Category
)
from .managers import CustomManager

# third party dependencies
from cloudinary.models import CloudinaryField
# models

class CustomUser(AbstractUser):
    email = models.EmailField(unique= True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)



    objects = CustomManager()
    REQUIRED_FIELDS =['username']
    USERNAME_FIELD: str = 'email'


    def __str__(self):
        return self.email

    
    



class Base(models.Model):
    created_at = models.DateTimeField(_('created_at'), auto_now_add= True )
    updated_at = models.DateTimeField(_('updated_at'), auto_now = True )

    class Meta:
        abstract = True
        get_latest_by = 'updated_at'
        ordering = ('-updated_at', '-created_at')




class Country(Base):
    name = models.CharField(_('name'), max_length = 100, null = False, blank = False)

    class Meta:
        verbose_name = 'Countries'

    def __str__(self):
        return self.name
        

class State(Base):
    country = models.ForeignKey(Country,on_delete= models.CASCADE, related_name= 'country')
    name = models.CharField(_('name'), max_length= 200, null = False)

    def __str__(self):
        return self.name



class City(Base):
    state = models.ForeignKey(State, on_delete=  models.CASCADE, related_name = 'state' )
    name = models.CharField(_('name'), max_length = 200, null = False)

    class Meta:
        verbose_name = 'Cities'

    def __str__(self):
        return self.name
        



class House(Base):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'seller')
    name = models.CharField(_('name'), max_length = 200, null = False)
    description = models.TextField(_('description'), max_length= 2000,  null = False, blank = False)
    
    image = CloudinaryField('image', null = True, blank = True)
    video = CloudinaryField(resource_type = 'auto', null = True, blank = True)
    price = models.DecimalField(_('price'), max_digits = 11, decimal_places= 2)
    currency = models.CharField(
        _('currency'), 
        max_length = 200, choices = Currency.choices, default = Currency.NGN)
    category = models.CharField(
        _('category'), max_length= 200, choices = Category.choices, default = Category.RENT)
    location = models.TextField(_('location'),max_length= 1000)
    city = models.ForeignKey(City, on_delete= models.CASCADE, related_name= 'city')
    
    status = models.CharField(
        _('status'), 
        max_length = 200, 
        default = HouseStatus.choices, choices = HouseStatus.choices)

    
    def __str__(self):
        return f'{self.name} selling at {self.price} by {self.seller}'
    
    @property
    def image_url(self):
        return(
            f'https://res.cloudinary.com/dmjwzcjel/{self.image}'
        )
    @property
    def video_url(self):
        return(
            f'https://res.cloudinary.com/dmjwzcjel/{self.video}'
        )

    
