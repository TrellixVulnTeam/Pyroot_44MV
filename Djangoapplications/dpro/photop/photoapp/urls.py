
from django.contrib import admin
from django.urls import path
from photoapp import views

app_name = 'photoapp'     # for using namespaces 

urlpatterns = [
    path('', views.index, name='index'),  # redirects the url to the view of the photoapp

    # redirects to another view with the matching url which is http://127.0.0.1:8000/photos/1/

    path('<int:Photo_id>/', views.detail, name='detail'),
]
