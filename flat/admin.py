from django.contrib import admin
from flat.models import Category, Flat


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

    class Meta:
        models = Category


class FlatAdmin(admin.ModelAdmin):
    list_display = ['house_name', 'house_number', 'area', 'flat_size', 'flat_rent', 'bad', 'bath', 'created_at']
    list_filter = ('house_name', 'created_at')

    class Meta:
        models = Flat

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Flat, FlatAdmin)
