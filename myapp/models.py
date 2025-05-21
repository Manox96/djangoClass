from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    Nom = models.CharField(max_length=200)
    Descreption = models.TextField(blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='photos/', null=True, blank=True)
    favorites = models.ManyToManyField(User, related_name='favorite_photos', blank=True)
    
    def __str__(self):
        return self.Nom
    
    
