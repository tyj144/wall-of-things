from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
# decorator requires that the user be logged in to edit
@login_required
def edit_thing(request, slug):
    thing = Thing.objects.get(slug=slug)

    if thing.user != request.user:
        raise Http404

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

# form for creating thing objects
def create_thing(request):
    form_class = ThingForm
    
    # check if form was already posted
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance of form info but don't save it yet
            thing = form.save(commit=False)

            # set additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)

            # save object
            thing.save()

            # redirect to the thing detail
            return redirect('thing_detail', slug=thing.slug)
    else: 
        form = form_class()
    
    return render(request, 'things/create_thing.html', {
        'form': form,
    })

def browse_by_name(request, initial=None):
    if initial:
        # filters by objects 
        things = Thing.objects.filter(name__istartswith=initial)
        things = things.order_by('name')
    else:
        things = Thing.objects.all().order_by('name')

    return render(request, 'search/search.html', {
        'things': things,
        'initial': initial,
    })
