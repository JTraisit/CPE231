from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def Home(request):
    return render(request,'Home.html')
    
def AboutAs(request):
    return render(request,'AboutAs.html')

def book(request):
    return render(request,'Book.html')