from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from rest_framework import status 

from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
  
  class Meta:
    model = User
    fields = ( 'email', 'username', 'first_name', 'last_name', 'password1', 'password2')

  def save(self, commit=True):
    # Save the provided password in hashed format
    user = super().save(commit=False)
    user.set_password(self.cleaned_data["password1"])
    if commit != False:
      user.save()
    return user

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1")
    password2 = self.cleaned_data.get("password2")
    if password1 and password2 and password1 != password2:
      raise ValidationError("Passwords don't match")
    return password2

  def clean_username(self):
    _username = self.cleaned_data["username"]
    username = _username.lower()
    
    if User.objects.filter(username=username).exists():
      raise ValidationError(
        _(f" username '{_username}' is already taken, try another one."),
        code='invalid'
      )
    return _username

  def clean_email(self):
    _email = self.cleaned_data["email"]
    email = _email
    # email = _email.lower()
    
    if User.objects.filter(email=email).exists():
      raise ValidationError(
        _(f" email '{_email}' is already registered."),
        code='invalid'
      )
    return _email

    
