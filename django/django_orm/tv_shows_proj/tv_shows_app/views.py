from django.shortcuts import render, redirect
from .models import SHOW
from django.contrib import messages

def index(request):
    return redirect('/shows')

def all_shows(request):
    context = {"Shows": SHOW.objects.all()}
    return render(request, 'all_shows.html', context)    

def shows_new(request):
    if request.method == 'GET':
        return render(request, 'show_new.html')
    return redirect('/shows')

# POST
def create(request):
    if request.method == 'POST':
        errors = SHOW.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            SHOW.objects.create(
                title = request.POST['title'],
                network = request.POST['network'],
                description = request.POST['description'],
                release_date = request.POST['release_date']
            )
            return redirect(f'/shows/{SHOW.objects.last().id}')
    return redirect('/shows')

def show_detail(request, showID):
    if request.method == 'GET':
        context = {"Show": SHOW.objects.get(id=showID)}
        return render(request, 'show_detail.html', context)
    return redirect('/shows')

def edit(request, showID):
    if request.method == 'GET':
        context = {"Show": SHOW.objects.get(id=showID)}
        return render(request, 'show_edit.html', context)
    return redirect('/shows')

# POST
def update(request, showID):
    if request.method == 'POST':
        errors = SHOW.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{showID}/edit')
        else:
            c = SHOW.objects.get(id=showID)
            c.title = request.POST['title']
            c.network = request.POST['network']
            c.description = request.POST['description']
            c.release_date = request.POST['release_date']
            c.save()

        return redirect(f'/shows/{showID}')
    return redirect('/shows')

# POST
def delete(request, showID):
    if request.method == 'POST':
        c = SHOW.objects.get(id=showID)
        c.delete()
    return redirect('/shows')
