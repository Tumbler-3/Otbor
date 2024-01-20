from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from Tasks.models import Task
from Tasks.serializers import TaskSerializer

# Create your views here.

class TasksView(ReadOnlyModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def get_response(self,request):
        pass
    