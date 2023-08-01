from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import User , Profile

# Register your models here.
class MyUserAdmin(UserAdmin):
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('user_type','student_id','semester','section','phone','image')}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets+(
    #     (None, {'fields': ('user_type','student_id','semester','section','phone','image')}),
    # )
    fieldsets = ()
    list_display = ('student_id', 'semester', 'username') 
    list_display_links = ('student_id', 'semester', 'username')
    search_fields = ('student_id','username','phone')
    ordering = ('created',)

    list_filter =()
    filter_horizontal = ()

    empty_value_display = "-empty-"
    #  fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ( 'user_type', 'phone')}),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('user_type', 'phone')}),
    # )

admin.site.register(User,MyUserAdmin)

# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('user.username','user.first_name')

class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user_name','full_name','user_type') 
    list_display_links = ('user_name','full_name','user_type') 

    def user_name(self,obj):
        return obj.user.username
    def full_name(self,obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    def user_type(self,obj):
        return obj.user.user_type
    
    
admin.site.register(Profile,ProfileAdmin)

# admin.site.register(Profile)