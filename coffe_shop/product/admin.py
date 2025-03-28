from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'available', 'photo')  # Campos a mostrar en la lista
    search_fields = ('name', 'description')  # Campos que se pueden buscar
admin.site.register(Product, ProductAdmin)  # Registra el modelo Product en el admin de Django