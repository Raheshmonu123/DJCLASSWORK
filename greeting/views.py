'''from django.shortcuts import render

def forhome(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')'''
    
    
from django.shortcuts import render


def greeting(request):
    my_objects = [
        {'name': 'John', 'job':'WB' , 'salary': 10000,'time': 'full-time'},
        {'name': 'Jane', 'job': 'AP', 'salary': 15000, 'time': 'part-time'},
        {'name': 'Bob', 'job': 'SE', 'salary': 20000, 'time': 'full-time' },
        {'name': 'Alice', 'job': 'DS', 'salary': 25000, 'time': 'full-time' }
    ]
    context = {'my_objects': my_objects}
    return render(request, 'index.html', context)

