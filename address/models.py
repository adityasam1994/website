from django.db import models

# Create your models here.
class Address(models.Model):
    user_id=models.CharField(max_length=10)
    fullname=models.CharField(max_length=100)
    mobile=models.CharField(blank=True,max_length=10)
    pincode=models.CharField(blank=True,max_length=30)
    town=models.CharField(blank=True,max_length=50)
    state=models.CharField(blank=True,max_length=50)
    house=models.CharField(blank=True,max_length=100)
    area=models.CharField(blank=True,max_length=50)
    landmark=models.CharField(blank=True,max_length=100)
    created = models.DateTimeField(blank=True,auto_now_add=True)
    updated = models.DateTimeField(blank=True,auto_now=True)

    class Meta:
        ordering = ('-created', )
 
    def __str__(self):
        return 'Address {}'.format(self.id)
 
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())