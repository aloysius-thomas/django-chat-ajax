from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class UserCreateForm(UserCreationForm):
    username = forms.EmailField(label='Email')
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget)

    class Meta(object):
        model = User
        fields = {
            'username',
            'first_name',
            'last_name',
            'date_of_birth',
            # 'avatar'
        }
