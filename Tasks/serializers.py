from rest_framework import serializers
from Tasks.models import Task


class TaskSerializer(serializers.ModelField):
     class Meta:
         model = Task
    

