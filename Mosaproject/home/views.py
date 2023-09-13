from multiprocessing import context
from django.shortcuts import redirect, render
from home.models import registerMosa
from home.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from home.models import contact


# Create your views here.
def home(request):
    #return HttpResponse('This is my home (/)')
    return render(request, 'home.html')
def event(request):
    #return HttpResponse('This is my members (/)')
    return render(request, 'event.html')
def Signin(request):

    #return HttpResponse('This is my members (/)')
    return render(request, 'Signin.html')
def register(request):
    if request.method == "POST":
        Username =request.POST["Username"]
        firstName =request.POST["firstName"]
        lastName =request.POST["lastName"]
        email =request.POST["email"]
        password =request.POST["password"]
        phoneNumber =request.POST["phoneNumber"]
        nationality =request.POST["nationality"]
        religion =request.POST["religion"]
        homeAddress =request.POST["homeAddress"]
        occupation =request.POST["occupation"]
        institution =request.POST["institution"]
        stateOfOrigin=request.POST["stateOfOrigin"]

        Register = registerMosa( Username=Username, firstName=firstName, lastName=lastName, email=email, password=password, phoneNumber=phoneNumber, nationality=nationality, religion=religion, homeAddress=homeAddress, occupation=occupation, stateOfOrigin=stateOfOrigin, institution=institution)
        Register.save()

        messages.success(request, "Your Registration was succcessful")
        return redirect("dues")
    #return HttpResponse('This is my members (/)')
    return render(request, 'register.html')
def blogs(request):
    #return HttpResponse('This is my blog (/)')
    return render(request, 'blogs.html')

def dues(request):
    #return HttpResponse('This is my blog (/)')
    return render(request, 'dues.html')
def contact(request):
    if request.method == "POST":
        firstName =request.POST["firstName"]
        lastName =request.POST["lastName"]
        emailAddress =request.POST["emailAddress"]
        desc =request.POST["desc"]

        Contact=contact_View(firstName=firstName, lastName=lastName, emailAddress=emailAddress, desc=desc )
        Contact.save()
    #return HttpResponse('This is my contact (/)')
    return render(request, 'contact.html')
def members(request):
    allregisterMosa = registerMosa.objects.all()
    context = {'members': allregisterMosa}
    #return HttpResponse('This is my Login (/)')
    return render(request, 'members.html', context)

