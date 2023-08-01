from django.contrib import admin

from .models import Project, Blog , Category, Subcategory, SliderImage

admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Subcategory) 
admin.site.register(SliderImage) 
