from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tracker.models import FoodEntry, UserProfile
from tracker.forms import FoodEntryForm

class DailySummaryViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")

    def test_redirects_if_not_logged_in(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def test_get_request_renders_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def test_post_invalid_data_does_not_create_entry(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def test_progress_values_in_context(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=10,
            category="breakfast",  # ✅ lowercase value
        )
        response = self.client.get(self.url)
        ctx = response.context
        self.assertEqual(ctx["consumed_total"]["calories_total"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])
