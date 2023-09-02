#Import all necessary functions.
from django.urls import path, re_path
from . import views



#Define a namespacing for the app
app_name = 'food'

# url patterns for the views defined.
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:recipe_id>/recipe', views.recipe_view, name='recipe_view'),
    path('login', views.user_login, name='login'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('register/', views.register, name='register'),
    re_path('about/', views.about, name='about'),
    re_path('logout/', views.logout, name='logout')
    
]