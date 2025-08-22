from rest_framework import serializers
from .models import *

# Serializer for a User, transforming in model to json or model to json 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

# Serializer for a Task, transforming in model to json or model to json 
class TaskSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id', 
            'description', 
            'name_class', 
            'priority', 
            'register_date', 
            'status', 
            'user', 
            'user_name'
        ]