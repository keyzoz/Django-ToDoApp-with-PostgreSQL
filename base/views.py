from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Task
# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'task_list'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'detail_task'
    template_name = 'base/task_detail.html'
    success_url = reverse_lazy('task:task-detail')
    
class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('task:tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_form.html'
    success_url = reverse_lazy('task:tasks')
    
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task_delete'
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('task:tasks') 
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    