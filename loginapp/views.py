from django.shortcuts import render
from .models import UserInfo
from .forms import UserForm, UserInfoForm
from .new_forms import UserForm_1, UserInfoForm_1
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    diction = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        diction = {'user_basic_info': user_basic_info, 'user_more_info': user_more_info}
    return render(request, 'loginapp/index.html', context=diction)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    diction = {'user_form': user_form, 'user_info_form': user_info_form, 'registered': registered}

    return render(request, 'loginapp/registration.html', context=diction)


def registration(request):
    register = False
    if request.method == 'POST':
        user_form_1 = UserForm_1(data=request.POST)
        user_information_1 = UserInfoForm_1(data=request.POST)
        if user_form_1.is_valid() and user_information_1.is_valid():
            user_form = user_form_1.save()
            user_form.set_password(user_form.password)
            user_form.save()
            user_info = user_information_1.save(commit=False)
            user_info.user = user_form
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            register = True
    else:
        user_form_1 = UserForm_1()
        user_information_1 = UserInfoForm_1()
    diction = {'user_form': user_form_1, 'user_info': user_information_1, 'registered': register}
    return render(request, 'loginapp/registration_1.html', context=diction)


def login_page(request):
    return render(request, 'loginapp/login.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('Loginapp:index'))
            else:
                return HttpResponse('Account is not active !!')
        else:
            return HttpResponse('Account Details are wrong !....')
    else:
        return HttpResponseRedirect(reverse('Loginapp:index'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Loginapp:login'))