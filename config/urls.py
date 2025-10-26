from django.contrib import admin
from django.urls import path, include
from drapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('aicreate/', views.aiquest_create),
    path('aicreate/<int:pk>/', views.aiquest_create)
]
