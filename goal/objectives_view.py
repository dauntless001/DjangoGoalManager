from django.shortcuts import render, redirect
from .models import Objective, Goal
from .forms import ObjForm
from  django.contrib import messages

def obj_delete(request, slug, id):
    query = Goal.objects.get(slug=slug)
    qs = query.objectives.filter(id=id)
    if qs:
        qs.delete()
        messages.success(request, 'Objective Delete successful')
        return redirect('goals:detail', slug=query.slug)


def obj_complete(request, slug, id):
    query = Goal.objects.get(slug=slug)
    qs = query.objectives.filter(id=id)
    if qs:
        qs.update(completed = True)
        messages.success(request, 'Yay! We did it, Time to step-up friend')
        return redirect('goals:detail', slug=query.slug)


