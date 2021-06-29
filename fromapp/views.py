from django.shortcuts import render
from . import froms
# Create your views here.


def from_1(request):
    signup = froms.Signup()
    dictionary = {
        'signup': signup
    }
    if request.method == 'POST':
        signup = froms.Signup(request.POST)
        if signup.is_valid():
            username = signup.cleaned_data['username']
            email = signup.cleaned_data['email']
            password = signup.cleaned_data['password']
            First_Name = signup.cleaned_data['First_Name']
            Last_Name = signup.cleaned_data['Last_Name']
            address = signup.cleaned_data['address']
            phone = signup.cleaned_data['phone']
            dob = signup.cleaned_data['dob']
            dictionary.update({'username': username})
            dictionary.update({'email': email})
            dictionary.update({'password': password})
            dictionary.update({'First_Name': First_Name})
            dictionary.update({'Last_Name': Last_Name})
            dictionary.update({"address": address})
            dictionary.update({'phone': phone})
            dictionary.update({"dob": dob})

            dictionary.update({'form_submited': "Yes"})

    return render(request, "from.html", context=dictionary)


def form(request):
    new_form = froms.Form()
    distionary = {
        'new_form': new_form
    }
    if request.method == "POST":
        new_form = froms.Form(request.POST)
        if new_form.is_valid():
            distionary.update({'booleanField': new_form.cleaned_data['booleanField']})
            distionary.update({'charfield': new_form.cleaned_data['charfield']})
            distionary.update({'choisefield': new_form.cleaned_data['choisefield']})
            distionary.update({'value': new_form.cleaned_data['value']})
            distionary.update({'radio_button': new_form.cleaned_data['radio_button']})
            distionary.update({'multipulchoise': new_form.cleaned_data['multipulchoise']})
            distionary.update({'multipulcheckbox': new_form.cleaned_data['multipulcheckbox']})
            distionary.update({'form_submited': "Yes"})
    return render(request, 'from1.html', context= distionary)


def user_form(request):
    user_form = froms.User_form()
    dictionary = {
        'user_form': user_form
    }
    if request.method == 'POST':
        user_form = froms.User_form(request.POST)
        dictionary.update({'user_form': user_form})
        if user_form.is_valid():
            dictionary.update({'name': user_form.cleaned_data['name']})
            dictionary.update({'number_feild': user_form.cleaned_data['number_feild']})
            dictionary.update({'form_submited': 'Yes'})
    return render(request, 'form3.html', context=dictionary)


def email_validation(request):
    email_form = froms.email_validation()
    dicitionary = {
        'email_form': email_form
    }
    if request.method == 'POST':
        email_form = froms.email_validation(request.POST)
        dicitionary.update({'email_form': email_form})
        if email_form.is_valid():
            #dicitionary.update({'user_email': email_form.cleaned_data['user_email']})
            #dicitionary.update({'user_vemail': email_form.cleaned_data['user_vemail']})
            dicitionary.update({'email_form': "Email Field Match "})
            dicitionary.update({'form_submited': 'Yes'})
    return render(request, 'email.html', context=dicitionary)