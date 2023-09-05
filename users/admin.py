from django.contrib import admin

from .models import CustomUser


class ModelAdminCustomUser(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'age', 'contact_no', 'email', 'date_joined')
    search_fields = ['first_name','email']
    ordering = ['date_joined']
    list_filter = ['age']

admin.site.register(CustomUser, ModelAdminCustomUser)
