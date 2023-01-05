from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('signup/', views.signUpView, name="signup"),
  path('login/', views.loginView, name="login-view"),
  path('logout/', views.logoutView, name="logout-view"),
  path('complete_reg/', views.complete_reg, name="complete_reg"),
  path('dashboard/', views.dashboard, name="dashboard"),
  path('create/', views.createPost, name="create_post"),
  path('<str:uid>/', views.View_Post, name="view_post"),
]