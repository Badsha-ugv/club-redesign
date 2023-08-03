from django.contrib import admin

from .models import Project, Blog , Category, Subcategory, SliderImage, Event

class EventAdmin(admin.ModelAdmin):
    list_display = ['subtitle','date']
    list_display_links = ['subtitle','date']
    list_filter = ('date',)
    search_fields = ('title','subtitle')

admin.site.register(Event, EventAdmin)

admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Subcategory) 
admin.site.register(SliderImage) 
