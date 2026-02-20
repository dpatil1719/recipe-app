from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import pandas as pd

from .models import Recipe
from .forms import RecipeSearchForm
from .utils import get_chart


# HOME PAGE
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"


# DETAIL PAGE
class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"


# SEARCH PAGE
@login_required
def search_recipes(request):
    form = RecipeSearchForm(request.POST or None)

    results = None
    results_table = None
    chart = None

    if request.method == "POST" and form.is_valid():
        recipe_name = form.cleaned_data.get("recipe_name", "").strip()
        chart_type = form.cleaned_data.get("chart_type")

        # Show-all if search box is empty
        if recipe_name:
            results = Recipe.objects.filter(name__icontains=recipe_name)
        else:
            results = Recipe.objects.all()

        # Build pandas table + chart only if we have results
        if results.exists():
            df = pd.DataFrame(results.values("id", "name", "cooking_time"))
            df = df.rename(columns={"id": "pk"})

            # HTML table
            results_table = df.to_html(index=False)

            # Chart (your utils.get_chart decides how to plot based on chart_type)
            # labels used mainly for pie charts
            if chart_type:
                chart = get_chart(chart_type, df, labels=df["name"].values)

    context = {
        "form": form,
        "results": results,
        "results_table": results_table,
        "chart": chart,
    }
    return render(request, "recipes/search.html", context)
