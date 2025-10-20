from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.TodoListCreateCreate.as_view(), name='list'),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()), 
    path('todos/<int:pk>/complete', views.ToDoToggleComplete.as_view()), 
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'), 
]