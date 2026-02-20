from django.urls import path
from .views import RecipeListView, RecipeDetailView, search_recipes

app_name = "recipes"

urlpatterns = [
    path("", RecipeListView.as_view(), name="list"),
    path("search/", search_recipes, name="search"),
    path("<int:pk>/", RecipeDetailView.as_view(), name="detail"),
]
