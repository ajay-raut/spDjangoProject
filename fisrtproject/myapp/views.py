from django.shortcuts import render

from django.http import HttpResponse

from myapp.models import Book, Student


def show_data(request):

    return render(request,"show-data.html",{"book":Book.objects.all()})

def student_data(request):
    return render(request,"student-data.html",{"student":Student.objects.all()})

def backbtn(request):
    return render(request,"show-data.html",{"book":Book.objects.all()})   
