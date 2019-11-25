from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from user.models import UserProfile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('awatar', 'about_me', 'location', 'birth_date')
        labels = {'awatar': 'Avatar'}

        widgets = {
            'about_me': forms.Textarea(),

            'birth_date': DatePickerInput()
        }
