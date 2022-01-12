from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

class ListTodo(generics.ListAPIView): #ListAPIView to display all todos
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodo(generics.RetrieveAPIView): #RetrieveAPIView to to get just one Todo
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer