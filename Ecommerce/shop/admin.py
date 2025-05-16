from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Category

# admin.site.register(Product)
# admin.site.register(Category)


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "price",)
    search_fields = ("name", "description", "slug", "price",)
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "slug", "id",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}