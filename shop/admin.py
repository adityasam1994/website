from django.contrib import admin
from .models import Category, Product, Banner, Highlights,Offer,Front_Page_Section

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','slug','old_price','price','stock','available','created_at','updated_at']
    list_filter=['available','created_at','updated_at']
    list_editable=['price','stock','available','old_price']
    prepopulated_fields={'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

class BannerAdmin(admin.ModelAdmin):
    list_display=['name','image','set_front','on']
    list_editable=['set_front','on']

admin.site.register(Banner,BannerAdmin)

class HighlightsAdmin(admin.ModelAdmin):
    list_display=['product']

admin.site.register(Highlights,HighlightsAdmin)

class OfferAdmin(admin.ModelAdmin):
    list_display=['title','available']
    list_editable=['available']

admin.site.register(Offer,OfferAdmin)

class Front_Page_SectionAdmin(admin.ModelAdmin):
    list_display=['title','category','activate']
    list_editable=['category','activate']

admin.site.register(Front_Page_Section,Front_Page_SectionAdmin)


