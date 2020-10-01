from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from medRelations.models import Clinic

class adminAccount(UserAdmin):
    list_display = ('email', 'username', 'address', 'date_joined', 'last_login', 'is_admin', 'is_staff',)
    search_fields = ('email', 'address',)
    readonly_fields = ('date_joined', 'last_login', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Clinic, adminAccount)
