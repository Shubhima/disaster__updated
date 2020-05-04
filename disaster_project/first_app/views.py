from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Organization
from first_app.models import TypesOfDisaster
from first_app.models import Blog
# Create your views here.
def index(request):
   return HttpResponse('Hello')


def help(request):
    my_dict={}
    return render(request,'help.html',context=my_dict)

def AboutUs(request):
    my_dict={}
    return render(request,'AboutUs.html',context=my_dict)

def Contact(request):
    my_dict={}
    return render(request,'Contact.html',context=my_dict)

def Home(request):
    my_dict={}
    return render(request,'Home.html',context=my_dict)

def LogIn(request):
    my_dict={}
    return render(request,'LogIn.html',context=my_dict)

def adminPannel(request):
    my_dict={}
    return render(request,'adminPannel.html',context=my_dict)

def changePass(request):
    my_dict={}
    return render(request,'changePass.html',context=my_dict)

def editProfile(request):
    my_dict={}
    return render(request,'editProfile.html',context=my_dict)

def helpSupport(request):
    my_dict={}
    return render(request,'helpSupport.html',context=my_dict)

def review(request):
    my_dict={}
    return render(request,'review.html',context=my_dict)


def Dashboard(request):
    my_dict={}
    return render(request,'Dashboard.html',context=my_dict)


def viewOrganization(request):
    o = Organization.objects.all()
    return HttpResponse("org")

def viewBlog(request):
    bl = Blog.objects.all()
    return render(request,"Blog.html",{'bl':bl})

def viewTypesOfDisaster(request):
    tod = TypesOfDisaster.objects.all()
    return render(request,"TypesOfDisaster.html",{'tod':tod})


def Post(request):
    my_dict={}
    return render(request,'Post.html',context=my_dict)


def createPost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                Post=Post()
                Post.title= request.POST.get('title')
                Post.content= request.POST.get('content')
                Post.save()
                
                return render(request, 'Post.html')  

        else:
                return render(request,'Post.html')

