# cookbook/ingredients/admin.py
from django.contrib import admin
from cookbook.ingredients.models import Category, Ingredient, Box

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Box)