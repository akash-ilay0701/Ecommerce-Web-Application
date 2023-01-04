#from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView




# def login(request):
#     return render(request, "registration/login.html")

class register(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'registration/signup.html'
