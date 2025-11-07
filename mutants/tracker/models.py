from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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

    def xǁUserProfileǁcalculate_nutrients__mutmut_orig(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_1(self):
        self.calories_target = None  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_2(self):
        self.calories_target = (self.weight_goal / 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_3(self):
        self.calories_target = (self.weight_goal * 31)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_4(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = None    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_5(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal / 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_6(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 2.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_7(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = None        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_8(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal / 3        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_9(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 4        # grams
        self.fat_target = self.weight_goal * 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_10(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = None          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_11(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal / 1          # grams
        self.save()

    def xǁUserProfileǁcalculate_nutrients__mutmut_12(self):
        self.calories_target = (self.weight_goal * 30)  # kcal
        self.protein_target = self.weight_goal * 1.5    # grams
        self.carbs_target = self.weight_goal * 3        # grams
        self.fat_target = self.weight_goal * 2          # grams
        self.save()
    
    xǁUserProfileǁcalculate_nutrients__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁUserProfileǁcalculate_nutrients__mutmut_1': xǁUserProfileǁcalculate_nutrients__mutmut_1, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_2': xǁUserProfileǁcalculate_nutrients__mutmut_2, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_3': xǁUserProfileǁcalculate_nutrients__mutmut_3, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_4': xǁUserProfileǁcalculate_nutrients__mutmut_4, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_5': xǁUserProfileǁcalculate_nutrients__mutmut_5, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_6': xǁUserProfileǁcalculate_nutrients__mutmut_6, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_7': xǁUserProfileǁcalculate_nutrients__mutmut_7, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_8': xǁUserProfileǁcalculate_nutrients__mutmut_8, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_9': xǁUserProfileǁcalculate_nutrients__mutmut_9, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_10': xǁUserProfileǁcalculate_nutrients__mutmut_10, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_11': xǁUserProfileǁcalculate_nutrients__mutmut_11, 
        'xǁUserProfileǁcalculate_nutrients__mutmut_12': xǁUserProfileǁcalculate_nutrients__mutmut_12
    }
    
    def calculate_nutrients(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁUserProfileǁcalculate_nutrients__mutmut_orig"), object.__getattribute__(self, "xǁUserProfileǁcalculate_nutrients__mutmut_mutants"), args, kwargs, self)
        return result 
    
    calculate_nutrients.__signature__ = _mutmut_signature(xǁUserProfileǁcalculate_nutrients__mutmut_orig)
    xǁUserProfileǁcalculate_nutrients__mutmut_orig.__name__ = 'xǁUserProfileǁcalculate_nutrients'