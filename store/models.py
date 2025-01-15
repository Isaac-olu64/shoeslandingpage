from django.db import models

# Create your models here.

GROUP_CHOICES = [
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
    ('CHILDREN','CHILDREN')

]

SIZE_CHOICES = [
    ('XSM','XSM'),
    ('SM','SM'),
    ('M','M'),
    ('L','L'),
    ('XL','XL'),
]

class Category(models.Model):
    image = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    size = models.CharField(max_length=255, choices=SIZE_CHOICES, blank=True, null=True,)
    price = models.IntegerField()
    group = models.CharField(max_length=255, choices=GROUP_CHOICES, blank=True, null=True,)
    

    def __str__(self):
        return self.image

