from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from tracker.models import FoodEntry, UserProfile
from tracker.forms import FoodEntryForm
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

class DailySummaryViewTests(TestCase):
    def xǁDailySummaryViewTestsǁsetUp__mutmut_orig(self):
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_1(self):
        self.user = None
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_2(self):
        self.user = User.objects.create_user(username=None, password="pass1234")
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_3(self):
        self.user = User.objects.create_user(username="testuser", password=None)
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_4(self):
        self.user = User.objects.create_user(password="pass1234")
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_5(self):
        self.user = User.objects.create_user(username="testuser", )
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_6(self):
        self.user = User.objects.create_user(username="XXtestuserXX", password="pass1234")
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_7(self):
        self.user = User.objects.create_user(username="TESTUSER", password="pass1234")
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_8(self):
        self.user = User.objects.create_user(username="testuser", password="XXpass1234XX")
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_9(self):
        self.user = User.objects.create_user(username="testuser", password="PASS1234")
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_10(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = None
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_11(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=None,
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_12(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=None,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_13(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=None,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_14(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=None,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_15(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=None,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_16(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=None,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_17(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=None,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_18(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=None,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_19(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
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
    def xǁDailySummaryViewTestsǁsetUp__mutmut_20(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_21(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_22(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_23(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_24(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_25(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_26(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_27(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=181,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_28(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=76,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_29(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=71,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_30(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2001,
            protein_target=150,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_31(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=151,
            carbs_target=250,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_32(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=251,
            fat_target=70,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_33(self):
        self.user = User.objects.create_user(username="testuser", password="pass1234")
        self.profile = UserProfile.objects.create(
            user=self.user,
            height=180,           # ✅ required
            weight=75,            # ✅ required
            weight_goal=70,       # ✅ add this
            calorie_target=2000,
            protein_target=150,
            carbs_target=250,
            fat_target=71,
        )
        self.client.login(username="testuser", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_34(self):
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
        self.client.login(username=None, password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_35(self):
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
        self.client.login(username="testuser", password=None)
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_36(self):
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
        self.client.login(password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_37(self):
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
        self.client.login(username="testuser", )
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_38(self):
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
        self.client.login(username="XXtestuserXX", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_39(self):
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
        self.client.login(username="TESTUSER", password="pass1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_40(self):
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
        self.client.login(username="testuser", password="XXpass1234XX")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_41(self):
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
        self.client.login(username="testuser", password="PASS1234")
        self.url = reverse("home")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_42(self):
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
        self.url = None
    def xǁDailySummaryViewTestsǁsetUp__mutmut_43(self):
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
        self.url = reverse(None)
    def xǁDailySummaryViewTestsǁsetUp__mutmut_44(self):
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
        self.url = reverse("XXhomeXX")
    def xǁDailySummaryViewTestsǁsetUp__mutmut_45(self):
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
        self.url = reverse("HOME")
    
    xǁDailySummaryViewTestsǁsetUp__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDailySummaryViewTestsǁsetUp__mutmut_1': xǁDailySummaryViewTestsǁsetUp__mutmut_1, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_2': xǁDailySummaryViewTestsǁsetUp__mutmut_2, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_3': xǁDailySummaryViewTestsǁsetUp__mutmut_3, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_4': xǁDailySummaryViewTestsǁsetUp__mutmut_4, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_5': xǁDailySummaryViewTestsǁsetUp__mutmut_5, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_6': xǁDailySummaryViewTestsǁsetUp__mutmut_6, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_7': xǁDailySummaryViewTestsǁsetUp__mutmut_7, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_8': xǁDailySummaryViewTestsǁsetUp__mutmut_8, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_9': xǁDailySummaryViewTestsǁsetUp__mutmut_9, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_10': xǁDailySummaryViewTestsǁsetUp__mutmut_10, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_11': xǁDailySummaryViewTestsǁsetUp__mutmut_11, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_12': xǁDailySummaryViewTestsǁsetUp__mutmut_12, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_13': xǁDailySummaryViewTestsǁsetUp__mutmut_13, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_14': xǁDailySummaryViewTestsǁsetUp__mutmut_14, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_15': xǁDailySummaryViewTestsǁsetUp__mutmut_15, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_16': xǁDailySummaryViewTestsǁsetUp__mutmut_16, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_17': xǁDailySummaryViewTestsǁsetUp__mutmut_17, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_18': xǁDailySummaryViewTestsǁsetUp__mutmut_18, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_19': xǁDailySummaryViewTestsǁsetUp__mutmut_19, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_20': xǁDailySummaryViewTestsǁsetUp__mutmut_20, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_21': xǁDailySummaryViewTestsǁsetUp__mutmut_21, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_22': xǁDailySummaryViewTestsǁsetUp__mutmut_22, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_23': xǁDailySummaryViewTestsǁsetUp__mutmut_23, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_24': xǁDailySummaryViewTestsǁsetUp__mutmut_24, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_25': xǁDailySummaryViewTestsǁsetUp__mutmut_25, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_26': xǁDailySummaryViewTestsǁsetUp__mutmut_26, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_27': xǁDailySummaryViewTestsǁsetUp__mutmut_27, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_28': xǁDailySummaryViewTestsǁsetUp__mutmut_28, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_29': xǁDailySummaryViewTestsǁsetUp__mutmut_29, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_30': xǁDailySummaryViewTestsǁsetUp__mutmut_30, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_31': xǁDailySummaryViewTestsǁsetUp__mutmut_31, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_32': xǁDailySummaryViewTestsǁsetUp__mutmut_32, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_33': xǁDailySummaryViewTestsǁsetUp__mutmut_33, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_34': xǁDailySummaryViewTestsǁsetUp__mutmut_34, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_35': xǁDailySummaryViewTestsǁsetUp__mutmut_35, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_36': xǁDailySummaryViewTestsǁsetUp__mutmut_36, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_37': xǁDailySummaryViewTestsǁsetUp__mutmut_37, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_38': xǁDailySummaryViewTestsǁsetUp__mutmut_38, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_39': xǁDailySummaryViewTestsǁsetUp__mutmut_39, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_40': xǁDailySummaryViewTestsǁsetUp__mutmut_40, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_41': xǁDailySummaryViewTestsǁsetUp__mutmut_41, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_42': xǁDailySummaryViewTestsǁsetUp__mutmut_42, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_43': xǁDailySummaryViewTestsǁsetUp__mutmut_43, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_44': xǁDailySummaryViewTestsǁsetUp__mutmut_44, 
        'xǁDailySummaryViewTestsǁsetUp__mutmut_45': xǁDailySummaryViewTestsǁsetUp__mutmut_45
    }
    
    def setUp(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDailySummaryViewTestsǁsetUp__mutmut_orig"), object.__getattribute__(self, "xǁDailySummaryViewTestsǁsetUp__mutmut_mutants"), args, kwargs, self)
        return result 
    
    setUp.__signature__ = _mutmut_signature(xǁDailySummaryViewTestsǁsetUp__mutmut_orig)
    xǁDailySummaryViewTestsǁsetUp__mutmut_orig.__name__ = 'xǁDailySummaryViewTestsǁsetUp'

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_orig(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_1(self):
        self.client.logout()
        response = None
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_2(self):
        self.client.logout()
        response = self.client.get(None)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_3(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(None, 302)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_4(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, None)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_5(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(302)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_6(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, )
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_7(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 303)
        self.assertIn("/login", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_8(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(None, response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_9(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", None)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_10(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn(response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_11(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", )

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_12(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("XX/loginXX", response.url)

    def xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_13(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("/LOGIN", response.url)
    
    xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_1': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_1, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_2': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_2, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_3': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_3, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_4': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_4, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_5': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_5, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_6': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_6, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_7': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_7, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_8': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_8, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_9': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_9, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_10': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_10, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_11': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_11, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_12': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_12, 
        'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_13': xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_13
    }
    
    def test_redirects_if_not_logged_in(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_orig"), object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_mutants"), args, kwargs, self)
        return result 
    
    test_redirects_if_not_logged_in.__signature__ = _mutmut_signature(xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_orig)
    xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in__mutmut_orig.__name__ = 'xǁDailySummaryViewTestsǁtest_redirects_if_not_logged_in'

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_orig(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_1(self):
        response = None
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_2(self):
        response = self.client.get(None)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_3(self):
        response = self.client.get(self.url)
        self.assertEqual(None, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_4(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, None)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_5(self):
        response = self.client.get(self.url)
        self.assertEqual(200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_6(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, )
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_7(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_8(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(None, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_9(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, None)
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_10(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_11(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, )
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_12(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "XXtracker/daily_summary.htmlXX")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_13(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "TRACKER/DAILY_SUMMARY.HTML")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_14(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn(None, response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_15(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", None)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_16(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn(response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_17(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", )
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_18(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("XXfood_formXX", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_19(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("FOOD_FORM", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_20(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(None, FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_21(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], None)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_22(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_23(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], )
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_24(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["XXfood_formXX"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_25(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["FOOD_FORM"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_26(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(None, 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_27(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], None)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_28(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_29(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], )

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_30(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["XXtargetsXX"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_31(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["TARGETS"]["calories_target"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_32(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["XXcalories_targetXX"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_33(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["CALORIES_TARGET"], 2000)

    def xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_34(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertIn("food_form", response.context)
        self.assertIsInstance(response.context["food_form"], FoodEntryForm)
        self.assertEqual(response.context["targets"]["calories_target"], 2001)
    
    xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_1': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_1, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_2': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_2, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_3': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_3, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_4': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_4, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_5': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_5, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_6': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_6, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_7': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_7, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_8': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_8, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_9': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_9, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_10': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_10, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_11': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_11, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_12': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_12, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_13': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_13, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_14': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_14, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_15': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_15, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_16': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_16, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_17': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_17, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_18': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_18, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_19': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_19, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_20': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_20, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_21': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_21, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_22': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_22, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_23': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_23, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_24': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_24, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_25': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_25, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_26': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_26, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_27': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_27, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_28': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_28, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_29': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_29, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_30': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_30, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_31': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_31, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_32': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_32, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_33': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_33, 
        'xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_34': xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_34
    }
    
    def test_get_request_renders_template(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_orig"), object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_mutants"), args, kwargs, self)
        return result 
    
    test_get_request_renders_template.__signature__ = _mutmut_signature(xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_orig)
    xǁDailySummaryViewTestsǁtest_get_request_renders_template__mutmut_orig.__name__ = 'xǁDailySummaryViewTestsǁtest_get_request_renders_template'

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_orig(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_1(self):
        data = None
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_2(self):
        data = {"XXnameXX": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_3(self):
        data = {"NAME": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_4(self):
        data = {"name": "XXXX", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_5(self):
        data = {"name": "", "XXcaloriesXX": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_6(self):
        data = {"name": "", "CALORIES": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_7(self):
        data = {"name": "", "calories": "XXXX", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_8(self):
        data = {"name": "", "calories": "", "XXproteinXX": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_9(self):
        data = {"name": "", "calories": "", "PROTEIN": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_10(self):
        data = {"name": "", "calories": "", "protein": "XXXX"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_11(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = None
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_12(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(None, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_13(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, None)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_14(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_15(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_16(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(None, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_17(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, None)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_18(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_19(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, )
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_20(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_21(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(None, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_22(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, None)
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_23(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_24(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, )
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_25(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "XXtracker/daily_summary.htmlXX")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_26(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "TRACKER/DAILY_SUMMARY.HTML")
        self.assertEqual(FoodEntry.objects.count(), 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_27(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(None, 0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_28(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), None)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_29(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(0)

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_30(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), )

    def xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_31(self):
        data = {"name": "", "calories": "", "protein": ""}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tracker/daily_summary.html")
        self.assertEqual(FoodEntry.objects.count(), 1)
    
    xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_1': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_1, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_2': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_2, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_3': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_3, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_4': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_4, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_5': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_5, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_6': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_6, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_7': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_7, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_8': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_8, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_9': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_9, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_10': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_10, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_11': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_11, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_12': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_12, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_13': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_13, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_14': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_14, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_15': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_15, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_16': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_16, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_17': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_17, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_18': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_18, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_19': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_19, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_20': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_20, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_21': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_21, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_22': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_22, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_23': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_23, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_24': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_24, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_25': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_25, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_26': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_26, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_27': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_27, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_28': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_28, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_29': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_29, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_30': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_30, 
        'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_31': xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_31
    }
    
    def test_post_invalid_data_does_not_create_entry(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_orig"), object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_mutants"), args, kwargs, self)
        return result 
    
    test_post_invalid_data_does_not_create_entry.__signature__ = _mutmut_signature(xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_orig)
    xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry__mutmut_orig.__name__ = 'xǁDailySummaryViewTestsǁtest_post_invalid_data_does_not_create_entry'

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_orig(self):
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_1(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_2(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_3(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_4(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_5(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_6(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_7(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=None,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_8(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=10,
            category=None,  # ✅ lowercase value
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_9(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_10(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_11(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_12(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_13(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_14(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_15(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_16(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=10,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_17(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="XXOatsXX",
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_18(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="oats",
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_19(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="OATS",
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_20(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=501,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_21(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=21,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_22(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=91,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_23(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=11,
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_24(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=10,
            category="XXbreakfastXX",  # ✅ lowercase value
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_25(self):
        # Create existing entries to test totals and progress
        FoodEntry.objects.create(
            user=self.user,
            date=timezone.now().date(),
            name="Oats",
            calories=500,
            protein=20,
            carbs=90,
            fat=10,
            category="BREAKFAST",  # ✅ lowercase value
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

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_26(self):
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
        response = None
        ctx = response.context
        self.assertEqual(ctx["consumed_total"]["calories_total"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_27(self):
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
        response = self.client.get(None)
        ctx = response.context
        self.assertEqual(ctx["consumed_total"]["calories_total"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_28(self):
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
        ctx = None
        self.assertEqual(ctx["consumed_total"]["calories_total"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_29(self):
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
        self.assertEqual(None, 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_30(self):
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
        self.assertEqual(ctx["consumed_total"]["calories_total"], None)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_31(self):
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
        self.assertEqual(500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_32(self):
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
        self.assertEqual(ctx["consumed_total"]["calories_total"], )
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_33(self):
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
        self.assertEqual(ctx["XXconsumed_totalXX"]["calories_total"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_34(self):
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
        self.assertEqual(ctx["CONSUMED_TOTAL"]["calories_total"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_35(self):
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
        self.assertEqual(ctx["consumed_total"]["XXcalories_totalXX"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_36(self):
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
        self.assertEqual(ctx["consumed_total"]["CALORIES_TOTAL"], 500)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_37(self):
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
        self.assertEqual(ctx["consumed_total"]["calories_total"], 501)
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_38(self):
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
        self.assertEqual(None, int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_39(self):
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
        self.assertEqual(ctx["calories_progress"], None)  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_40(self):
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
        self.assertEqual(int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_41(self):
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
        self.assertEqual(ctx["calories_progress"], )  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_42(self):
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
        self.assertEqual(ctx["XXcalories_progressXX"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_43(self):
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
        self.assertEqual(ctx["CALORIES_PROGRESS"], int(500 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_44(self):
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
        self.assertEqual(ctx["calories_progress"], int(None))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_45(self):
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
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 / 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_46(self):
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
        self.assertEqual(ctx["calories_progress"], int(500 * 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_47(self):
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
        self.assertEqual(ctx["calories_progress"], int(501 / 2000 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_48(self):
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
        self.assertEqual(ctx["calories_progress"], int(500 / 2001 * 100))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_49(self):
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
        self.assertEqual(ctx["calories_progress"], int(500 / 2000 * 101))  # 25%
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_50(self):
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
        self.assertEqual(None, int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_51(self):
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
        self.assertEqual(ctx["protein_progress"], None)
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_52(self):
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
        self.assertEqual(int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_53(self):
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
        self.assertEqual(ctx["protein_progress"], )
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_54(self):
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
        self.assertEqual(ctx["XXprotein_progressXX"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_55(self):
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
        self.assertEqual(ctx["PROTEIN_PROGRESS"], int(20 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_56(self):
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
        self.assertEqual(ctx["protein_progress"], int(None))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_57(self):
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
        self.assertEqual(ctx["protein_progress"], int(20 / 150 / 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_58(self):
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
        self.assertEqual(ctx["protein_progress"], int(20 * 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_59(self):
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
        self.assertEqual(ctx["protein_progress"], int(21 / 150 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_60(self):
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
        self.assertEqual(ctx["protein_progress"], int(20 / 151 * 100))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_61(self):
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
        self.assertEqual(ctx["protein_progress"], int(20 / 150 * 101))
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_62(self):
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
        self.assertEqual(None, int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_63(self):
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
        self.assertEqual(ctx["carbs_progress"], None)
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_64(self):
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
        self.assertEqual(int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_65(self):
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
        self.assertEqual(ctx["carbs_progress"], )
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_66(self):
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
        self.assertEqual(ctx["XXcarbs_progressXX"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_67(self):
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
        self.assertEqual(ctx["CARBS_PROGRESS"], int(90 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_68(self):
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
        self.assertEqual(ctx["carbs_progress"], int(None))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_69(self):
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
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 / 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_70(self):
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
        self.assertEqual(ctx["carbs_progress"], int(90 * 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_71(self):
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
        self.assertEqual(ctx["carbs_progress"], int(91 / 250 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_72(self):
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
        self.assertEqual(ctx["carbs_progress"], int(90 / 251 * 100))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_73(self):
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
        self.assertEqual(ctx["carbs_progress"], int(90 / 250 * 101))
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_74(self):
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
        self.assertEqual(None, int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_75(self):
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
        self.assertEqual(ctx["fat_progress"], None)
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_76(self):
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
        self.assertEqual(int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_77(self):
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
        self.assertEqual(ctx["fat_progress"], )
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_78(self):
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
        self.assertEqual(ctx["XXfat_progressXX"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_79(self):
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
        self.assertEqual(ctx["FAT_PROGRESS"], int(10 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_80(self):
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
        self.assertEqual(ctx["fat_progress"], int(None))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_81(self):
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
        self.assertEqual(ctx["fat_progress"], int(10 / 70 / 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_82(self):
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
        self.assertEqual(ctx["fat_progress"], int(10 * 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_83(self):
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
        self.assertEqual(ctx["fat_progress"], int(11 / 70 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_84(self):
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
        self.assertEqual(ctx["fat_progress"], int(10 / 71 * 100))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_85(self):
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
        self.assertEqual(ctx["fat_progress"], int(10 / 70 * 101))
        self.assertIn("foods_by_category", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_86(self):
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
        self.assertIn(None, ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_87(self):
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
        self.assertIn("foods_by_category", None)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_88(self):
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
        self.assertIn(ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_89(self):
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
        self.assertIn("foods_by_category", )
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_90(self):
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
        self.assertIn("XXfoods_by_categoryXX", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_91(self):
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
        self.assertIn("FOODS_BY_CATEGORY", ctx)
        self.assertIn("breakfast", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_92(self):
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
        self.assertIn(None, ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_93(self):
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
        self.assertIn("breakfast", None)

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_94(self):
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
        self.assertIn(ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_95(self):
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
        self.assertIn("breakfast", )

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_96(self):
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
        self.assertIn("XXbreakfastXX", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_97(self):
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
        self.assertIn("BREAKFAST", ctx["foods_by_category"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_98(self):
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
        self.assertIn("breakfast", ctx["XXfoods_by_categoryXX"])

    def xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_99(self):
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
        self.assertIn("breakfast", ctx["FOODS_BY_CATEGORY"])
    
    xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_1': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_1, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_2': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_2, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_3': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_3, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_4': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_4, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_5': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_5, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_6': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_6, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_7': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_7, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_8': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_8, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_9': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_9, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_10': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_10, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_11': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_11, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_12': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_12, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_13': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_13, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_14': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_14, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_15': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_15, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_16': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_16, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_17': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_17, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_18': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_18, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_19': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_19, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_20': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_20, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_21': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_21, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_22': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_22, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_23': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_23, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_24': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_24, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_25': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_25, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_26': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_26, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_27': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_27, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_28': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_28, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_29': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_29, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_30': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_30, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_31': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_31, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_32': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_32, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_33': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_33, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_34': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_34, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_35': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_35, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_36': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_36, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_37': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_37, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_38': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_38, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_39': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_39, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_40': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_40, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_41': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_41, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_42': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_42, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_43': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_43, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_44': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_44, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_45': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_45, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_46': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_46, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_47': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_47, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_48': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_48, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_49': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_49, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_50': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_50, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_51': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_51, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_52': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_52, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_53': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_53, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_54': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_54, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_55': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_55, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_56': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_56, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_57': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_57, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_58': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_58, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_59': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_59, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_60': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_60, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_61': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_61, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_62': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_62, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_63': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_63, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_64': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_64, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_65': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_65, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_66': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_66, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_67': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_67, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_68': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_68, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_69': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_69, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_70': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_70, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_71': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_71, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_72': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_72, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_73': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_73, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_74': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_74, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_75': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_75, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_76': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_76, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_77': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_77, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_78': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_78, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_79': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_79, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_80': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_80, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_81': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_81, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_82': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_82, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_83': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_83, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_84': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_84, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_85': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_85, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_86': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_86, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_87': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_87, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_88': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_88, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_89': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_89, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_90': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_90, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_91': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_91, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_92': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_92, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_93': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_93, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_94': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_94, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_95': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_95, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_96': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_96, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_97': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_97, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_98': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_98, 
        'xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_99': xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_99
    }
    
    def test_progress_values_in_context(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_orig"), object.__getattribute__(self, "xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_mutants"), args, kwargs, self)
        return result 
    
    test_progress_values_in_context.__signature__ = _mutmut_signature(xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_orig)
    xǁDailySummaryViewTestsǁtest_progress_values_in_context__mutmut_orig.__name__ = 'xǁDailySummaryViewTestsǁtest_progress_values_in_context'
