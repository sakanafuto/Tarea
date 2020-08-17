from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Task, User

class IndexView(ListView):
  model = User, Task
  template_name = 'tarea/tasks/index.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    return Task.objects.order_by('-pub_date')