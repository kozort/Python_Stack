from django.shortcuts import render, redirect
from time import gmtime, strftime
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        print("created gold = 0")
    return render(request, 'index.html')

def farm(request):
    if request.method == 'POST':
        addGold(request,10,20)
    return redirect('/')

def cave(request):
    if request.method == 'POST':
        addGold(request,5,10)
    return redirect('/')

def house(request):
    if request.method == 'POST':
        addGold(request,2,5)
    return redirect('/')

def casino(request):
    if request.method == 'POST':
        addGold(request,-50,50)
    return redirect('/')

def clear(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect("/")

def addGold(request,min,max):
    gold = random.randint(min,max)
    request.session['gold'] += gold
    date = strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['activities'].append(f"Earned {gold} from the farm! ({date})")
    return request