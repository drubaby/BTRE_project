from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Validations
        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email address is already registered')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

                    # # Log in automatically after registration
                    # # Bug: This method logs user in as admin as well
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')

                    # # Make user log in manually after registration
                    user.save()
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        # If user is found in db log them in
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

# Redirect to index page after logout
def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
