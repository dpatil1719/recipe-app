from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Recipe
from .forms import RecipeSearchForm


class RecipeAuthViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create sample recipes
        Recipe.objects.create(name="Pancakes", description="Yummy", cooking_time=15)
        Recipe.objects.create(name="Vegetable Pasta", description="Healthy", cooking_time=25)
        Recipe.objects.create(name="Vegetable Biryani", description="Spicy", cooking_time=45)

    def test_home_requires_login(self):
        """Home (recipe list) should redirect to login if not logged in."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_search_requires_login(self):
        """Search page should redirect to login if not logged in."""
        response = self.client.get("/search/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_detail_requires_login(self):
        """Detail page should redirect to login if not logged in."""
        r = Recipe.objects.first()
        response = self.client.get(f"/{r.pk}/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login/", response.url)

    def test_home_after_login_shows_recipes(self):
        """After login, home page should show recipe names."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pancakes")
        self.assertContains(response, "Vegetable Pasta")
        self.assertContains(response, "Vegetable Biryani")

    def test_search_partial_name_returns_matches(self):
        """Searching 'veg' should return both Vegetable recipes."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post("/search/", data={"recipe_name": "veg"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Vegetable Pasta")
        self.assertContains(response, "Vegetable Biryani")
        self.assertNotContains(response, "Pancakes")

    def test_search_blank_shows_all(self):
        """Leaving recipe_name blank should show all recipes (Show-all feature)."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post("/search/", data={"recipe_name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pancakes")
        self.assertContains(response, "Vegetable Pasta")
        self.assertContains(response, "Vegetable Biryani")

    def test_search_with_chart_renders_image(self):
        """Selecting a chart type should render a base64 image in HTML."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post("/search/", data={"recipe_name": "pan", "chart_type": "#1"})
        self.assertEqual(response.status_code, 200)
        # If chart exists, template should include this base64 image prefix
        self.assertContains(response, "data:image/png;base64")


class RecipeFormTest(TestCase):
    def test_form_has_fields(self):
        form = RecipeSearchForm()
        self.assertIn("recipe_name", form.fields)
        self.assertIn("chart_type", form.fields)

    def test_form_accepts_partial_text(self):
        form = RecipeSearchForm(data={"recipe_name": "veg", "chart_type": "#2"})
        self.assertTrue(form.is_valid())

    def test_form_allows_blank_search(self):
        form = RecipeSearchForm(data={"recipe_name": "", "chart_type": ""})
        self.assertTrue(form.is_valid())
