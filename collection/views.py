from django.shortcuts import render
from collection.models import Thing

def index(request):
    # get all Thing objects from database
    things = Thing.objects.all()

    return render(request, 'index.html', {
        'things': things,
    })
