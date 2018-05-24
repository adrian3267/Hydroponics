from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import CertificationForm
from .forms import DeleteCertificationForm
from .forms import GardenForm, GardenSetForm
from .models import Certification
from .models import RequiredCertificationDocuments
from .models import Documents
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
            return HttpResponseRedirect('/certification/')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = GardenForm()
    return render(request, 'certification/certification-new.html', {"form": form})


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
            return HttpResponseRedirect('/certification/')
        
    # if a GET (or any other method) we'll create a blank form
    return render(request, 'certification/change-setpoints.html', {"form": form})



def getParameters(request, pk, template_name = 'certification/certification-new.html'):
    instance = GardenSet.objects.get(id=pk)
    form = GardenSetForm(request.GET or None, instance=instance)
    if request.method == 'POST':
        # check whether it's valid:dj
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect("/certification/")
    return HttpResponse(instance.concentration_set)
                             #+ "/n" + instance.next_cycle_set
#    return render(request, template_name, { "form": form })



@login_required(login_url='/auth/login/')
def editCertification(request, pk, template_name = 'certification/certification-new.html'):
    instance = Certification.objects.get(id=pk)
    form = CertificationForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        # check whether it's valid:dj
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect("/certification/" + str(instance.id) + "/edit2")
    return render(request, template_name, { "form": form })


@login_required(login_url='/auth/login/')
def deleteCertification(request, pk, template_name = 'certification/certification-list.html'):
    new_to_delete = get_object_or_404(Certification, id=pk)
    # +some code to check if this object belongs to the logged in user (Not doing it)

    if request.method == 'POST':
        form = DeleteCertificationForm(request.POST, instance=new_to_delete)

        if form.is_valid():  # checks CSRF
            new_to_delete.delete()
            return HttpResponseRedirect("/certification/")  # wherever to go after deleting

    else:
        form = DeleteCertificationForm(instance=new_to_delete)

    template_vars = {'form': form}
    return render(request, template_name, template_vars)



@login_required(login_url='/auth/login/')
def documentsView(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        instance = Certification.objects.get(id=pk)
        # process the data in form.cleaned_data as required
        item_list = request.POST.getlist('documents_checkboxes[]', None)
        for item in item_list:
            doc_instance = Documents.objects.get(id=item)
            item_obj = RequiredCertificationDocuments(document_type=doc_instance, certification=instance)
            item_obj.save()
        return HttpResponseRedirect('/certification')
    # if a GET (or any other method) we'll create a blank form
    else:
        documents = Documents.objects.all()
    return render(request, 'certification/certification-new2.html', {"documents": documents})


@login_required(login_url='/auth/login/')
def editDocumentsView(request, pk):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        instance = Certification.objects.get(id=pk)
        # process the data in form.cleaned_data as required
        item_list = request.POST.getlist('documents_checkboxes[]', None)
        for item in item_list:
            doc_instance = Documents.objects.get(id=item)
            item_obj = RequiredCertificationDocuments(document_type=doc_instance, certification=instance)
            item_obj.save()
        return HttpResponseRedirect('/certification')
    # if a GET (or any other method) we'll create a blank form
    else:
        documents = Documents.objects.all()
        for doc in documents:
            try:
                if RequiredCertificationDocuments.objects.get(certification=pk, document_type=doc.id):
                       doc.checkbox = "checked"
                       item_delete = RequiredCertificationDocuments.objects.get(certification=pk, document_type=doc.id)
                       #item_delete.delete()
            except RequiredCertificationDocuments.DoesNotExist:
                doc.checkbox = ""

    return render(request, 'certification/certification-new2.html', {"documents": documents})



def overview(request):
    return render(request, 'certification/overview.html')
