from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    return render(request,'study_logs/index.html')

def history(request):
    return render(request,'study_logs/history.html')

def gallery(request):
    return render(request,'study_logs/gallery.html')

def news(request):
    return render(request,'study_logs/news.html')

def familytree(request):
    return render(request,'study_logs/familytree.html')

def base(request):
    return render(request,'study_logs/index.html')
