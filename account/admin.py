from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Student,Staff
# from staff.models import Student


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_staffs','is_student',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff','is_staffs','is_student')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)







class StaffAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'address', 'dob', 'designation', 'qualification')

class StudentAdmin(admin.ModelAdmin):
    list_display = ( 'address', 'dob', 'mobile',   'qualification', 'college', 'course')



admin.site.register(Staff,StaffAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(get_user_model(), CustomUserAdmin)
