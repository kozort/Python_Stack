from django.shortcuts import render, redirect
from .models import USER
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')

# POST
def register(request):
    if request.method == 'POST':
        errors = USER.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            USER.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                birthday = request.POST['birthday'],
                password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode() 
            )
            return redirect(f'/success')
    return redirect('/')

# POST
def login(request):
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        user = USER.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                return redirect('/success')
            else:
                request.session['er'] = "Invalid credentials."
                return redirect('/')
    return redirect('/')
