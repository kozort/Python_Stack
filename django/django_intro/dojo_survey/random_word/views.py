from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string


def random_word(request):
    if not 'attempt_count' in request.session:
        print("entered if to create new KEYS")
        request.session['attempt_count'] = 0
        request.session['random_word'] = ""
    context = {
        'attempt_count': request.session['attempt_count'],
        'random_word': request.session['random_word']
    }
    return render(request, "random_word.html", context)

def generate(request):
    print("entered generate")
    print(request.session['attempt_count'])
    print(request.session['random_word'])
    if request.method == 'POST':
        print("entered if POST")
        request.session['attempt_count'] += 1
        request.session['random_word'] = get_random_string(length=14)
    return redirect('/random_word')

def reset(request):
    request.session['attempt_count'] = 0
    request.session['random_word'] = ""
    return redirect('/random_word')
    
