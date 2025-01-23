from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(user_registration)
admin.site.register(camera_registration)
admin.site.register(PhotographerImage)
admin.site.register(available_Photographer)
admin.site.register(Booking)
admin.site.register(add_product)
admin.site.register(Feedback)
admin.site.register(Notification)
admin.site.register(PasswordReset)