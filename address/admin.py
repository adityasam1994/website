from django.contrib import admin
from .models import Address
# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display=['fullname','mobile','pincode','town','state','house','area','landmark']
    list_filter = ['created', 'updated']

admin.site.register(Address,AddressAdmin)