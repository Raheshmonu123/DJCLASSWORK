from django.urls import path,include
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('result/',views.result,name="result"),
    path('logout/', views.logout_view, name='logout'),
     path('login/',views.login_page,name="login")
]