from django.shortcuts import render , HttpResponse

# Create your views here.

def Home (request):
    return render(request,"index.html")
def About(request):
    return render (request,"about.html")
def Contact(request):
    return render (request,"contact.html")
    
