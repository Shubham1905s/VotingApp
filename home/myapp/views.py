from django.shortcuts import render,HttpResponse


def home(request):
    return render(request,'home.html')

def signin(request):
    return render(request,'signin.html')

def instructions(request):
    return render(request,'instructions.html')

def votingPage(request):
    return render(request,'votingPage.html')

def loginreal(request):
    return render(request,'loginreal.html')

def about(request):
    return render(request,'about.html')