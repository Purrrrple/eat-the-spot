from django.contrib import admin
from .models import Recipe, Amount, Ingredient


# Register your models here.

admin.site.register(Ingredient)

class AmountInline(admin.TabularInline):
    model = Amount

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        AmountInline,
    ]

admin.site.register(Recipe, RecipeAdmin)
