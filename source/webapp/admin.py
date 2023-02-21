from django.contrib import admin
from webapp.models import Category, Product


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    fields = ('id', 'title', 'description')
    readonly_fields = ('id', 'title', 'description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'added_at', 'price', 'image')
    list_filter = ('id', 'category', 'added_at', 'price')
    search_fields = ('id', 'category', 'description', 'added_at', 'price')
    fields = ('id', 'category', 'description', 'added_at', 'price', 'image')
    readonly_fields = ('id', 'category', 'description', 'added_at', 'price', 'image')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
