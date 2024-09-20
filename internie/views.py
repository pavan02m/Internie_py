from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'core/index.html')

def user_login(request):
    # if request.user.is_authenticated :
    #     return redirect('login')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in")# Log in the user
                return redirect('index')  # Redirect to a home page or dashboard
            else:
                messages.error(request, "Invalid credentials, please try again.")
                return redirect('login')  # Redirect to the login page again
            
        except:
            messages.warning(request, f"User with {username} does not exist")
            return redirect('login')  # Redirect or handle as needed
        
    return render(request, 'userauth/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "successfully logout.")
    return redirect("login")