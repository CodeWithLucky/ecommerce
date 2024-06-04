

from django.contrib import admin
from .models import ContactInfo, Role,CustomUser
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.admin.views.decorators import staff_member_required

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'contact_no', 'address')
    search_fields = ('email', 'contact_no')

# @admin.register(UserInfo)
# class UserInfoAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'middle_name', 'last_name', 'email', 'contact_no')
#     search_fields = ('first_name', 'middle_name', 'last_name', 'email')
#     list_filter = ('roles',)

# @admin.register(AccountInfo)
# class AccountInfoAdmin(admin.ModelAdmin):
#     list_display = ('username', 'user', 'status')
#     search_fields = ('username', 'user__first_name', 'user__last_name')
#     list_filter = ('status',)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'email', 'sex'
    ]
from django.shortcuts import redirect

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'sex', 'delete_button')
    search_fields = ('first_name', 'last_name', 'email')

    def delete_button(self, obj):
        return format_html(
            '<a class="button" href="{}">Delete</a>',
            reverse('admin:customuser_delete', args=[obj.pk])
        )
    delete_button.short_description = 'Delete User'
    delete_button.allow_tags = True

    @staff_member_required
    def delete_view(self, request, pk):
        obj = self.get_object(request, pk)
        if obj:
            obj.delete()
            return redirect(reverse('admin:customuser_changelist'))
        return redirect(reverse('admin:customuser_changelist'))

    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)  # Use custom CSS if needed
        }

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    filter_horizontal = ('users',)


