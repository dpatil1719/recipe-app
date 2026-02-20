from django import forms

CHART_CHOICES = (
    ("", "No chart"),   # allows blank selection
    ("#1", "Bar chart"),
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(
        max_length=120,
        required=False,
        label="Recipe name",
        widget=forms.TextInput(attrs={"placeholder": "e.g. veg, pan, soup"})
    )

    chart_type = forms.ChoiceField(
        choices=CHART_CHOICES,
        required=False,
        label="Chart type"
    )
