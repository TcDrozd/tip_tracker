from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Tip_Entry, Tip_Type
from .forms import Tip_Form

# Create your views here.

def index(request):
    """ The homepage for tip tracker """
    return render(request, 'tip_tracker_app/index.html')

@login_required
def entries(request):
    """ Each individual tip logged """
    entries = Tip_Entry.objects.filter(owner=request.user).order_by('date_added')
    context = {'entries':entries}
    return render(request, 'tip_tracker_app/entries.html', context)

@login_required
def types(request):
    """ Show both types """
    types = Tip_Type.objects.all()
    context={'types':types}
    return render(request, 'tip_tracker_app/types.html', context)

@login_required
def type(request, type_id):
    """ Show a single type of tip and all its entries (cash/CC) """
    entries = Tip_Entry.objects.filter(owner=request.user, id=type_id).order_by('date_added')
    type = Tip_Type.objects.get(id=type_id)

    context = {'type':type, 'entries':entries}
    return render(request, 'tip_tracker_app/type.html', context)

@login_required
def new_entry(request):
    """ Enter a new tip log """
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = Tip_Form()
    else:
        # POST the submitted data
        form = Tip_Form(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('tip_tracker_app:types'))
    context = {'form':form}
    return render(request, 'tip_tracker_app/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """ Edit an existing Entry """
    entry = Tip_Entry.objects.get(id=entry_id)
    type = entry.type

    if request.method != 'POST':
        # Initial request, prefill the form
        form = Tip_Form(instance=entry)
    else:
        # POST the new data submitted
        form = Tip_Form(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tip_tracker_app:type', args=[type.id]))
    context = {'entry':entry, 'type':type, 'form':form}
    return render(request, 'tip_tracker_app/edit_entry.html', context)
