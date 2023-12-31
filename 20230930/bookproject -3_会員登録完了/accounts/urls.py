from django.urls import path
from django.contrib.auth import views as authview
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/",authview.LoginView.as_view(),name="login"),
    path("logout/",authview.LogoutView.as_view(),name="logout"),
    path("signup/",views.SignupView.as_view(),name="signup"),
]