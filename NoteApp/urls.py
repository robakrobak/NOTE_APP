"""NoteApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

from user.views import signup, login_view, UserProfileModel, PasswordResetView2, change_password
from django.urls import path
from core.views import NotesListView, logout_view
from note.views import NoteCreateView, NoteDetailView, mark_as_done, add_comment_to_note

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_view, name='login'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', NotesListView.as_view(), name='home'),
    url(r'^password_reset/$', PasswordResetView2.as_view(template_name='password_reset_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    path('user_profile/<int:pk>/', UserProfileModel.as_view(), name='user_profile'),
    url(r'^note/add/$', NoteCreateView.as_view(), name='add_note'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('notes/<int:pk>/', mark_as_done, name='mark_as_done'),
    url(r'^password/$', change_password, name='change_password'),
    path('note/<slug:pk>/', add_comment_to_note, name='add_comment_to_note'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
