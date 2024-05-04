from django.shortcuts import render
from myceleryproject.celery import add
from .tasks import *
from celery.result import AsyncResult
# Create your views here.

# Enqueue task using delay()
# def index(request):
#     print("results: ")
#     # result1 = add(10,20)
#     result1 = add.delay(10, 20)
#     print(result1)
#     result2 = sub.delay(90, 10)
#     print(result2)
#     # add.delay(10 ,20)
#     return render(request, "myapp/home.html")

# Enqueue task using apply_async()
# def about(request):
#     print("results: ")
#     # result1 = add(10,20)
#     result1 = add.apply_async(args=[10, 20])
#     print(result1)
#     result2 = sub.apply_async(args=[90,10])
#     print(result2)
#     # add.delay(10 ,20)
#     return render(request, "myapp/about.html")


# display addition value after task execution
def index(request):
    result = add.delay(10, 20)
    return render(request, 'myapp/home.html', {'result': result})

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, "myapp/contact.html")

def check_result(request, task_id):
    # retrieve the task result using task id
    result = AsyncResult(task_id)
    print("results: ")
    # print("Ready", result.ready())
    # print("successful", result.successful())
    # print("falied", result.failed())
    # print("Get:", result.get()) # this will block the call
    return render(request, 'myapp/result.html', {'result': result})

