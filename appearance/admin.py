from django.contrib import admin
from appearance.models import Social_Media_Link, Header
# Register your models here.
class Social_Media_LinkAdmin(admin.ModelAdmin):
    list_display=['name','link']
    

admin.site.register(Social_Media_Link, Social_Media_LinkAdmin)

class HeaderAdmin(admin.ModelAdmin):
    list_display=['name','tagline']

admin.site.register(Header,HeaderAdmin)