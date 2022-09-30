from django.contrib import admin
from .models import *
from django.contrib.auth import admin as auth_admin


admin.site.register(Usuario, auth_admin.UserAdmin)


