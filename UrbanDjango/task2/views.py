import django
from django.shortcuts import render
from django.views.generic import TemplateView

def func1(request):
    return render(request, 'func_template.html')

class class1(TemplateView):
    template_name = 'class_template.html'