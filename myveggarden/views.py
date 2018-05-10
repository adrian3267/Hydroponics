from django.shortcuts import render

# Create your views here.

def overview(request):
    return render(request, 'myveggarden/overview.html')

def home(request):
    return render(request, 'myveggarden/home.html')