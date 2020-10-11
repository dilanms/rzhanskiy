from django import forms
from django.contrib.auth.models import User
from .models import Profile, Company, Affiliater, Employee, Services


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Passwords don\'t match.")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'company_inn')
        widgets = {'author': forms.HiddenInput()}


class AffiliaterForm(forms.ModelForm):
    class Meta:
        model = Affiliater
        fields = ('affiliate_name', 'affiliate_adres', 'tel_number')
        widgets = {'company_name': forms.HiddenInput()}


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_name', 'employee_surname', 'employee_patronymic')

class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('service_name', 'service_price', 'service_duration')