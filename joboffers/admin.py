from django.contrib import admin
from .models import User, Offer_job, User_profile, Application, SMS

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        obj.delete()

# Register your models here, except for User
admin.site.register(Offer_job)
admin.site.register(User_profile)
admin.site.register(Application)
admin.site.register(SMS)

# Register the User model with the custom admin class
admin.site.register(User, UserAdmin)