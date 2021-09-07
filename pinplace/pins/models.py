from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.

class Pins(models.Model):
    pin_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    lat = models.DecimalField(max_digits=20, decimal_places=10, default=51.511511)
    lng = models.DecimalField(max_digits=20, decimal_places=10, default=-0.133492)
    notes = models.TextField()
    tags = TaggableManager()
    colour = models.CharField(max_length=100, default='#FF0000')
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    class Meta:
        verbose_name_plural = "Pins"

    def __str__(self):
        return self.name  

    def snippet(self):
        return self.pin[:50] + '...'

class Lists(models.Model):
    name = models.CharField(max_length=100, blank=False)
    thumb = models.CharField(max_length=100, blank=True)
    colour = models.CharField(max_length=100, default='#FF0000')
    date_created = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    pin_id = models.ForeignKey(Pins, on_delete=models.CASCADE, blank=True)
    
    class Meta:
        verbose_name_plural = "Lists"

    def __str__(self):
        return self.name