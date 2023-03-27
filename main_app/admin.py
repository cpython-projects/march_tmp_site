from django.contrib import admin


from .models import DishCategory, Dish, Gallery, Reservation


admin.site.register(Gallery)
admin.site.register(Reservation)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'position', 'is_visible', 'is_special', 'is_signature', 'price',
                    'discount', 'ingredients', 'photo']
    list_filter = ['is_visible', 'is_special', 'is_signature', 'category']
    list_editable = ['category', 'position', 'is_visible', 'is_special', 'is_signature', 'price', 'discount',
                     'ingredients', 'photo']


# @admin.register(DishCategory)
# class DishCategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'position', 'is_visible']
#     list_filter = ['is_visible']
#     list_editable = ['position', 'is_visible']


class DishInline(admin.TabularInline):
    model = Dish

@admin.register(DishCategory)
class CategoriesWithDishesAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_filter = ['is_visible']
    list_editable = ['position', 'is_visible']
    inlines = [DishInline]