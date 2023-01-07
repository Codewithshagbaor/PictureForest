from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name="index"),
  path('signup/', views.signUpView, name="signup"),
  path('login/', views.loginView, name="login-view"),
  path('logout/', views.logoutView, name="logout-view"),
  path('complete_reg/', views.complete_reg, name="complete_reg"),
  path('create/', views.createPost, name="create_post"),
  path('<str:uid>/', views.View_Post, name="view_post"),
  path('Profile/<str:username>/', views.view_user, name="view_user"),
]
