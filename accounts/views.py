from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


def register(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Account creation successfull--{ username }')
            return redirect('blog:home')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form':form})

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request, 'accounts/logout.html')
