from django.contrib import admin
from .models import OldEmployee, NewEmployee, Question1, Question2, Question3

admin.site.register(OldEmployee)
admin.site.register(NewEmployee)
admin.site.register(Question1)
admin.site.register(Question2)
admin.site.register(Question3)

# Register your models here.
