from django.shortcuts import render, redirect

def index(request):
    return render(request, "index.html")

def result(request):
    return render(request, "result.html")
    
def takeData(request):
    if request.method == 'POST':
        context = {
            'yourName': request.POST['yourName'],
            'favLanguage': request.POST['favLanguage'],
            'location': request.POST['location'],
            'comment':  request.POST['comment']
        }
        return render(request, "result.html", context)
    return render(request, "result.html")