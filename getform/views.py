from django.shortcuts import render

def home(request):
    
    return render(request, 'home.html')

def result(request):
    
    username = request.GET.get('username', 'Guest')
    full_data = request.GET 
    return render(request, 'result.html', {'username': username, 'data': full_data})
