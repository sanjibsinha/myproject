from django.shortcuts import render

def index(request):
    context = {'message': 'Hello from Django!'}  # Context is created HERE
    return render(request, 'myapp/index.html', context)