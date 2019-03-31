from django.shortcuts import render, redirect

def register(request):
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')

# Redirect to index page after logout
def logout(request):
    return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
