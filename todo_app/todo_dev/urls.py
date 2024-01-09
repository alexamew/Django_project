from django.contrib import admin
from django.urls import path, include
from . import views
from todo_dev.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
	path('update_task/<str:pk>/', views.updateTask, name="update_task"),
	path('delete/<str:pk>/', views.deleteTask, name="delete"),

]

