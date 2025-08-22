from django.shortcuts import render
from .serializers import *
from .models import * 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import *


# Views for a User crud -> Remove, Update, Insert, Delete 

class CreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Swagger docs for a Post and get Method
    @swagger_auto_schema(
        operation_description='Create a New User', 
        request_body=UserSerializer, 
        responses={
            201: openapi.Response('User Create!', UserSerializer), 
            400: 'Erro to create user :('
        }
    )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Created','data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Erro to create'}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(
        operation_description="List All Users",
        responses={
            200: UserSerializer,
            404: 'Not Found', 
            500: 'Error in Request', 
            }
    )
    
    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateDeleteDetailUser(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description='Get User Detail by ID',
        responses={
            200: UserSerializer,
            404: 'User not found',
        }
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(
        operation_description='Update an existing user (PUT)',
        request_body=UserSerializer,
        responses={
            200: openapi.Response('User updated!', UserSerializer),
            400: 'Invalid data',
            404: 'User not found'
        }
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating user'}, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        operation_description='Partially update an existing user (PATCH)',
        request_body=UserSerializer,
        responses={
            200: openapi.Response('User partially updated!', UserSerializer),
            400: 'Invalid data',
            404: 'User not found'
        }
    )
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Partially Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating user'}, status=status.HTTP_400_BAD_REQUEST)
        

    @swagger_auto_schema(
        operation_description='Delete a user by ID',
        responses={
            204: 'User deleted!',
            404: 'User not found'
        }
    )
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)



# Views for a task crud -> Remove, Update, Insert, Delete 
class CreateTaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        operation_description='Create a new Task',
        request_body=TaskSerializer,
        responses={
            201: openapi.Response('Task created!', TaskSerializer),
            400: 'Error to create task :('
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': 'Error to create'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="List all Tasks",
        responses={
            200: TaskSerializer(many=True),
            404: 'Not Found',
            500: 'Error in Request',
        }
    )
    def get(self, request, *args, **kwargs):
        tasks = self.get_queryset()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateDeleteDetailTask(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        operation_description='Get Task Detail by ID',
        responses={
            200: TaskSerializer,
            404: 'Task not found',
        }
    )
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description='Update an existing task (PUT)',
        request_body=TaskSerializer,
        responses={
            200: openapi.Response('Task updated!', TaskSerializer),
            400: 'Invalid data',
            404: 'Task not found'
        }
    )
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating task'}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Partially update an existing task (PATCH)',
        request_body=TaskSerializer,
        responses={
            200: openapi.Response('Task partially updated!', TaskSerializer),
            400: 'Invalid data',
            404: 'Task not found'
        }
    )
    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Partially Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating task'}, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(
        operation_description='Delete a task by ID',
        responses={
            204: 'Task deleted!',
            404: 'Task not found'
        }
    )
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
    
# Create your views here.
