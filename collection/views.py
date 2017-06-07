from django.shortcuts import render

def index(request):
    number = 4
    thing = "Thing 1"
    return render(request, 'index.html', {
        'number': number,
        'thing': thing,
    })
