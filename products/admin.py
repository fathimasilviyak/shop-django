from django.contrib import admin
from .models import Products, Offer


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')

# Register your models here.
admin.site.register(Products, ProductsAdmin)
admin.site.register(Offer, OfferAdmin)