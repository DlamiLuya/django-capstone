# Import all necessary functions
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Define a class that will create a form that will allow the user to register as a new user.
class UserRegistrationForm(UserCreationForm):
    """This method will define the user registration form as per the django template
        It adds more functionalities like first name, last name and email

        :param charfield first_name: The users first name
        :param Charfield last_name: The users last name
        :param Charfield email_address: The users email adress

        :returns: The sum of two numbers

        :rtype: int
    """
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email_address = forms.CharField()
    

    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name', 'email_address', 'password1', 'password2']