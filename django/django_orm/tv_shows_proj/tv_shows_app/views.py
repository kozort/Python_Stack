from django.shortcuts import render, redirect
from .models import SHOW

# Create your views here.
def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {"Shows": SHOW.objects.all()}
    return render(request, 'all_shows.html', context)    

def shows_new(request):
    if request.method == 'GET':
        return render(request, 'show_new.html')
    return redirect('/shows')

def create(request):
    if request.method == 'POST':
        SHOW.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            description = request.POST['description'],
            release_date = request.POST['release_date']
        )
    return redirect(f'/shows/{SHOW.objects.last().id}')

def show_detail(request, showID):
    context = {"Show": SHOW.objects.get(id=showID)}
    return render(request, 'show_detail.html', context)

def edit(request, showID):
    if request.method == 'GET':
        context = {"Show": SHOW.objects.get(id=showID)}
        return render(request, 'show_edit.html', context)
    return redirect('/shows')

def update(request, showID):
    if request.method == 'POST':
        c = SHOW.objects.get(id=showID)
        c.title = request.POST['title']
        c.network = request.POST['network']
        c.description = request.POST['description']
        c.release_date = request.POST['release_date']
        # won't update for some reason, T/S this

        return redirect(f'/shows/{showID}')
    return redirect('/shows')

def delete(request, showID):
    if request.method == 'POST':
        c = SHOW.objects.get(id=showID)
        c.delete()
    return redirect('/shows')
