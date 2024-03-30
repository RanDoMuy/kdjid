"""WealthOrigin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from wealth_origin_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('secret_admin/', admin.site.urls),
    path('', views.load, name= "load"),
    path('home/', views.home, name= "home"),
    path("about/", views.about, name="about"),
    path("terms&conditions/", views.terms, name="terms"),
    path("register/", views.register, name="register"),
    path("account-verification/", views.verify, name="account_verify"),
    path("accounts/login/", views.user_login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("deposit/", views.deposit, name="deposit"),
    path("confirm_d/<str:amount>/", views.confirm_deposit, name="confirmd"),
    path("confirm_w/", views.confirm_withdraw, name="confirmw"),
    path("investment_plan/success", views.invest_success, name="invest_success"),
    path("investment_plan/failed", views.invest_failed, name="invest_failed"),
    path("investment_plan/", views.invest, name="invest"),
    path('investment_plan/starter/', views.starter, name="starter plan"),
    path('investment_plan/bronze/', views.bronze, name="bronze plan"),
    path('investment_plan/silver/', views.silver, name="silver plan"),
    path('investment_plan/gold', views.gold, name="gold plan"),
    path('investment_plan/diamond/', views.diamond, name="diamond plan"),
    path('investment_plan/platinum/', views.platinum, name="platinum plan"),
    path("withdraw/", views.withdraw, name="withdraw"),
    path("faq/", views.faq, name="faq"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.user_logout, name="logout")
]

handler404 = 'wealth_origin_app.views.handler404'
