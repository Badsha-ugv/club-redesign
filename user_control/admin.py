from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User 

# Register your models here.
class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type','student_id','semester','section','phone','image')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets+(
        (None, {'fields': ('user_type','student_id','semester','section','phone','image')}),
    )

    list_display = ('student_id', 'semester', 'username') 
    search_fields = ('student_id','username','phone')
    ordering = ('created',)

    empty_value_display = "-empty-"
    #  fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ( 'user_type', 'phone')}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('user_type', 'phone')}),
    # )

admin.site.register(User,MyUserAdmin)