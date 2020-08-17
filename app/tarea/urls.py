from django.urls import path

from . import views

app_name = 'tarea'
urlpatterns = [
  path('', views.IndexView.as_view(), name='index'),

  path('new/', views.new, name="new"),
  path('task/<int:pk>/', views.DetailView.as_view(), name='detail'),
  path('task/<int:pk>/edit', views.edit, name='edit'),
  path('task/<int:pk>/delete', views.delete, name='delete'),
]