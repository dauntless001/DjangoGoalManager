from django.shortcuts import render, redirect
from .models import Goal
from .forms import GoalForm, ObjForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/accounts')
def goal_list(request):
    query = Goal.objects.filter(user=request.user)
    qs = Paginator(query, 6)
    page_number = request.GET.get('page')
    qs = qs.get_page(page_number)
    name = 'goal_list.html'
    context = {
        'goals':qs
    }
    return render(request, name, context)


@login_required(login_url='/accounts')
def goal_detail(request, slug):
    qs = Goal.objects.get(slug=slug)
    query = qs.objectives.all()
    form = ObjForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.obj = qs
        obj.user = request.user
        obj.save()
        return redirect('goals:detail', slug=qs.slug)
    paginate = Paginator(query, 12)
    page_number = request.GET.get('page')
    query = paginate.get_page(page_number)
    name = 'goal_detail.html'
    btn_name = 'Add Obj'
    context = {
        'goal':qs,
        'obj' : query,
        'form' : form,
        'btn_name' : btn_name
    }
    return render(request, name, context)


@login_required(login_url='/accounts')
def goal_delete(request, slug):
    qs = Goal.objects.get(slug=slug)
    if qs:
        if qs.completed == True:
            qs.delete()
            messages.success(request, 'Hurray, We achieved the aim, Time to step up!')
        else:
            qs.delete()
            messages.success(request, 'Oops, maybe we will not be able to achieve it anyways')
        return redirect('goals:list')



@login_required(login_url='/accounts')
def goal_complete(request, slug):
    qs = Goal.objects.get(slug=slug)
    if qs:
        qs.completed = True
        qs.save()
        return redirect('goals:list')


@login_required(login_url='/accounts')
def goal_create(request):
    form = GoalForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'To achieve this Goal with less effort, as a team i will want us to create objectives')
        return redirect('goals:detail', slug=instance.slug)
    name = 'goal_create.html'
    context = {
        'form':form
    }
    return render(request, name, context)



@login_required(login_url='/accounts')
def goal_edit(request, slug):
    qs = Goal.objects.get(slug=slug)
    form = GoalForm(request.POST or None, instance=qs)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Goal update successful')
        return redirect('goals:detail', slug=instance.slug)
    name = 'goal_create.html'
    context = {
        'form':form
    }
    return render(request, name, context)