from django.urls import path
from . import views
urlpatterns = [
    path('simpleapi',views.simpleapi,name='simple_api')
]