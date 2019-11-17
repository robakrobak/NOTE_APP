from django import forms
from django.db import models
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
        fields = ('user', 'awatar', 'about_me', 'location', 'birth_date')


# class UserProfileForm(forms.ModelForm):
#     # user = forms.OneToOneField(User, on_delete=models.DO_NOTHING)
#     # awatar = forms.FileField(upload_to='awatar')
#     about_me = forms.CharField(max_length=512)
#     location = forms.CharField(max_length=30, blank=True)
#     birth_date = forms.DateField(null=True, blank=True)
#
#     def __init__(self, *args, **kwargs):
#         super(UserProfileForm, self).__init__(*args, **kwargs)
#         try:
#             self.fields['user'].initial = self.instance.user.user
#             self.fields['awatar'].initial = self.instance.user.awatar
#             self.fields['about_me'].initial = self.instance.user.about_me
#             self.fields['location'].initial = self.instance.user.location
#             self.fields['birth_date'].initial = self.instance.user.birth_date
#         except User.DoesNotExist:
#             pass
#
#     class Meta:
#         model = UserProfile
#         fields = ['user', 'awatar', 'about_me', 'location', 'birth_date']
