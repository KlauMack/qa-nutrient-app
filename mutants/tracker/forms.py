from .models import FoodEntry
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
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


class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ["name", "calories", "protein", "carbs", "fat", "date", "category"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "flex-1 p-2 rounded bg-transparent text-gray-100 text-right focus:outline-none focus:ring-2 focus:ring-green-400",
                "placeholder": "e.g. Oat meal, Apple"
            }),
            "calories": forms.NumberInput(attrs={
                "class": "w-24 p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
                "placeholder": "-"
            }),
            "protein": forms.NumberInput(attrs={
                "class": "w-16 p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
                "placeholder": "-"
            }),
            "carbs": forms.NumberInput(attrs={
                "class": "w-16 p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
                "placeholder": "-"
            }),
            "fat": forms.NumberInput(attrs={
                "class": "w-16 p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
                "placeholder": "-"
            }),
            "date": forms.DateInput(attrs={
                "class": "w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
                "type": "date"
            }),
            "category": forms.Select(attrs={
                "class": "w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400"})
        }

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400",
            }
        )
    )


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def xǁRegistrationFormǁ__init____mutmut_orig(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_1(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(**kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_2(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, )

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_3(self, *args, **kwargs):
        super(None, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_4(self, *args, **kwargs):
        super(RegistrationForm, None).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_5(self, *args, **kwargs):
        super(self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_6(self, *args, **kwargs):
        super(RegistrationForm, ).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_7(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = None
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_8(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['XXusernameXX'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_9(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['USERNAME'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_10(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['XXclassXX'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_11(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['CLASS'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_12(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'XXpeer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400XX'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_13(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'PEER W-FULL P-2 ROUNDED BG-GRAY-700 TEXT-GRAY-100 FOCUS:OUTLINE-NONE FOCUS:RING-2 FOCUS:RING-GREEN-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_14(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = None
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_15(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['XXpassword1XX'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_16(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['PASSWORD1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_17(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['XXclassXX'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_18(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['CLASS'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_19(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'XXpeer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400XX'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_20(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'PEER W-FULL P-2 ROUNDED BG-GRAY-700 TEXT-GRAY-100 FOCUS:OUTLINE-NONE FOCUS:RING-2 FOCUS:RING-GREEN-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_21(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = None

    def xǁRegistrationFormǁ__init____mutmut_22(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['XXpassword2XX'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_23(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['PASSWORD2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_24(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['XXclassXX'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_25(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['CLASS'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'

    def xǁRegistrationFormǁ__init____mutmut_26(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'XXpeer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400XX'

    def xǁRegistrationFormǁ__init____mutmut_27(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'PEER W-FULL P-2 ROUNDED BG-GRAY-700 TEXT-GRAY-100 FOCUS:OUTLINE-NONE FOCUS:RING-2 FOCUS:RING-GREEN-400'
    
    xǁRegistrationFormǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁRegistrationFormǁ__init____mutmut_1': xǁRegistrationFormǁ__init____mutmut_1, 
        'xǁRegistrationFormǁ__init____mutmut_2': xǁRegistrationFormǁ__init____mutmut_2, 
        'xǁRegistrationFormǁ__init____mutmut_3': xǁRegistrationFormǁ__init____mutmut_3, 
        'xǁRegistrationFormǁ__init____mutmut_4': xǁRegistrationFormǁ__init____mutmut_4, 
        'xǁRegistrationFormǁ__init____mutmut_5': xǁRegistrationFormǁ__init____mutmut_5, 
        'xǁRegistrationFormǁ__init____mutmut_6': xǁRegistrationFormǁ__init____mutmut_6, 
        'xǁRegistrationFormǁ__init____mutmut_7': xǁRegistrationFormǁ__init____mutmut_7, 
        'xǁRegistrationFormǁ__init____mutmut_8': xǁRegistrationFormǁ__init____mutmut_8, 
        'xǁRegistrationFormǁ__init____mutmut_9': xǁRegistrationFormǁ__init____mutmut_9, 
        'xǁRegistrationFormǁ__init____mutmut_10': xǁRegistrationFormǁ__init____mutmut_10, 
        'xǁRegistrationFormǁ__init____mutmut_11': xǁRegistrationFormǁ__init____mutmut_11, 
        'xǁRegistrationFormǁ__init____mutmut_12': xǁRegistrationFormǁ__init____mutmut_12, 
        'xǁRegistrationFormǁ__init____mutmut_13': xǁRegistrationFormǁ__init____mutmut_13, 
        'xǁRegistrationFormǁ__init____mutmut_14': xǁRegistrationFormǁ__init____mutmut_14, 
        'xǁRegistrationFormǁ__init____mutmut_15': xǁRegistrationFormǁ__init____mutmut_15, 
        'xǁRegistrationFormǁ__init____mutmut_16': xǁRegistrationFormǁ__init____mutmut_16, 
        'xǁRegistrationFormǁ__init____mutmut_17': xǁRegistrationFormǁ__init____mutmut_17, 
        'xǁRegistrationFormǁ__init____mutmut_18': xǁRegistrationFormǁ__init____mutmut_18, 
        'xǁRegistrationFormǁ__init____mutmut_19': xǁRegistrationFormǁ__init____mutmut_19, 
        'xǁRegistrationFormǁ__init____mutmut_20': xǁRegistrationFormǁ__init____mutmut_20, 
        'xǁRegistrationFormǁ__init____mutmut_21': xǁRegistrationFormǁ__init____mutmut_21, 
        'xǁRegistrationFormǁ__init____mutmut_22': xǁRegistrationFormǁ__init____mutmut_22, 
        'xǁRegistrationFormǁ__init____mutmut_23': xǁRegistrationFormǁ__init____mutmut_23, 
        'xǁRegistrationFormǁ__init____mutmut_24': xǁRegistrationFormǁ__init____mutmut_24, 
        'xǁRegistrationFormǁ__init____mutmut_25': xǁRegistrationFormǁ__init____mutmut_25, 
        'xǁRegistrationFormǁ__init____mutmut_26': xǁRegistrationFormǁ__init____mutmut_26, 
        'xǁRegistrationFormǁ__init____mutmut_27': xǁRegistrationFormǁ__init____mutmut_27
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁRegistrationFormǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁRegistrationFormǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁRegistrationFormǁ__init____mutmut_orig)
    xǁRegistrationFormǁ__init____mutmut_orig.__name__ = 'xǁRegistrationFormǁ__init__'


class ProfileSetupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["height", "weight", "weight_goal"]

        widgets = {
            "height": forms.NumberInput(attrs={"class": "peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400", "placeholder": "Height (cm)"}),
            "weight": forms.NumberInput(attrs={"class": "peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400", "placeholder": "Weight (kg)"}),
            "weight_goal": forms.NumberInput(attrs={"class": "peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400", "placeholder": "Weight Goal (kg)"}),
        }