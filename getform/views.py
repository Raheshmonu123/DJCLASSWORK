from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def home(request):
    
    return render(request, 'home.html')

def result(request):
    
    username = request.GET.get('username', 'Guest')
    full_data = request.GET 
    return render(request, 'result.html', {'username': username, 'data': full_data})


def signup_page(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            # Redirect to login page after successful signup
            return HttpResponse("user created successfully")
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form})




def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            user = form.get_user()
            login(request, user)
            # Redirect to home page after successful login
            print(request.COOKIES,request.POST)
            
            return HttpResponse("logged in successfully")
           
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)