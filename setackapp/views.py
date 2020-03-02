from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'setackapp/index.html')

def laundry(request):
    return render(request, 'setackapp/laundry.html')

def contact(request):
    return render(request, 'setackapp/contact.html')