from django.shortcuts import render

def index(request):
    context ={
        'title':'Home',
        'heading': 'Selamat Datang',
        'subheading': 'di website kuntuludun'
    }
    return render(request, 'index.html', context)