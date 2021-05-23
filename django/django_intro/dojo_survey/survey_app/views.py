from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    return render(request, "result.html")
    
def takeData(request):
    if request.method == 'POST':
        request.session['yourName']    = request.POST['yourName']
        request.session['favLanguage'] = request.POST['favLanguage']
        request.session['location']    = request.POST['location']
        request.session['comment']     = request.POST['comment']
    return redirect('/result')