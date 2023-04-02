from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OldEmployee, NewEmployee, Question1, Question2
from .forms import UserForm, OldEmployeeForm, NewEmployeeForm, QuestionForm1, QuestionForm3
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime

def home(request):
    date_posted = datetime.datetime.now().year
    context = {
        'date_posted':date_posted,
    }
    return render(request, "my_app/home.html", context)

def signup(request):
    date_posted = datetime.datetime.now().year
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            NewEmployee.objects.create(
                user=user,
                first_name=user.username,
            )
            messages.info(request, "You create an accont!")
            return redirect("my_app:signin")
        else:
            form = UserForm()
    context = {
        'form':form,
        'date_posted':date_posted,
    }
    return render(request, "my_app/signup.html", context)

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("new_account")
        else:
            messages.info(request, "Your password and email didn't match!")
    return render(request, "my_app/signin.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

@login_required
def new_account(request):
    return render(request, "my_app/new_account.html")

@login_required
def new_employee_question1(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        answer1 = request.POST.get("answer1")
        answer2 = request.POST.get("answer2")
        answer3 = request.POST.get("answer3")
        answer4 = request.POST.get("answer4")
        answer5 = request.POST.get("answer5")
        answer6 = request.POST.get("answer6")
        answer7 = request.POST.get("answer7")
        model = Question1(user=user, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, answer6=answer6, answer7=answer7)
        model.save()
        return redirect("new_soft_questions")
    return render(request, "my_app/new_employee_question1.html")

@login_required
def new_soft_questions(request):
    form = QuestionForm3()
    if request.method == "POST":
        form = QuestionForm3(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = QuestionForm3()
    context = {
        'form':form,
    }
    return render(request, "my_app/new_soft_questions.html", context)

@login_required
def settings(request):
    date_posted = datetime.datetime.now().year
    model = request.user
    form = NewEmployeeForm(instance=model)
    if request.method == "POST":
        form = NewEmployeeForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
        else:
            form = NewEmployeeForm()
    context = {
        'date_posted':date_posted,
        'form':form,
        'model':model,
    }
    return render(request, "my_app/settings.html", context)

###################################
############OLD####################
###################################

def oldsignup(request):
    date_posted = datetime.datetime.now().year
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            OldEmployee.objects.create(
                user=user,
                first_name=user.username,
            )
            messages.info(request, "You create an account!")
            return redirect("my_app:oldsignin")
        else:
            form = UserForm()
    context = {
        'form':form,
        'date_posted':date_posted,
    }
    return render(request, "my_app/oldsignup.html", context)

def oldsignin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("old_account")
        else:
            messages.info(request, "Your password and email didn't match!")
    return render(request, "my_app/oldsignin.html")

@login_required
def old_account(request):
    return render(request, "my_app/old_account.html")

@login_required
def old_employee_settings(request):
    date_posted = datetime.datetime.now().year
    model = request.user
    form = OldEmployeeForm(instance=model)
    if request.method == "POST":
        form = OldEmployeeForm(request.POST, request.FILES, instance=model)
        if form.is_valid():
            form.save()
        else:
            form = OldEmployeeForm()
    context = {
        'date_posted':date_posted,
        'form':form,
        'model':model,
    }
    return render(request, "my_app/old_settings.html", context)

@login_required
def all_users(request):
    model = NewEmployee.objects.all()
    context = {
        'model':model
    }
    return render(request, "my_app/all_users.html", context)

@login_required
def old_employee_question(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        answer1 = request.POST.get("answer1")
        answer2 = request.POST.get("answer2")
        answer3 = request.POST.get("answer3")
        answer4 = request.POST.get("answer4")
        answer5 = request.POST.get("answer5")
        answer6 = request.POST.get("answer6")
        answer7 = request.POST.get("answer7")
        model = Question2(user=user, answer1=answer1, answer2=answer2, answer3=answer3, answer4=answer4, answer5=answer5, answer6=answer6, answer7=answer7)
        model.save()
        return redirect("soft_questions")
    return render(request, "my_app/old_employee_question1.html")

@login_required
def soft_questions(request):
    form = QuestionForm3()
    if request.method == "POST":
        form = QuestionForm3(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = QuestionForm3()
    context = {
        'form':form,
    }
    return render(request, "my_app/soft_questions.html", context)

# Create your views here.
