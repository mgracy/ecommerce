from django.contrib import admin
from .models import Catalog, CatalogCategory, Product, ProductDetail, ProductAttribute
# Register your models here.
admin.site.register(Catalog)
admin.site.register(CatalogCategory)
admin.site.register(Product)
admin.site.register(ProductDetail)
admin.site.register(ProductAttribute)
