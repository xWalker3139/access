from django.db import models
from django.contrib.auth.models import User

EXPERIENCE_N = (
    ("0-6 months", "0-6 months"),
    ("6-12 months", "6-12 months"),
)

EXPERIENCE = (
    ("1-3 years", "1-3 years"),
    ("3-5 years", "3-5 years"),
    ("5-10 years", "5-10 years"),
    ("More than 10 years", "More than 10 years"),
)

INDUSTRIES = (
    ('Technology', 'Technology'),
    ('Healthcare', 'Healthcare'),
    ('Finance', 'Finance'),
    ('Education', 'Education'),
    ('Retail', 'Retail'),
    ('Other', 'Other'),
)

WORK = (
    ('Frontend', 'Frontend'),
    ('Backend', 'Backend'),
    ('Frontend and Backend', 'Frontend and Backend'),
)

FRONTEND = (
    ('React', 'React'),
    ('Angular', 'Angular'),
    ('Vue', 'Vue'),
    ('Other', 'Other')
)

TOOLS = (
    ('NPM/Yarn', 'NPM/Yarn'),
    ('Webpack', 'Webpack'),
    ('Grunt/Gulp', 'Grunt/Gulp'),
    ('Babel', 'Babel'),
)

BACKEND = (
    ('Node.js', 'Node.js'),
    ('Django', 'Django'),
    ('Ruby on Rails', 'Ruby on Rails'),
    ('Spring Boot', 'Spring Boot'),
    ('ASP.NET', 'ASP.NET'),
    ('Other', 'Other'),
)

PROGRAMMING = (
    ('Java', 'Java'),
    ('Python', 'Python'),
    ('Ruby', 'Ruby'),
    ('PHP', 'PHP'),
    ('C#', 'C#'),
    ('Other', 'Other')
)

COMMUNICATION = (
    ('Assertive', 'Assertive'),
    ('Passive', 'Passive'),
    ('Agressive', 'Agressive'),
    ('Collaborative', 'Assertive'),
    ('Other', 'Other'),
)

CONFLICTS = (
    ('Avoidance', 'Avoidance'),
    ('Confrontation', 'Confrontation'),
    ('Compromise', 'Compromise'),
    ('Collaboration', 'Collaboration'),
    ('Other', 'Other'),
)

class OldEmployee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=264, null=True, blank=False)
    last_name = models.CharField(max_length=264, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    image = models.FileField(null=True, blank=False, upload_to='images/')

    def __str__(self):
        return self.first_name

class NewEmployee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=264, null=True, blank=False)
    last_name = models.CharField(max_length=264, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    image = models.FileField(null=True, blank=False, upload_to='images/')

    def __str__(self):
        return self.first_name

class Question1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=264, null=True, blank=False, choices=EXPERIENCE_N)
    answer2 = models.CharField(max_length=264, null=True, blank=False, choices=INDUSTRIES)
    answer3 = models.CharField(max_length=264, null=True, blank=False, choices=WORK)
    answer4 = models.CharField(max_length=264, null=True, blank=False, choices=FRONTEND)
    answer5 = models.CharField(max_length=264, null=True, blank=False, choices=TOOLS)
    answer6 = models.CharField(max_length=264, null=True, blank=False, choices=BACKEND)
    answer7 = models.CharField(max_length=264, null=True, blank=False, choices=PROGRAMMING)

    def __str__(self):
        return self.answer1

class Question2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=264, null=True, blank=False, choices=EXPERIENCE)
    answer2 = models.CharField(max_length=264, null=True, blank=False, choices=INDUSTRIES)
    answer3 = models.CharField(max_length=264, null=True, blank=False, choices=WORK)
    answer4 = models.CharField(max_length=264, null=True, blank=False, choices=FRONTEND)
    answer5 = models.CharField(max_length=264, null=True, blank=False, choices=TOOLS)
    answer6 = models.CharField(max_length=264, null=True, blank=False, choices=BACKEND)
    answer7 = models.CharField(max_length=264, null=True, blank=False, choices=PROGRAMMING)

    def __str__(self):
        return self.answer1

class Question3(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer1 = models.CharField(max_length=264, null=True, blank=False, choices=COMMUNICATION)
    answer2 = models.CharField(max_length=264, null=True, blank=False, choices=CONFLICTS)

    def __str__(self):
        return self.answer1

# Create your models here.
