from django.shortcuts import render, redirect

from collection.models import Thing
from collection.forms import ThingForm

def index(request):
    # get all Thing objects from database
    things = Thing.objects.all()

    return render(request, 'index.html', {
        'things': things,
    })

# view for a Thing object
def thing_detail(request, slug):
    thing = Thing.objects.get(slug=slug)
    
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })

'''
    Renders a page with a form that can edit a Thing object.
        - called if user wants to access form or wants to post the form
        - accessing form: creates a form using ThingForm
        - posting form: edits the object if the form is valid, then redirects the user
'''
def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)

    # check if the form is being submitted
    form_class = ThingForm
    if request.method == "POST":
        # grab the data and post it
        form = form_class(data=request.POST, instance=thing)
        
        # save it and redirect back to the detail if it's valid
        if form.is_valid():
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    else:
        # create the form
        form = form_class(instance=thing)
    
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })
