from django.contrib import admin
from excelapp.models import MyModel

# Register your models here.

@admin.register(MyModel)
class exceladmin(admin.ModelAdmin):
    list_display = ['username', 'phone_number', 'email', 'password']