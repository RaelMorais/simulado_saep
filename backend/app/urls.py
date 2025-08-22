from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import CreateUserView, UpdateDeleteDetailUser, CreateTaskView, UpdateDeleteDetailTask

schema_view = get_schema_view(
   openapi.Info(
      title="API To-Do List Saep",
      default_version='v1',
      description="Documentação da API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('user/', CreateUserView.as_view()), 
    path('user/<int:pk>', UpdateDeleteDetailUser.as_view()), 
    path('task/', CreateTaskView.as_view()), 
    path('task/<int:pk>', UpdateDeleteDetailTask.as_view()), 

    # Swagger Urls configs 
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
