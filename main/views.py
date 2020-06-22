from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo

# Create your views here.
def home(request):
    items=Todo.objects.all().order_by("-added_date")
    return render(request,'todoapp/index.html/',{"items":items})

@csrf_exempt
def add_to_do(request):
    date=timezone.now()
    content=request.POST['c']
    Todo.objects.create(added_date=date,text=content)
    #print(Todo.objects.all().count())
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request,todo_id):
    print(todo_id)
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
