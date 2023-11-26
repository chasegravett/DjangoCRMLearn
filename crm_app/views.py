from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import Customer



def home(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Logged in as {username}")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return render(request, 'home.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            # Authenticate newly made user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in as {username}")
                return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form})
    
    return render(request, 'register.html', {'form' : form})


def show_users(request):
    customers = Customer.objects.all()
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_firstname(request):
    customers = Customer.objects.all().order_by('first_name')
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_lastname(request):
    customers = Customer.objects.all().order_by('last_name', 'first_name')
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_creation(request):
    customers = Customer.objects.all().order_by('created_at')
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_street(request):
    customers = Customer.objects.all().order_by('street_address')
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_state(request):
    customers = Customer.objects.all().order_by('state')
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_email(request):
    customers = Customer.objects.all().order_by('email')
    return render(request, 'show_users.html', {'customers' : customers})


def show_users_sorted_phone(request):
    customers = Customer.objects.all().order_by('phone')
    return render(request, 'show_users.html', {'customers' : customers})