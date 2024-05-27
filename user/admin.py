

from django.contrib import admin
from .models import ContactInfo, UserInfo, AccountInfo, Role

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'contact_no', 'address')
    search_fields = ('email', 'contact_no')

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name', 'email', 'contact_no')
    search_fields = ('first_name', 'middle_name', 'last_name', 'email')
    list_filter = ('roles',)

@admin.register(AccountInfo)
class AccountInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'user', 'status')
    search_fields = ('username', 'user__first_name', 'user__last_name')
    list_filter = ('status',)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    filter_horizontal = ('users',)


