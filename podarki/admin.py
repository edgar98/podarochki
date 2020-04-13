from django.contrib import admin
from podarki.models import *


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3


class ShopEntryAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(ShopUser)
admin.site.register(ShopEntry, ShopEntryAdmin)
# admin.site.register(Photo)
admin.site.register(ShopCartEntry)
admin.site.register(ShopCart)
admin.site.register(UserAddress)
# admin.site.register(Order)

# Register your models here.
