from django.utils import timezone
from .models import Todo
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-time')

    return render(request, 'todoapp/index.html', {
        'todo_items': todo_items,
    })


def add_todo(request):
    current_date = timezone.now()
    content = request.POST['content']

    Todo.objects.create(text=content, time=current_date)

    return HttpResponseRedirect("/")


def delete_todo(request, id_todo):
    Todo.objects.get(id=id_todo).delete()

    return HttpResponseRedirect("/")
