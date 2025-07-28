from django.db import models


class CookingAppliance(models.Model):
    cooking_appliance = models.CharField(max_length=100)
    CO2 = models.FloatField(default=0.0)


class CookingMethod(models.Model):
    cooking_method = models.CharField(max_length=100)
    CO2 = models.FloatField(default=0.0)
    nutrition_loss = models.FloatField(default=0.0)


def get_nutrition_badge_class(value):
    value = value.lower()
    if "high" in value:
        return "badge bg-success"
    elif "medium" in value:
        return "badge bg-warning text-dark"
    elif "low" in value:
        return "badge bg-danger"
    return "badge bg-secondary"


def get_emissions_badge_class(value):
    value = value.lower()
    if "low" in value:
        return "badge bg-success"
    elif "medium" in value:
        return "badge bg-warning text-dark"
    elif "high" in value:
        return "badge bg-danger"
    return "badge bg-secondary"


class IngredientSubstitutes(models.Model):
    ingredient = models.CharField(max_length=150)
    nutritional_value_key = models.CharField(max_length=30, default="none")
    nutritional_value = models.FloatField(default=0.0)
    emissions_key = models.CharField(max_length=30, default="none")
    emissions = models.FloatField(default=0.0)

    def __str__(self):
        return self.ingredient

    def nutrition_badge_class(self):
        return get_nutrition_badge_class(self.nutritional_value_key)

    def emissions_badge_class(self):
        return get_emissions_badge_class(self.emissions_key)


class Ingredient(models.Model):
    ingredient = models.CharField(max_length=150, unique=True)
    nutritional_value_key = models.CharField(max_length=30, default="none")
    nutritional_value = models.FloatField(default=0.0)
    emissions_key = models.CharField(max_length=30, default="none")
    emissions = models.FloatField(default=0.0)
    substitutes = models.ManyToManyField(
        IngredientSubstitutes, blank=True, symmetrical=False, related_name='substituted_by')

    def __str__(self):
        return self.ingredient

    def nutrition_badge_class(self):
        return get_nutrition_badge_class(self.nutritional_value_key)

    def emissions_badge_class(self):
        return get_emissions_badge_class(self.emissions_key)


class Recipe(models.Model):
    name = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')
    cooking_time_minutes = models.FloatField(default=0.0)
    cooking_method = models.CharField(max_length=100, default='---')
    serving_size = models.IntegerField()
    image_url = models.CharField(max_length=2083, default="---")
    foodtags = models.CharField(max_length=1000, default="---")
    colour_code_emissions = models.CharField(max_length=10, default='---')
    colour_code_nutrition = models.CharField(max_length=10, default='---')

    def __str__(self):
        return self.name


class RecipeStep(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, null=True, blank=True, related_name='steps')
    step_1 = models.CharField(max_length=5000)
    step_2 = models.CharField(max_length=5000)
    step_3 = models.CharField(max_length=5000, default="null")
    step_4 = models.CharField(max_length=5000, default="null")
    step_5 = models.CharField(max_length=5000, default="null")
    step_6 = models.CharField(max_length=5000, default="null")
    step_7 = models.CharField(max_length=5000, default="null")
    step_8 = models.CharField(max_length=5000, default="null")
    step_9 = models.CharField(max_length=5000, default="null")
    step_10 = models.CharField(max_length=5000, default="null")


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    location_emission_factor = models.FloatField(default=0.0)


class Timeofday(models.Model):
    time_of_day = models.CharField(max_length=100)
    emission_multiplier = models.FloatField(default=0.0)


class SubstituteCookingMethod(models.Model):
    substitute_cooking_method = models.CharField(
        max_length=150, default="none")
    fuel = models.CharField(max_length=100, default="none")
    emissions = models.CharField(max_length=100, default="none")
