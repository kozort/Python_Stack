from django.shortcuts import render, redirect, HttpResponse

def index(request):
    #context = {"USERS": USER.objects.all()}
    return render(request, 'index.html')
