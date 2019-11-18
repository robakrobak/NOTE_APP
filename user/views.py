# django
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, User
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, render
from user.models import UserProfile
# python
from core.email_service import confirms_registration, password_reset_fail
from user.forms import SignUpForm, UserProfileForm
from user.models import UserProfile


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            UserProfile.objects.create(user=user)
            login(request, user)
            confirms_registration(email, username, raw_password)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class PasswordResetView2(PasswordResetView):
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = User.objects.filter(email=email).exists()
        if user:
            opts = {
                'use_https': self.request.is_secure(),
                'token_generator': self.token_generator,
                'from_email': self.from_email,
                'email_template_name': self.email_template_name,
                'subject_template_name': self.subject_template_name,
                'request': self.request,
                'html_email_template_name': self.html_email_template_name,
                'extra_email_context': self.extra_email_context,
            }
            form.save(**opts)
        else:
            password_reset_fail(email)
        return super().form_valid(form)

      
class UserProfileModel(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    success_url = "/"
    template_name = "user_profile.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
    # add permission for users, so everyone can not change others profile
