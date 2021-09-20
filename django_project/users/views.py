from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Your account has been successfully created! You are now able to log in!")
            #password = form.cleaned_data.get('password')
            return redirect('login')
        else:
            messages.warning(request, "Failed to create account! Something went wrong!")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})