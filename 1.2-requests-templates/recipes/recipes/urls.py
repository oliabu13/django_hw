from django.urls import path
from calculator.views import start, recipe_list, recipe

urlpatterns = [
    path('', start, name='start'),
    path('recipe_list/', recipe_list, name='recipe_list'),
    path('recipe/<str:recipe_name>/', recipe, name='recipe')

]
