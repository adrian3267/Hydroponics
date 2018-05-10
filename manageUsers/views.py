from django.shortcuts import render
from django.core.urlresolvers import reverse
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def manageUsers(request, action='list_supplier_users'):
    if request.session['user_type'] == 'Embraco':
        embraco_users_enabled = EmbracoProfile.objects.get(user=request.user).is_administrator
        if request.method == 'POST':
            action = request.POST['action']
    else:
        embraco_users_enabled = False

    # Get contents based on action value
    if action == 'list_embraco_users' and embraco_users_enabled:
        user_list_type = 'embraco'
        user_list = EmbracoProfile.objects.all()
    else:
        user_list_type = 'supplier'
        user_list = SupplierProfile.objects.all()
    # Returns view to user
    return render(request,
                  'manageUsers/manage-users.html',
                  {
                      "embraco_users_enabled": embraco_users_enabled,
                      "user_list_type": user_list_type,
                      "user_list": user_list,
                  })

@login_required(login_url='/auth/login/')
def editEmbracoUser(request, pk, template_name = 'manageUsers/embraco_user_edit.html'):
    instance = EmbracoProfile.objects.get(id=pk)
    user_form = UserForm(request.POST or None, instance=instance.user)
    embraco_user_form = EmbracoUserForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        # check whether it's valid:dj
        if user_form.is_valid() and embraco_user_form.is_valid():
            # process the data in form.cleaned_data as required
            updated_user = user_form.save()
            updated_embraco_user = embraco_user_form.save(commit=False)
            updated_embraco_user.user = updated_user
            updated_embraco_user.save()
            # redirect to a new URL:
            url = reverse('manage-users-embraco', kwargs={'action': 'list_embraco_users'})
            return HttpResponseRedirect(url)
    return render(request, template_name, { "user_form": user_form , "embraco_user_form": embraco_user_form,})

@login_required(login_url='/auth/login/')
def editSupplierUser(request, pk, template_name = 'manageUsers/supplier_user_edit.html'):
    instance = SupplierProfile.objects.get(id=pk)
    user_form = UserForm(request.POST or None, instance=instance.user)
    supplier_user_form = SupplierUserForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        # check whether it's valid:dj
        if user_form.is_valid() and supplier_user_form.is_valid():
            # process the data in form.cleaned_data as required
            updated_user = user_form.save()
            updated_supplier_user = supplier_user_form.save(commit=False)
            updated_supplier_user.user = updated_user
            updated_supplier_user.save()
            # redirect to a new URL:
            url = reverse('manage-users')
            return HttpResponseRedirect(url)
    return render(request, template_name, { "user_form": user_form , "supplier_user_form": supplier_user_form,})

@login_required(login_url='/auth/login/')
def createEmbracoUser(request, template_name = 'manageUsers/embraco_user_edit.html'):
    user_form = UserForm(request.POST or None)
    embraco_user_form = EmbracoUserForm(request.POST or None)
    if request.method == 'POST':
        # check whether it's valid:dj
        if user_form.is_valid() and embraco_user_form.is_valid():
            # process the data in form.cleaned_data as required
            created_user = user_form.save()
            created_embraco_user = embraco_user_form.save(commit=False)
            created_embraco_user.user = created_user
            created_embraco_user.save()
            # redirect to a new URL:
            url = reverse('manage-users-embraco', kwargs={'action': 'list_embraco_users'})
            return HttpResponseRedirect(url)
    return render(request,template_name, {"user_form": user_form, "embraco_user_form": embraco_user_form })

@login_required(login_url='/auth/login/')
def createSupplierUser(request, template_name = 'manageUsers/supplier_user_edit.html'):
    user_form = UserForm(request.POST or None)
    supplier_user_form = SupplierUserForm(request.POST or None)
    if request.method == 'POST':
        # check whether it's valid:dj
        if user_form.is_valid() and supplier_user_form.is_valid():
            # process the data in form.cleaned_data as required
            created_user = user_form.save()
            created_supplier_user = supplier_user_form.save(commit=False)
            created_supplier_user.user = created_user
            created_supplier_user.save()
            # redirect to a new URL:
            url = reverse('manage-users')
            return HttpResponseRedirect(url)
    return render(request, template_name, {"user_form": user_form, "supplier_user_form": supplier_user_form })
