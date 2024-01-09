from django.contrib import admin
from django.urls import path, include
from todo_dev import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_dev.urls')),
]
