from django.shortcuts import render, redirect
from .models import USER

def index(request):
    context = {"USERS": USER.objects.all()}
    return render(request, 'index.html', context)

def takeUser(request):
    if request.method == 'POST':
        if request.POST['firstname'] != "":
            if request.POST['lastname'] != "":
                if request.POST['email'] != "":
                    if request.POST['age'] != "":
                        USER.objects.create(
                            first_name = request.POST['firstname'], 
                            last_name = request.POST['lastname'], 
                            email_address = request.POST['email'],
                            age = request.POST['age']
                            )
    return redirect('/')