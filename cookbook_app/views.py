from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)
    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight = weight
    recipe_product.save()
    return HttpResponse("Product added to recipe successfully.")


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    for recipe_product in recipe.recipeproduct_set.all():
        product = recipe_product.product
        product.times_cooked += 1
        product.save()
    return HttpResponse("Recipe cooked successfully.")


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recipes = Recipe.objects.exclude(recipeproduct__product=product).filter(recipeproduct__weight__lt=10)
    return render(request, 'recipes_without_product.html', {'recipes': recipes})
