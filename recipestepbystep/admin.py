from django.contrib import admin
from .models import Recipe, Timeofday, Location
from .models import RecipeStep, CookingAppliance, CookingMethod
from .models import SubstituteCookingMethod, Ingredient, IngredientSubstitutes


class CookingApplianceAdmin(admin.ModelAdmin):
    list_display = ('cooking_appliance', 'CO2')


class CookingMethodAdmin(admin.ModelAdmin):
    list_display = ('cooking_method', 'CO2', 'nutrition_loss')


class TimeofdayAdmin(admin.ModelAdmin):
    list_display = ('time_of_day', 'emission_multiplier')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'location_emission_factor')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient',
                    'nutritional_value_key', 'nutritional_value',
                    'emissions_key', 'emissions')


class IngredientSubstitutesAdmin(admin.ModelAdmin):
    list_display = ('ingredient',
                    'nutritional_value_key', 'nutritional_value',
                    'emissions_key', 'emissions')


class SubstituteCookingMethodAdmin(admin.ModelAdmin):
    list_display = ('substitute_cooking_method', 'fuel', 'emissions')


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time_minutes', 'cooking_method',
                    'serving_size', 'foodtags', 'colour_code_emissions', 'colour_code_nutrition')


class RecipeStepAdmin(admin.ModelAdmin):
    list_display = ('step_1', 'step_2', 'step_3', 'step_4',
                    'step_5', 'step_6', 'step_7', 'step_8', 'step_9', 'step_10')


admin.site.register(Timeofday, TimeofdayAdmin)
admin.site.register(Location, LocationAdmin, )
admin.site.register(SubstituteCookingMethod, SubstituteCookingMethodAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientSubstitutes, IngredientSubstitutesAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeStep, RecipeStepAdmin)
admin.site.register(CookingAppliance, CookingApplianceAdmin)
admin.site.register(CookingMethod, CookingMethodAdmin)
