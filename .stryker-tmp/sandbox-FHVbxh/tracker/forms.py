from .models import FoodEntry
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


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

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password1'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'
        self.fields['password2'].widget.attrs['class'] = 'peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400'


class ProfileSetupForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["height", "weight", "weight_goal"]

        widgets = {
            "height": forms.NumberInput(attrs={"class": "peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400", "placeholder": "Height (cm)"}),
            "weight": forms.NumberInput(attrs={"class": "peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400", "placeholder": "Weight (kg)"}),
            "weight_goal": forms.NumberInput(attrs={"class": "peer w-full p-2 rounded bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-green-400", "placeholder": "Weight Goal (kg)"}),
        }