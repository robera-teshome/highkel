from asyncio.windows_events import NULL
from distutils.command.upload import upload
from pyexpat import model
from statistics import mode
from tabnanny import verbose
from tkinter import Image, Variable
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Hader(models.Model):
    office_phone = models.TextField(max_length=100)
    sel_phone = models.TextField(max_length=100)
    location = models.TextField(max_length=100)
    facebook = models.TextField(max_length=100)
    twitter = models.TextField(max_length=100)
    linkdean = models.TextField(max_length=100)
    logo_footer = models.ImageField( upload_to='Header', height_field=None, width_field=None, max_length=None)    
    logo_header = models.ImageField(upload_to='Header', height_field=None, width_field=None, max_length=None)
    logo_wite = models.ImageField(upload_to='Header', height_field=None, width_field=None, max_length=None)
    footer_description = models.TextField(max_length=300)
    
    class Meta:
        verbose_name = 'offive_Phone'
        verbose_name_plural = 'Header'

    def __str__(self):
        return self.location 

class slider(models.Model):
    title = models.TextField(max_length=100)
    slogone = models.TextField()
    discriptions = models.TextField(default='highkel')

    image = models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None )   
    list_title = models.TextField(max_length=100)
    lift_discription = models.TextField(max_length=100)
    right_title = models.TextField(max_length=100)
    ritht_discription = models.TextField(max_length=100)
    class Meta:
        verbose_name = 'slogone'
        verbose_name_plural = 'Slider'

    def __str__(self):
        return self.slogone


class status(models.Model):
    project_completed = models.TextField(max_length=100)
    project_completed_icon = models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None ) 
    patients_satisfied=models.TextField(max_length=100)
    patients_satisfied_icon= models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None ) 
    medical_beds = models.TextField(max_length=100)
    medical_beds_icon=  models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None ) 
    Laboratory_experts = models.TextField(max_length=100)
    Laboratory_experts_icon= models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None )
    service1 = models.TextField(max_length=100)
    service1_discription = models.TextField(max_length=100)
    service2 = models.TextField(max_length=100)
    service2_discription = models.TextField(max_length=100)
    service3 = models.TextField(max_length=100)
    service3_discription = models.TextField(max_length=100)
    service1_icon= models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None )
    service2_icon= models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None )
    service3_icon= models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None )
    back_icon= models.ImageField( upload_to='slide', height_field=None, width_field=None, max_length=None )

    class Meta:
        verbose_name = 'project_completed'
        verbose_name_plural = 'Highkel Status'
    def __str__(self):
        return self.project_completed 
            

    

        
          

