from django.contrib import admin
from .models import *
from django.contrib.auth import admin as auth_admin


# Register your models here.

admin.site.register(Usuario, auth_admin.UserAdmin)