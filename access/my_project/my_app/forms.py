from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import OldEmployee, NewEmployee, Question1, Question3

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
        }

class OldEmployeeForm(forms.ModelForm):
    class Meta:
        model = OldEmployee
        fields = ("user", "first_name", "last_name", "email", "image")
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'type':'hidden'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name...'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image...'}),
        }

class NewEmployeeForm(forms.ModelForm):
    class Meta:
        model = NewEmployee
        fields = ("user", "first_name", "last_name", "email", "image")
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control', 'id':'user1', 'value':'', 'type':'hidden'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name...'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name...'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email...'}),
            'image':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image...'}),
        }

class QuestionForm1(forms.ModelForm):
    class Meta:
        model = Question1
        fields = ("user", "answer1", "answer2", "answer3", "answer4", "answer5", "answer6", "answer7")
        widgets = {
            'user':forms.TextInput(attrs={'value':'', 'id':'user1', 'type':'hidden'}),
            'answer1':forms.Select(attrs={'class':'form-control'}),
            'answer2':forms.Select(attrs={'class':'form-control'}),
            'answer3':forms.Select(attrs={'class':'form-control'}),
            'answer4':forms.Select(attrs={'class':'form-control'}),
            'answer5':forms.Select(attrs={'class':'form-control'}),
            'answer6':forms.Select(attrs={'class':'form-control'}),
            'answer7':forms.Select(attrs={'class':'form-control'}),
        }

class QuestionForm3(forms.ModelForm):
    class Meta:
        model = Question3
        fields = ('user', 'answer1', 'answer2')
        widgets = {
            'user':forms.TextInput(attrs={'value':'', 'id':'user1', 'type':'hidden'}),
            'answer1':forms.Select(attrs={'class':'form-control'}),
            'answer2':forms.Select(attrs={'class':'form-control'}),
        }