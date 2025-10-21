from django.shortcuts import render

def forhome(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

