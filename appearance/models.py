from django.db import models

# Create your models here.
class Social_Media_Link(models.Model):
    name=models.CharField(max_length=20)
    link=models.URLField(max_length=300, blank=True)

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name

class Header(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.CharField(max_length=100,blank=True)

    class Meta:
        ordering=("name",)
