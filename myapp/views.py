from django.shortcuts import render

def index(request):
    context = {
        'message': 'Hello from Django World!',
        'items': ['Apple', 'Banana', 'Orange', 'Grapes'],
        'author': {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York'
        }
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    context = {'message': 'About page'}  # Context is created HERE
    return render(request, 'myapp/about.html', context)

def contact(request):
    context = {'message': 'Contact page'}  # Context is created HERE
    return render(request, 'myapp/contact.html', context)

