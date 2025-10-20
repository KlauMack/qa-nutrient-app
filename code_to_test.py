from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from .models import FoodEntry, UserProfile
from .forms import FoodEntryForm
# --- New helper/service class ---
class NutritionSummaryService:
    """Atsakinga už maistinių medžiagų sumų ir tikslų skaičiavimą."""
    def __init__(self, user, date):
        self.user = user
        self.date = date
    def get_entries(self):
        return FoodEntry.objects.filter(user=self.user, date=self.date)
    def calculate_totals(self, entries):
        fields = ["calories", "protein", "carbs", "fat"]
        return {f"{field}_total": sum(getattr(e, field) for e in entries) for field in fields}
    def get_targets(self):
        profile, _ = UserProfile.objects.get_or_create(user=self.user)
        return {
            "calories_target": profile.calorie_target,
            "protein_target": profile.protein_target,
            "carbs_target": profile.carbs_target,
            "fat_target": profile.fat_target,
        }
# --- Refactored view ---
def daily_summary(request):
    today = timezone.now().date()
    service = NutritionSummaryService(request.user, today)
    if request.method == "POST" and "name" in request.POST:
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.date = today
            food_entry.save()
            return redirect(reverse("home"))
    else:
        form = FoodEntryForm()
    entries = service.get_entries()
    targets = service.get_targets()
    consumed_total = service.calculate_totals(entries)
    context = {
        "form": form,
        "entries": entries,
        "targets": targets,
        "consumed_total": consumed_total,
        "date": today,
    }
    return render(request, "daily_summary.html", context)