from django.contrib import admin
from  .models import Profile, Notification

# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Profile)
admin.site.register(Notification, NotificationAdmin)