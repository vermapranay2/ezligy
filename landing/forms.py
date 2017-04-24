from django import forms
from .models import Register, Contact


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields =[
            "first_name","last_name","father_name","date_of_birth","gender","email","office_address",
            "mobile_number","office_landline","State_BAR_Registration","local_BAR","Place_Of_Practice",
            "area","other_area",
        ]


class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields=[
            "name","contact","email","service","message"
        ]


