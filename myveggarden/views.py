from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import GardenForm, GardenSetForm
from .models import Garden, GardenSet


def addMeasure(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GardenForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            savedform = form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/myveggarden/history')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GardenForm()
    return render(request, 'myveggarden/add-measure.html', {"form": form})


def changeSetpoints(request):
    instance = GardenSet.objects.get(id=1)
    form = GardenSetForm(request.POST or None, instance=instance)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            savedform = form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/myveggarden/history')

    # if a GET (or any other method) we'll create a blank form
    return render(request, 'myveggarden/change-setpoints.html', {"form": form})


def getSetpoints(request, pk, template_name='certification/certification-new.html'):
    instance = GardenSet.objects.get(id=pk)
    form = GardenSetForm(request.GET or None, instance=instance)
    if request.method == 'POST':
        # check whether it's valid:dj
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect("/history/")
    return HttpResponse(instance.concentration_set)
    # + "/n" + instance.next_cycle_set


#    return render(request, template_name, { "form": form })


def overview(request):
    garden_obj = Garden.objects.all().order_by("-id")[:1]
    #garden_obj = Garden.objects.get(id=1)
    return render(request, 'myveggarden/overview.html', { "garden_obj": garden_obj })

def home(request):
    return render(request, 'myveggarden/home.html')
