from django import forms
from .models import ParkingImage, Vehicle
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ParkingImageForm(forms.ModelForm):
    class Meta:
        model = ParkingImage
        fields = ['image']


# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class": "form-control"}))

    password1 = forms.CharField(max_length=150,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(max_length=150,
                                required=True,
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['license_plate', 'vehicle_type']


class VehicleSearchForm(forms.Form):
    license_plate = forms.CharField(max_length=12, label='License Plate')

    def clean_license_plate(self):
        license_plate = self.cleaned_data['license_plate']
        # Убираем пробелы, тире и приводим к верхнему регистру
        cleaned_license_plate = license_plate.upper().replace(" ", "").replace("-", "")
        return cleaned_license_plate
