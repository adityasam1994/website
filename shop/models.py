from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

# Create your models here.

class Offer(models.Model):
    title=models.CharField(max_length=100)
    available=models.BooleanField(default=True)

    class Meta:
        ordering=('title',)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('shop:offer', args=[self.id])    

class Banner(models.Model):
    name=models.CharField(max_length=50,db_index=True,default="banner")
    image=models.ImageField(upload_to='banners/%Y/%m/%d',blank=True)
    set_front=models.BooleanField(default=False)
    on = models.BooleanField(default=True)

    class Meta:
        ordering=('image',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:banner')


class Category(models.Model):
    name=models.CharField(max_length=150,db_index=True)
    slug=models.SlugField(max_length=150, unique=True, db_index=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])



class Product(models.Model):
    Category=models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100, db_index=True)
    description=models.TextField(blank=True)
    specifications=models.TextField(blank=True,default=None,null=True)
    old_price=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0)
    price=models.PositiveIntegerField(default=None)
    offer=models.ForeignKey(Offer, on_delete=models.CASCADE,blank=True,default=None,null=True)
    available=models.BooleanField(default=True)
    stock=models.PositiveIntegerField()
    one_person_order_limit=models.PositiveIntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,self.slug])

class Highlights(models.Model):
    product=models.ForeignKey(Product,default=None,blank=True,null=True,on_delete=models.CASCADE)
    highlight1=models.TextField(default=None,null=True,blank=True)
    highlight1_image=models.ImageField(upload_to='highlights/%Y/%m/%d',default=None,null=True,blank=True)
    highlight2=models.TextField(default=None,null=True,blank=True)
    highlight2_image=models.ImageField(upload_to='highlights/%Y/%m/%d',default=None,null=True,blank=True)
    highlight3=models.TextField(default=None,null=True,blank=True)
    highlight3_image=models.ImageField(upload_to='highlights/%Y/%m/%d',default=None,null=True,blank=True)
    highlight4=models.TextField(default=None,null=True,blank=True)
    highlight4_image=models.ImageField(upload_to='highlights/%Y/%m/%d',default=None,null=True,blank=True)
    highlight5=models.TextField(default=None,null=True,blank=True)
    highlight5_image=models.ImageField(upload_to='highlights/%Y/%m/%d',default=None,null=True,blank=True)
    highlight6=models.TextField(default=None,null=True,blank=True)
    highlight6_image=models.ImageField(upload_to='highlights/%Y/%m/%d',default=None,null=True,blank=True)

    class Meta:
        ordering=('product',)
        verbose_name='highlight'
        verbose_name_plural='highlights'

    
class Front_Page_Section(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    activate=models.BooleanField(default=True)

    class Meta:
        verbose_name='Front_Page_Section'
        verbose_name_plural='Front_Page_Sections'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:section', args=[self.id])
        
    


