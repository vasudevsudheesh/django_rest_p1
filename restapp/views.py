from .serializers import TaskSerializers, UserSerializer
from rest_framework import viewsets
from .models import Task
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_created')
    serializer_class = TaskSerializers


class DueTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(completed=False).order_by('-date_created')
    serializer_class = TaskSerializers


class CreateUserview(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class CompletedTaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.filter(completed=True).order_by('-date_created')
    serializer_class = TaskSerializers
