from django.contrib import admin
from .models import contectus
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'messages')

admin.site.register(contectus, ContactAdmin)