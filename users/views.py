from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm


def register(request):
    if request.method != 'POST':
        form = SignUpForm()
    else:
        form = SignUpForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #new_user.refresh_from_db()
            #new_user.profile.Gender = form.cleaned_data.get('Gender')
            #new_user.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form':form}
    return render(request,'registration/register.html', context)
