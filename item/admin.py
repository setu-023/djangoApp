from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from . models import Item

# class UserAdmin(BaseUserManager):
# import pdb; pdb.set_trace()
#     fieldsets = (
#
#         ('Permissions', {'fields': ('is_check',)}),
#     )
#

# ow register the new UserAdmin...
admin.site.register(Item,)
