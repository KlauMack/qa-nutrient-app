from django.shortcuts import render, redirect, get_object_or_404
from .models import FoodEntry, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *
from .forms import FoodEntryForm, LoginForm, RegistrationForm, ProfileSetupForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.utils import timezone
from django.http import HttpResponseRedirect
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result



def x_profile_setup__mutmut_orig(request):
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



def x_profile_setup__mutmut_1(request):
    try:
        profile = None
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



def x_profile_setup__mutmut_2(request):
    try:
        profile = request.user.userprofile
        return redirect(None)
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



def x_profile_setup__mutmut_3(request):
    try:
        profile = request.user.userprofile
        return redirect("XX/XX")
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



def x_profile_setup__mutmut_4(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method != "POST":
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



def x_profile_setup__mutmut_5(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "XXPOSTXX":
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



def x_profile_setup__mutmut_6(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "post":
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



def x_profile_setup__mutmut_7(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = None
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_8(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = ProfileSetupForm(None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_9(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            profile = None
            profile.user = request.user
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_10(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=None)
            profile.user = request.user
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_11(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=True)
            profile.user = request.user
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_12(request):
    try:
        profile = request.user.userprofile
        return redirect("/")
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        form = ProfileSetupForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = None
            profile.calculate_nutrients()
            profile.save()
            return redirect("/")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_13(request):
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
            return redirect(None)
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_14(request):
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
            return redirect("XX/XX")
    else:
        form = ProfileSetupForm()

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_15(request):
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
        form = None

    return render(request, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_16(request):
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

    return render(None, "tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_17(request):
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

    return render(request, None, {"form": form})



def x_profile_setup__mutmut_18(request):
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

    return render(request, "tracker/profile_setup.html", None)



def x_profile_setup__mutmut_19(request):
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

    return render("tracker/profile_setup.html", {"form": form})



def x_profile_setup__mutmut_20(request):
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

    return render(request, {"form": form})



def x_profile_setup__mutmut_21(request):
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

    return render(request, "tracker/profile_setup.html", )



def x_profile_setup__mutmut_22(request):
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

    return render(request, "XXtracker/profile_setup.htmlXX", {"form": form})



def x_profile_setup__mutmut_23(request):
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

    return render(request, "TRACKER/PROFILE_SETUP.HTML", {"form": form})



def x_profile_setup__mutmut_24(request):
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

    return render(request, "tracker/profile_setup.html", {"XXformXX": form})



def x_profile_setup__mutmut_25(request):
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

    return render(request, "tracker/profile_setup.html", {"FORM": form})

x_profile_setup__mutmut_mutants : ClassVar[MutantDict] = {
'x_profile_setup__mutmut_1': x_profile_setup__mutmut_1, 
    'x_profile_setup__mutmut_2': x_profile_setup__mutmut_2, 
    'x_profile_setup__mutmut_3': x_profile_setup__mutmut_3, 
    'x_profile_setup__mutmut_4': x_profile_setup__mutmut_4, 
    'x_profile_setup__mutmut_5': x_profile_setup__mutmut_5, 
    'x_profile_setup__mutmut_6': x_profile_setup__mutmut_6, 
    'x_profile_setup__mutmut_7': x_profile_setup__mutmut_7, 
    'x_profile_setup__mutmut_8': x_profile_setup__mutmut_8, 
    'x_profile_setup__mutmut_9': x_profile_setup__mutmut_9, 
    'x_profile_setup__mutmut_10': x_profile_setup__mutmut_10, 
    'x_profile_setup__mutmut_11': x_profile_setup__mutmut_11, 
    'x_profile_setup__mutmut_12': x_profile_setup__mutmut_12, 
    'x_profile_setup__mutmut_13': x_profile_setup__mutmut_13, 
    'x_profile_setup__mutmut_14': x_profile_setup__mutmut_14, 
    'x_profile_setup__mutmut_15': x_profile_setup__mutmut_15, 
    'x_profile_setup__mutmut_16': x_profile_setup__mutmut_16, 
    'x_profile_setup__mutmut_17': x_profile_setup__mutmut_17, 
    'x_profile_setup__mutmut_18': x_profile_setup__mutmut_18, 
    'x_profile_setup__mutmut_19': x_profile_setup__mutmut_19, 
    'x_profile_setup__mutmut_20': x_profile_setup__mutmut_20, 
    'x_profile_setup__mutmut_21': x_profile_setup__mutmut_21, 
    'x_profile_setup__mutmut_22': x_profile_setup__mutmut_22, 
    'x_profile_setup__mutmut_23': x_profile_setup__mutmut_23, 
    'x_profile_setup__mutmut_24': x_profile_setup__mutmut_24, 
    'x_profile_setup__mutmut_25': x_profile_setup__mutmut_25
}

def profile_setup(*args, **kwargs):
    result = _mutmut_trampoline(x_profile_setup__mutmut_orig, x_profile_setup__mutmut_mutants, args, kwargs)
    return result 

profile_setup.__signature__ = _mutmut_signature(x_profile_setup__mutmut_orig)
x_profile_setup__mutmut_orig.__name__ = 'x_profile_setup'

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

def x_register__mutmut_orig(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_1(request):
    if request.method != "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_2(request):
    if request.method == "XXPOSTXX":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_3(request):
    if request.method == "post":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_4(request):
    if request.method == "POST":
        form = None
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_5(request):
    if request.method == "POST":
        form = RegistrationForm(None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_6(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = None
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_7(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(None, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_8(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, None)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_9(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_10(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, )
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_11(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(None)
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_12(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("XXprofile_setupXX")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_13(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("PROFILE_SETUP")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_14(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = None
    
    return render(request, "tracker/register.html", {"form": form})

def x_register__mutmut_15(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(None, "tracker/register.html", {"form": form})

def x_register__mutmut_16(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, None, {"form": form})

def x_register__mutmut_17(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", None)

def x_register__mutmut_18(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render("tracker/register.html", {"form": form})

def x_register__mutmut_19(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, {"form": form})

def x_register__mutmut_20(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", )

def x_register__mutmut_21(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "XXtracker/register.htmlXX", {"form": form})

def x_register__mutmut_22(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "TRACKER/REGISTER.HTML", {"form": form})

def x_register__mutmut_23(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"XXformXX": form})

def x_register__mutmut_24(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("profile_setup")
    else:
        form = RegistrationForm()
    
    return render(request, "tracker/register.html", {"FORM": form})

x_register__mutmut_mutants : ClassVar[MutantDict] = {
'x_register__mutmut_1': x_register__mutmut_1, 
    'x_register__mutmut_2': x_register__mutmut_2, 
    'x_register__mutmut_3': x_register__mutmut_3, 
    'x_register__mutmut_4': x_register__mutmut_4, 
    'x_register__mutmut_5': x_register__mutmut_5, 
    'x_register__mutmut_6': x_register__mutmut_6, 
    'x_register__mutmut_7': x_register__mutmut_7, 
    'x_register__mutmut_8': x_register__mutmut_8, 
    'x_register__mutmut_9': x_register__mutmut_9, 
    'x_register__mutmut_10': x_register__mutmut_10, 
    'x_register__mutmut_11': x_register__mutmut_11, 
    'x_register__mutmut_12': x_register__mutmut_12, 
    'x_register__mutmut_13': x_register__mutmut_13, 
    'x_register__mutmut_14': x_register__mutmut_14, 
    'x_register__mutmut_15': x_register__mutmut_15, 
    'x_register__mutmut_16': x_register__mutmut_16, 
    'x_register__mutmut_17': x_register__mutmut_17, 
    'x_register__mutmut_18': x_register__mutmut_18, 
    'x_register__mutmut_19': x_register__mutmut_19, 
    'x_register__mutmut_20': x_register__mutmut_20, 
    'x_register__mutmut_21': x_register__mutmut_21, 
    'x_register__mutmut_22': x_register__mutmut_22, 
    'x_register__mutmut_23': x_register__mutmut_23, 
    'x_register__mutmut_24': x_register__mutmut_24
}

def register(*args, **kwargs):
    result = _mutmut_trampoline(x_register__mutmut_orig, x_register__mutmut_mutants, args, kwargs)
    return result 

register.__signature__ = _mutmut_signature(x_register__mutmut_orig)
x_register__mutmut_orig.__name__ = 'x_register'


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
