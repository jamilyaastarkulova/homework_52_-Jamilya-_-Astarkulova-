from django.urls import path
from webapp.views import index_view, todo_create_view, todo_view, todo_delete_view

urlpatterns = [
    path('', index_view, name='todo_list'),
    path('todo/add/', todo_create_view, name='todo_create'),
    path('todo/<int:pk>/', todo_view, name='todo_view'),
    path('todo/<int:pk>/delete/', todo_delete_view, name='todo_delete'),
]