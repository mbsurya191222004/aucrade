from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("signup/", views.Sign_up.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("login2/",views.login.as_view()),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auctons/add/", views.add_auctons.as_view()),
    path("auctons/deduct/", views.deduct_auctons.as_view()),

]
