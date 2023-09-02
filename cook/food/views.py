#Import all necessary functions
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Recipe
from .forms import UserRegistrationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.

# Define a view that will return the home page, this page contains a list of recipes.
def home(request):
    print(request.user.username)
    recipe_list = Recipe.objects.order_by('id')
    context = {'recipe_list': recipe_list, "username": request.user.username}
    return render(request, 'home.html', context)



# Define a view funstion that will take a request from the user, where they have chosen the recipe they wanna see.
# This function returns the full recipe page
def recipe_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe.html', {'recipe': recipe})


# Define a function that will take the user to the about page
def about(request):
    return render(request, 'about.html')
    

#Define a function that will take the user to the login page
def user_login(request):
    return render(request, 'authentication/login.html')


#logout funstion to send user back to login page.
def logout(request):
    return render(request, 'authentication/login.html')


# Define a function that will verify the user within the database and log them into the website,
# If user is valid, if not it will prompt them to login again.
def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('food:user_login'))
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('food:home')
        )


# Define a function that will have a user register their account if they are a new user.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('food:login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)