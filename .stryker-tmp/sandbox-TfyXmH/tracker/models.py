from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class FoodEntry(models.Model):
    CATEGORY_CHOICES = [
        ('uncategorized', 'Uncategorized'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    calories = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    protein = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    carbs = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    fat = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    date = models.DateField(default=timezone.now)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='uncategorized'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category}) ({self.calories} kcal)"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    weight_goal = models.FloatField()

    # Example nutrient goals
    calorie_target = models.FloatField(default=2000)
    protein_target = models.FloatField(default=150)
    carbs_target = models.FloatField(default=250)
    fat_target = models.FloatField(default=70)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def calculate_nutrients(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()