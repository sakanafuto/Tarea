from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView

from .models import Task, User

class IndexView(ListView):
  model = User, Task
  template_name = 'tarea/tasks/index.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    return Task.objects.order_by('-pub_date')

class DetailView(DetailView):
  model = Task
  template_name = 'tarea/tasks/detail.html'

def new(request):
  model = User, Task
  template_name = "tarea/tasks/new.html"
  if request.method == "POST":
    task = Task(
      title=request.POST["title"],
      caption=request.POST["caption"],
      pub_date=timezone.now(),
      user=request.user
      )
    task.save()
    return redirect('tarea:index')
  return render(request, template_name)

def edit(request, pk):
  template_name = "tarea/tasks/edit.html"
  task = get_object_or_404(Task, pk=pk)
  if request.method == "POST":
    task.title = request.POST["title"]
    task.caption = request.POST["caption"]
    task.save()
    return redirect('tarea:detail', pk=pk)
  context = {"task":task}
  return render(request, template_name, context)

def delete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.delete()
  return redirect('tarea:index')