from django.shortcuts import render, get_object_or_404
from .models import Recipe, Location, Timeofday


def index(request):
    recipes = Recipe.objects.all()
    locations = Location.objects.all()
    timeofdays = Timeofday.objects.all()
    selected_timeofday = None
    selected_recipe = None
    selected_location = None
    recipe_steps = None
    total_ingredient_emissions = 0

    if request.method == 'POST':
        recipe_id = request.POST.get('selected_recipe')
        location_id = request.POST.get('selected_location')
        timeofday_id = request.POST.get('selected_timeofday')

        if recipe_id:
            selected_recipe = get_object_or_404(Recipe, id=recipe_id)
            request.session['selected_recipe_id'] = recipe_id

        elif 'selected_recipe_id' in request.session:
            selected_recipe = get_object_or_404(
                Recipe, id=request.session['selected_recipe_id'])

        if location_id:
            selected_location = get_object_or_404(Location, id=location_id)
            request.session['selected_location_id'] = location_id
            try:
                selected_location = Location.objects.get(id=location_id)
            except Location.DoesNotExist:
                selected_location = None

        elif 'selected_location_id' in request.session:
            selected_location = get_object_or_404(
                Location, id=request.session['selected_location_id'])

        if timeofday_id:
            selected_timeofday = get_object_or_404(Timeofday, id=timeofday_id)
            request.session['selected_timeofday_id'] = timeofday_id
            try:
                selected_timeofday = Timeofday.objects.get(id=timeofday_id)
            except Timeofday.DoesNotExist:
                selected_timeofday = None

        elif 'selected_timeofday_id' in request.session:
            selected_timeofday = get_object_or_404(
                Timeofday, id=request.session['selected_timeofday_id'])

        if selected_recipe:
            recipe_steps = selected_recipe.steps.first()

        if selected_recipe:
            for ingredient in selected_recipe.ingredients.all():
                try:
                    total_ingredient_emissions += float(ingredient.emissions)
                except (ValueError, TypeError):
                    pass

    return render(request, 'index.html', {
        'recipe': recipes,
        'location': locations,
        'timeofday': timeofdays,
        'selected_recipe': selected_recipe,
        'selected_timeofday': selected_timeofday,
        'selected_location': selected_location,
        'recipe_steps': recipe_steps,
        'total_ingredient_emissions': total_ingredient_emissions,

    },)
