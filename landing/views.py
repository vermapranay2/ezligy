from django.shortcuts import render, redirect
from .forms import RegisterForm , ContactForm
from .models import Service, Heads, Single
from django.urls import reverse

# Create your views here.

def index(request):

     return render(request, 'index.html',)


def services(request):

     return render(request, 'test.html',)

def sitemap(request):

     return render(request, 'sitemap.html',)


def feedback(request):

     return render(request, 'feedback.html',)

def paralegal(request):

     return render(request, 'paralegal.html',)

def contact(request):
     form= ContactForm(request.POST or None)
     if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
          return redirect('index')


     context = {"form": form,}
     return render(request, 'contact.html', context)

def register(request):
     form = RegisterForm(request.POST or None)
     if form.is_valid():
          instance = form.save(commit=False)
          instance.save()
     context = {"form": form,}
     return render(request, 'register.html', context)



def formation(request):
     head=Heads.objects.get(pk=1)

     allServices=head.service_set.all()
     context = {'services':allServices,'heading':'Formation Of Entity'}


     return render(request, 'heads.html',context)

def sole(request):

     singleObj=Single.objects.get(pk=1)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def society(request):

     singleObj=Single.objects.get(pk=2)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def partnership(request):

     singleObj=Single.objects.get(pk=3)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def private(request):

     singleObj=Single.objects.get(pk=4)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def llp(request):

     singleObj=Single.objects.get(pk=5)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def opc(request):

     singleObj=Single.objects.get(pk=6)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})


def trust(request):

     singleObj=Single.objects.get(pk=7)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def nidhi(request):

     singleObj=Single.objects.get(pk=8)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def section8(request):

     singleObj=Single.objects.get(pk=9)

     print(singleObj)

     return render(request,'services.html',{'obj':singleObj})

def paraform(request):

     return render(request, 'paralegal_form.html',)


