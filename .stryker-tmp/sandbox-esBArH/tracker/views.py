from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodEntry, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *
from .forms import FoodEntryForm, LoginForm, RegistrationForm, ProfileSetupForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.utils import timezone
from django.http import HttpResponseRedirect



def profile_setup(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})

@login_required
def daily_summary(request):
    today = timezone.now().date()

    if request.method == "POST" and 'name' in request.POST:
        form = FoodEntryForm(request.POST)
        if form.is_valid():
            food_entry = form.save(commit=False)
            food_entry.user = request.user
            food_entry.date = today
            food_entry.save()
            return redirect('/')
    else:
        form = FoodEntryForm()

    entries = FoodEntry.objects.filter(user=request.user, date=today)

    profile = UserProfile.objects.get(user=request.user)

    calories_target = profile.calorie_target
    protein_target = profile.protein_target
    carbs_target = profile.carbs_target
    fat_target = profile.fat_target

    targets = {
        "calories_target": calories_target,
        "protein_target": protein_target,
        "carbs_target": carbs_target,
        "fat_target": fat_target,
    }

    calories_total = sum(e.calories for e in entries)
    protein_total = sum(e.protein for e in entries)
    carbs_total = sum(e.carbs for e in entries)
    fat_total = sum(e.fat for e in entries)

    consumed_total = {
        "calories_total": calories_total,
        "protein_total": protein_total,
        "carbs_total": carbs_total,
        "fat_total": fat_total,
    }

    def progress(total, goal):
        return min(int(float(total) / float(goal) * 100), 100)
    
    foods_by_category = {}
    for category, label in FoodEntry.CATEGORY_CHOICES:
        foods_by_category[category] = entries.filter(category=category)
    
    context = {
        "food_form": FoodEntryForm(),
        "entries": entries,
        "targets": targets,
        "consumed_total": consumed_total,
        "calories_progress": progress(calories_total, calories_target),
        "protein_progress": progress(protein_total, protein_target),
        "carbs_progress": progress(carbs_total, carbs_target),
        "fat_progress": progress(fat_total, fat_target),
        "foods_by_category": foods_by_category,
    }

    return render(request, "tracker/daily_summary.html", context)

@login_required
def edit_food(request):
    if request.method == "POST":
        food_id = request.POST.get("food_id")
        food = get_object_or_404(FoodEntry, id=food_id, user=request.user)

        food.name = request.POST.get("name")
        food.calories = request.POST.get("calories") or 0
        food.protein = request.POST.get("protein") or 0
        food.carbs = request.POST.get("carbs") or 0
        food.fat = request.POST.get("fat") or 0
        food.save()

    return redirect("/")

@login_required
def delete_food(request):
    if request.method == "POST":
        food_id = request.POST.get("food_id")
        food = get_object_or_404(FoodEntry, id=food_id, user=request.user)
        food.delete()

    return redirect("/")

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})


class LoginView(auth_views.LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm

@login_required
def edit_profile(request):
    profile = request.user.userprofile

    if request.method == 'POST':
        form = ProfileSetupForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ProfileSetupForm(instance=profile)

    return render(request, 'tracker/profile_setup.html', {'form': form})
