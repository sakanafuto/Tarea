from django.urls import path
from django.contrib.auth import views as av
from . import views

app_name = 'tarea'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),

  path('login/', av.LoginView.as_view(), name='login'),
  path('logout/', av.LogoutView.as_view(), name='logout'),
  path('password_change/', av.PasswordChangeView.as_view(), name='password_change'),
  path('password_change/done/', av.PasswordChangeDoneView.as_view(), name='password_change_done'),

  path('profile/', views.UserProfileView.as_view(), name="profile"),
  path('create/', views.UserCreateView.as_view(), name="create"),

  path('new/', views.new, name="new"),
  path('task/<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('task/<int:pk>/edit', views.edit, name='edit'),
  path('task/<int:pk>/delete', views.delete, name='delete'),
  path('task/uncomplete/<int:pk>', views.uncomplete, name="uncomplete"),
  path('task/complete/<int:pk>', views.complete, name="complete"),
]