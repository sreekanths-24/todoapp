from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *  # Import all models from models.py
from .forms import *

# Existing views...

def mark_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.completed = True
        task.save()
        return redirect('task_list')

    # Handle GET requests or other cases here (if needed).

# Other views...

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        form = EditTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = EditTaskForm(instance=task)

    context = {'form': form, 'task': task}
    return render(request, 'edit_task.html', context)

def task_list(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)
        form = TaskForm()

        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                return redirect('task_list')

        context = {'tasks': tasks, 'form': form}
        return render(request, 'task_list.html', context)
    else:
        return redirect('signin')

def task_detail(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id, user=request.user)
        context = {'task': task}
        return render(request, 'task_detail.html', context)
    else:
        return redirect('signin')

def task_delete(request, task_id):
    if request.user.is_authenticated:
        task = Task.objects.get(id=task_id, user=request.user)
        task.delete()
        return redirect('task_list')
    else:
        return redirect('signin')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Signup successful!')
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Signin successful!')
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    messages.success(request, 'Signout successful!')
    return redirect('signin')
