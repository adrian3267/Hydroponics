from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from authentication.models import *
from django.http import HttpResponseRedirect

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['inputName']
        password = request.POST['inputPassword']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            #Verify user type: Supplier or Embraco's user
            embraco_user = EmbracoProfile.objects.get(user=user.id)
            supplier_user = EmbracoProfile.objects.get(user=user.id)
            if embraco_user: #If it's Embraco's user
                request.session['user_type'] = 'Embraco'
            elif supplier_user: #If it's a Supplier's user
                request.session['user_type'] = 'Supplier'
            else:
                request.session['user_type'] = 'Undefined'
            #End user type verification

            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message
            return HttpResponseRedirect('/auth/login/')
    else:
        return render(request, 'authentication/login.html')

def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')