from django.db import models
from shop.models import Product
from phone_field import PhoneField

# Create your models here.
class Order(models.Model):
    user_id=models.PositiveIntegerField(default=False,null=True,blank=True)
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
    paid = models.BooleanField(default=False)
    charge_id=models.CharField(max_length=200 ,default=False,null=True,blank=True)
    delivered =  models.BooleanField(default=False)

    class Meta:
        ordering = ('-created', )
 
    def __str__(self):
        return 'Order {}'.format(self.id)
 
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE,blank=True,null=True)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=None)
    quantity = models.PositiveIntegerField(default=1)
    user_id = models.PositiveIntegerField(default=False,null=True,blank=True)
 
    def __str__(self):
        return '{}'.format(self.id)
 
    def get_cost(self):
        return self.price * self.quantity


class Review(models.Model):
    user_id = models.IntegerField()
    user_name=models.CharField(max_length=100,default=False,null=True,blank=True)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    review = models.TextField()
 
    def __str__(self):
        return '{}'.format(self.product_id)


