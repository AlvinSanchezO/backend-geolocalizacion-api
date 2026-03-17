from django.shortcuts import render

def home(request):
    context = {
        "message": "Welcome to the admin home page!"
    }
    return render(request, 'index.html', context)
