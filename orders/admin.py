from django.contrib import admin
from .models import Order,OrderItem,Review
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display=['user_id','fullname','mobile','pincode','town','state','house','area','landmark','delivered']
    list_filter = ['paid', 'created', 'updated','delivered']
    list_editable = ['delivered']
    inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=['product_name','review']
    
admin.site.register(Review, ReviewAdmin)

