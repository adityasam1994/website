from django.contrib import admin
from .models import Cart_Record
# Register your models here.

class Cart_RecordAdmin(admin.ModelAdmin):
    list_display=['user_id','product_id','quantity']

admin.site.register(Cart_Record, Cart_RecordAdmin) 