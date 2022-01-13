from django.urls import path
from maketodo import views

app_name = 'maketodo'

urlpatterns = [
    path('listtodo/', views.currenttodo, name='currenttodo'),
    path('completed/', views.completetodos, name='completetodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.completetodo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name='deletetodo'),
    path('', views.home, name='home'),
    path('create/', views.createtodo, name='createtodo'),
]
