from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.api.serializers import RegistrationSerializer



class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = (
		('Permissions', {'fields': ('is_admin',)}),
	)

#
# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     serializer = RegistrationSerializer
#
#     fieldsets = (
#         ('Permissions', {'fields': ('ADMIN',)}),
#     )
#
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


admin.site.register(Account)
