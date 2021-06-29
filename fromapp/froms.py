from django import forms
from django.core import validators



class Signup(forms.Form):
    username = forms.CharField(required=False, label='User Name', initial='username')
    email = forms.EmailField(label="Email", initial='email@email.com')
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    First_Name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={"placeholder": "Enter your name"}))
    Last_Name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': "Enter your last name"}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'placeholder': "Enter your address"}))
    phone = forms.CharField(label="Mobile Number", widget=forms.TextInput(attrs={'placeholder': "Enter your 11 digit mobile number"}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'type': "date"}))


class Form(forms.Form):
    booleanField = forms.BooleanField(required=False)
    charfield = forms.CharField(required=False, max_length=15, min_length=3)
    #choisefield = forms.ChoiceField(choices=(('1','Web Developer'), ('2', 'App Developer'),('3', 'Desktop Developer')))
    choisefield = forms.ChoiceField(choices=(('', '---Select Option---'),('1','Web Developer'), ('2', 'App Developer'),('3', 'Desktop Developer') ))
    field = (('', '---Select Option---'),('1','Web Developer'), ('2', 'App Developer'),('3', 'Desktop Developer') )
    value = forms.ChoiceField(choices=field)
    field_1 = (('1','Web Developer'), ('2', 'App Developer'),('3', 'Desktop Developer'))
    radio_button = forms.ChoiceField(choices=field_1, widget=forms.RadioSelect())
    multipulchoise = forms.MultipleChoiceField(choices=field)
    multipulcheckbox = forms.MultipleChoiceField(choices=field_1, widget=forms.CheckboxSelectMultiple)


def even_or_not(value):
    if value%2 == 1:
        raise forms.ValidationError("Please Insert an even number")


class User_form(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(3)])
    number_feild = forms.IntegerField(validators=[validators.MaxValueValidator(8), validators.MinValueValidator(2)])
    even_field = forms.IntegerField(validators=[even_or_not])


class email_validation(forms.Form):
    user_email = forms.EmailField()
    user_vemail = forms.EmailField()

    def clean(self):
        all_cleaned_data = super().clean()
        user_email = all_cleaned_data['user_email']
        user_vemail = all_cleaned_data['user_vemail']

        if user_email != user_vemail:
            raise forms.ValidationError('Your email does not match')



