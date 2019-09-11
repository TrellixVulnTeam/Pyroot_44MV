from django.shortcuts import render
from rest_framework import viewsets     # viewing the model data
from .serializers import TaskSerializers, UserSerializers  # to have the data in json output
from .models import Task                 # data source
from django_filters.rest_framework import DjangoFilterBackend  # for filter backend
from rest_framework import filters                             # for filter
from rest_framework.permissions import IsAuthenticated, AllowAny  # to authenticate and allow to view
# allow anyone to register

from django.contrib.auth import get_user_model                 # for the user
from rest_framework.generics import CreateAPIView              # Create the API view

# Create your views here.
# Displays the api data contents here


class TaskViewSet(viewsets.ModelViewSet):  # default viewset
    permission_classes = (IsAuthenticated,)                  # to check the authentication
    queryset = Task.objects.all().order_by('-date_created')  # data returned by the query
    serializer_class = TaskSerializers                       # json converter

#   using filters - backend, ordering, searching
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)

    # filtering ,ordering, searching
    filter_fields = ('completed',)               # filtering based on the completed field
    ordering = ('-date_created',)                # ordering based on date_created
    search_fields = ('task_name',)               # searching based on the task_name field

# without filters

# class TaskViewSetDue(viewsets.ModelViewSet):  # viewset for the uncompleted tasks
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=False)
#     serializer_class = TaskSerializers
#
#
# class TaskViewSetCompleted(viewsets.ModelViewSet):  # viewset for the completed tasks
#     queryset = Task.objects.all().order_by('-date_created').filter(completed=True)
#     serializer_class = TaskSerializers

# API view


class CreateUserView(CreateAPIView):
    model = get_user_model()
    serializer_class = UserSerializers
    permission_classes = AllowAny
