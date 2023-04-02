"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "my_app"

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'my_app/', include("my_app.urls")),
    url(r'home/', views.home, name="home"),
    url(r'new_employee/', views.new_account, name="new_account"),
    url(r'logout_user/', views.logout_user, name="logout_user"),
    url(r'new_employee_question1/(?P<pk>\d+)/', views.new_employee_question1, name="new_employee_question1"),
    url(r'new_employee_question2/', views.new_soft_questions, name="new_soft_questions"),
    url(r'settings/', views.settings, name="settings"),
    ###################################################
    url(r'old_employee/', views.old_account, name="old_account"),
    url(r'old_employee_settings/', views.old_employee_settings, name="old_settings"),
    url(r'old_employee_all_users/', views.all_users, name="all_users"),
    url(r'old_employee_question1/(?P<pk>\d+)/', views.old_employee_question, name="old_employee_question"),
    url(r'old_employee_question2/', views.soft_questions, name="soft_questions")

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
