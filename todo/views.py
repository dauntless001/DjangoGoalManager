from django.shortcuts import render, HttpResponse, redirect
from .models import Todo
from .forms import TodoForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts')
def home_view(request):
    query = Todo.objects.filter(user=request.user)
    qs = Paginator(query, 5)
    page_number = request.GET.get('page')
    qs = qs.get_page(page_number)
    name = 'index.html'
    context = {
        'todos' : qs
    }
    return render(request, name, context)

@login_required(login_url='/accounts')
def delete_view(request, slug):
    qs = Todo.objects.get(slug=slug)
    if qs:
        qs.delete()
        messages.success(request, 'Task Deleted Successfully')
        return redirect('todo:home')



@login_required(login_url='/accounts')
def complete_view(request, slug):
    qs = Todo.objects.get(slug=slug)
    if qs:
        qs.completed = True
        qs.save()
        messages.success(request, 'Congratulations for Making it till the End')
        return redirect('todo:home')


@login_required(login_url='/accounts')
def create_view(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        create = form.save(commit=False)
        create.user = request.user
        create.save()
        messages.success(request, 'Task Created Successfully')
        return redirect('todo:home')
    name = 'create_todo.html'
    context = {
        'form' : form
    }
    return render(request, name, context)

@login_required(login_url='/accounts')
def edit_view(request, slug):
    qs = Todo.objects.get(slug=slug)
    form = TodoForm(request.POST or None, instance=qs)
    if form.is_valid():
        create = form.save(commit=False)
        create.user = request.user
        create.save()
        messages.success(request, 'Task update Successful')
        return redirect('todo:home')
    name = 'create_todo.html'
    context = {
        'form' : form
    }
    return render(request, name, context)