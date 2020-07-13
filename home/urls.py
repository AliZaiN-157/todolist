from django.contrib import admin
from django.urls import path, include
from home import views
from home.views import deleteTodoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView, name='delete'),

]
