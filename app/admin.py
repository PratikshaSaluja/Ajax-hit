from django.contrib import admin
from .models import testuser1
# Register your models here.

@admin.register(testuser1)
class useradmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')
