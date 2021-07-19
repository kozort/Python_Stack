from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    #context = {"USERS": USER.objects.all()}
    return render(request, 'index.html')