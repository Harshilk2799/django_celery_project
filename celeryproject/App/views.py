from django.shortcuts import render
from celeryproject.celery import add
from App.tasks import sub
from celery.result import AsyncResult

# Enqueue Task using delay()
# def index(request):
#     # result = add(10,20)
#     # print("Result: ", result)

#     result = add.delay(10,20)
#     print("Result: ", result)

#     result1 = sub.delay(110,20)
#     print("Result: ", result1)
#     return render(request, "app/home.html")


# Enqueue Task using apply_async()
# def index(request):
#     # result = add(10,20)
#     # print("Result: ", result)

#     result = add.apply_async(args = [10,20])
#     print("Result: ", result)

#     result1 = sub.apply_async(args = [110,20])
#     print("Result: ", result1)
#     return render(request, "app/home.html")


# Display addition value after task execution
def index(request):
    result = add.delay(10,20)
    return render(request, "app/home.html", {"result": result})

def about(request):
    return render(request, "app/about.html")

def contact(request):
    return render(request, "app/contact.html")

def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)

    # Attribute
    # print("Result ID: ", result.id)
    # print("Result Task ID: ", result.task_id)
    # print("Result State: ", result.state)
    # print("Result Status: ", result.status)
    # print("Final Result: ", result.result)

    # Methods 
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    # print("Get: ", result.get())
    return render(request, "app/result.html", {"result":result})