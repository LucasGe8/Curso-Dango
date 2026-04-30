from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone1', 'email')
    search_fields = ('name', 'phone1', 'email')
    ordering = ('name',)

    

admin.site.register(Contact, ContactAdmin)


