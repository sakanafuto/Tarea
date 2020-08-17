from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, FormView

from .models import Task, User

class UserCreateView(FormView):
  form_class = UserCreationForm
  template_name = 'registration/create.html'
  success_url = reverse_lazy('tarea:profile')
  def form_valid(self, form):
    print(self.request.POST['next'])
    if self.request.POST['next'] == 'back':
      return render(self.request, 'registration/create.html', {'form': form})
    elif self.request.POST['next'] == 'confirm':
      return render(self.request, 'registration/create_confirm.html', {'form': form})
    elif self.request.POST['next'] == 'regist':
      form.save()
      user = authenticate(
        username=form.cleaned_data['username'],
        password=form.cleaned_data['password1'],
      )
      login(self.request, user)
      return super().form_valid(form)
    else:
      return redirect(reverse_lazy('tarea:index'))

class UserProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'registration/profile.html'
  def get_queryset(self):
    return User.objects.get(id=self.request.user.id)

class IndexView(ListView):
  model = User, Task
  template_name = 'tarea/tasks/index.html'
  context_object_name = 'task_list'

  def get_queryset(self):
    return Task.objects.order_by('-pub_date')

class DetailView(DetailView):
  model = Task
  template_name = 'tarea/tasks/detail.html'

@login_required

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
  context = {"task": task}
  return render(request, template_name, context)

def delete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.delete()
  return redirect('tarea:index')

def uncomplete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.completed = False
  task.save()
  return redirect('tarea:index')

def complete(request, pk):
  task = get_object_or_404(Task, pk=pk)
  task.completed = True
  task.save()
  return redirect('tarea:index')