from django.conf.urls import url
from my_app import views

app_name = "my_app"

urlpatterns = [
    url(r"signup/", views.signup, name="signup"),
    url(r'signin/', views.signin, name="signin"),
    url(r'signin_old_employeer/', views.oldsignin, name="oldsignin"),
    url(r'signup_old_employeer/', views.oldsignup, name="oldsignup"),
]