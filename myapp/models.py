from django.db import models
from django.utils import timezone

# Create your models here.
class Photo(models.Model) :
    Nom = models.CharField(max_length=200);
    Descreption = models.TextField(blank=True)
    upload_date = models.DateTimeField(default=timezone.now)
    is_pulic = models.BooleanField(default=True)
    
    
