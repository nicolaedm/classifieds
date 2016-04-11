from django.contrib import admin

# Register your models here.

from .models import Category, Add

admin.site.register(Category)
admin.site.register(Add)