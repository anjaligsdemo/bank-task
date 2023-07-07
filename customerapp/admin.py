from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Material, UserMaterials, Branch, District
from django.contrib import admin

admin.site.register(CustomUser)
admin.site.register(Material)
admin.site.register(UserMaterials)
admin.site.register(Branch)
admin.site.register(District)

