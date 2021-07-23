from django.shortcuts import render, redirect
from .models import USER
from django.contrib import messages
import bcrypt


def index(request):
    # if a user is logged in prevent relogin from a different user. Do not want to overwrite the session data. User needs to log out first then they can go to index.thml to login/register
    try: 
        if request.session['userid']:
            context = {"User": USER.objects.get(id=request.session['userid'])}
            return render(request, 'success.html', context)
    except:
        return render(request, 'index.html')

def success(request):
        try:
            context = {
                "User": USER.objects.get(id=request.session['userid']),
                "how_directed": request.session['how_directed']}
            print(USER.objects.get(id=request.session['userid']).first_name)
            return render(request, 'success.html', context)
        except:
            return redirect('/')

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
            request.session['userid'] = USER.objects.last().id
            request.session['how_directed'] = "registered"
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
                request.session['how_directed'] = "logged in"
                return redirect('/success')
            else:
                request.session['er'] = "Invalid credentials."
                return redirect('/')
    return redirect('/')

def logout(request):
    if request.method == 'POST':
        request.session.flush()
    return redirect('/')

def email(request):
    if request.method == 'POST':
        found = False
        print(request.POST['email'])
        if len(USER.objects.filter(email=request.POST['email'])) > 0:
            found = True
        context = {'bad': found}
        return render(request, 'partials/email.html', context)  # render a partial and return it
    return redirect('/')