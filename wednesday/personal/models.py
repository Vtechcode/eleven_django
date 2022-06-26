from django.db import models

# Create your models here.

class Individual(models.Model):
    
    div = models.TextField()
    img = models.ImageField(upload_to='pics')
    par = models.TextField()
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')