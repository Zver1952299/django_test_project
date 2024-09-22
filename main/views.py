from django.shortcuts import render


def index(request):
    data = {
        'title': '192272',
        'list': ['Adam', 'Eva', 'Mary', 'Tom']
    }
    return render(request, 'main/index.html', {'data': data})


def about(request):
    return render(request, 'main/about.html')
