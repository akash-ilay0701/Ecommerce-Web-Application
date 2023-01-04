from django.shortcuts import render, redirect
from .models import Course, Order


# Create your views here.

def home(request):
    data = Course.objects.all()
    return render(request, "home.html",{'courses': data})

def learnMore(request, id):
    value = Course.objects.get(id=id)
    return render(request, "learnMore.html", {'course' : value})


def buyNow(request,id):
    data = Course.objects.get(id=id)
    return render(request, "buyNow.html", {"id":id, 'course':data})

def confirmBuy(request,id):
    order = Order()
    order.studentName = request.POST.get("name")
    order.email = request.POST.get("email")
    order.mobile = request.POST.get("contact")
    order.address = request.POST.get("address")
    order.course = Course.objects.get(id=id)
    order.save()
    return redirect('confirmed')


def confirmed(request):

    return render(request, 'confirmed.html')
