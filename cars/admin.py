from django.contrib import admin
from .models import Car
from django.utils.html import format_html


# Register your models here.
class CarAdmin(admin.ModelAdmin):
#    def thumbnail(self, object):
#         # Return an image thumbnail with specific styling for display in the admin
#         if object.car_photo:
#             return format_html('<img src="{}" width="40" style="border-radius:50px;"/>'.format(object.car_photo.url))
#         else:
#             return format_html('<img src="/photos/2024/10/03/1902536917_abijxTN.jpg" width="40" style="border-radius:50px;"/>')

   #thumbnail.short_description = 'photo'
 list_display = ('id', 'car_title', 'city', 'state', 'color', 'model', 'year', 'price', 'fuel_type', 'is_featured')


admin.site.register(Car, CarAdmin)

