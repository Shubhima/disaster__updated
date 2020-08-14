from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Organization
from first_app.models import TypesOfDisaster
from first_app.models import Blog
from first_app.models import Review
from first_app.models import HelpSupport
from first_app.models import Register
from first_app.models import ContactUs
from first_app.models import Subscribe
from first_app.models import Notify 
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth import update_session_auth_hash
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import gmplot
from io import BytesIO
import io
import base64
from PIL import Image, ImageDraw
import PIL, PIL.Image
from django.conf import settings
from django.core.mail import send_mail
import numpy as np
import time
import datetime
import os
import pickle
from dateutil.parser import parse
import time as timelibrary

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
    if request.method=='POST':
        if request.POST.get('nm') and request.POST.get('e') and request.POST.get('msg') and request.POST.get('ph'):
            Post=ContactUs()
            Post.Name= request.POST.get('nm')
            Post.Email= request.POST.get('e')
            Post.Message= request.POST.get('msg')
            Post.PhoneNo= request.POST.get('ph')
            Post.save()
            
            return render(request,'Contact.html')
    else:
            return render(request,'Contact.html')


def Base(request):
    my_dict={}
    return render(request,'Base.html',context=my_dict)

def SubsAdmin(request):
    my_dict={}
    return render(request,'SubsAdmin.html',context=my_dict)

def Home(request):
    my_dict={}
    return render(request,'Home.html',context=my_dict)


def adminPannel(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    userdetail= Register.objects.get(Email=request.session['email'])
    return render(request,'adminPannel.html',{'user':userdetail})

def changePass(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn/')
    if request.method=='POST':
        reg=Register.objects.get(Email=request.session['email'])
        password=request.POST.get('opassword')
        newpwd=request.POST.get('npassword')
        confirmpwd=request.POST.get('rpassword')
        print("old password", password)      
        print(newpwd)
        print(confirmpwd)
        if(newpwd==confirmpwd):
            p=reg.Pass
            print("db password",p)
            if(password==p):
                reg.Pass=newpwd
                reg.save()
                rest="Password Changed"
                print("Password updated")
                return render(request,'changePass.html',{'rest':rest})
            else:
                print("Password not updated")
                res="Invalid current password"
                return render(request,'changePass.html',{'res':res})
        else:
            res="Confirm password and new password don't match"
            return render(request,'changePass.html',{'res':res})
    else:
        return render(request,'changePass.html')

def editProfile(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    userdetail= Register.objects.get(Email=request.session['email'])
    if request.method == 'POST':
        detail=Register.objects.get(Email=request.POST.get('em'))
        detail.Name = request.POST.get('nm')
        detail.Email = request.POST.get('em')
        detail.save()
        data=Register.objects.get(Email=request.session['email'])
        return render(request,'Base.html',{'us':data})
    else:
        return render(request,'editProfile.html',{'us':userdetail})



def NewRegister(request):
    print("newsregister")
    em=request.POST.get('mail')
    s=Register.objects.filter(Email=em)
    if (len(s)>0):
        err="You are already registered with this email."
        return render(request,'LogIn.html',{'err':err})
    else:
        pass1=request.POST.get('pass')
        cpass=request.POST.get('cpass')
        if pass1==cpass:
            Post=Register()
            Post.Name= request.POST.get('name')
            Post.Email= request.POST.get('mail')
            Post.Pass= request.POST.get('pass')
            
            Post.save()
            us="Thanks for registering with us"
            return render(request,'LogIn.html',{'us':us})
        else:
            ch="The password confirmation does not match."
            return render(request,'LogIn.html',{'ch':ch})




def NewLogin(request):
    if request.method=='POST':
        formpost=True
        us=request.POST.get('n')
        pw=request.POST.get('p')
        errormessage=""
        expert = Register.objects.filter(Email=us, Pass=pw)
        k=len(expert)
        if k>0:
            print("Valid credentials")
            request.session['email']=us
            return render(request,'Base.html',{})
        else:
            print("Invalid credentials")
            errormessage="Invalid credentials"
            return render(request,'LogIn.html', {'formpost': formpost})
    else:
        formpost=False
        return render(request,'LogIn.html', {'formpost': formpost})


def helpSupport(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method=='POST':
        if request.POST.get('txt') and request.POST.get('tarea'):
            Post=HelpSupport()
            Post.Subject= request.POST.get('txt')
            Post.Message= request.POST.get('tarea')
            Post.save()
            
            return render(request,'helpSupport.html')
    else:
            return render(request,'helpSupport.html')

def review(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method=='POST':
        if request.POST.get('txt') and request.POST.get('tarea'):
            Post=Review()
            Post.Subject= request.POST.get('txt')
            Post.Message= request.POST.get('tarea')
            Post.save()
            
            return render(request,'review.html')
    else:
            return render(request,'review.html')


def logout(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    del request.session['email']
    return redirect('/LogIn')

def Dashboard(request):
    my_dict={}
    return render(request,'Dashboard.html',context=my_dict)


def viewOrganization(request):
    o = Organization.objects.all()
    return render(request,"organization.html",{'o':o})

def viewOrganizationdetail(request,id):
    o = Organization.objects.get(id=id)
    return render(request,"viewOrganizationdetail.html",{'o':o})

def viewBlog(request):
    bl = Blog.objects.all()
    return render(request,"Blog.html",{'bl':bl})

def viewBlogdetail(request,id):
    bl = Blog.objects.get(id=id)
    return render(request,"viewBlogdetail.html",{'bl':bl}) 

def viewTypesOfDisaster(request):
    tod = TypesOfDisaster.objects.all()
    return render(request,"TypesOfDisaster.html",{'tod':tod})

def viewTypesOfDisasterdetail(request,id):
    tod = TypesOfDisaster.objects.get(id=id)
    return render(request,"viewTypesOfDisasterdetail.html",{'tod':tod})


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

def fileUpload(request):
    if request.method=='POST':
        f = request.FILES['sentFile']
        handle_uploaded_file(f,f.name)
        return HttpResponse(f.name)
    else :
        return  render (request,'fileUpload.html',{})


def handle_uploaded_file(f,name):
    destination = open(name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()


def NatDisV(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'NatDisV.html',context=my_dict)

def NatDisVDynamic(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        print(x)
        fig=plt.figure(figsize=(8, 9), dpi=80,facecolor='w', edgecolor='w')
        

        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('natural-disasters-by-type.csv')
        df=df.drop(2,axis=0)
        df1=(df[(df['Entity']==x)])
        df1=df1.set_index('Year')
        a=str(df1.iloc[0,0])
        if x=='Earthquake' or x=="All natural disasters" or x=="Extreme weather":
            df1.iloc[70:,2].plot.bar(title=' Reported disaster is ' +a,figsize=(6,5))
        elif x=="Mass movement (dry)" or x=="Storm":
            df1.iloc[:20,2].plot.bar(title=' Reported disaster is ' +a,figsize=(6,5))
        else:
            df1.iloc[40:,2].plot.bar(title=' Reported disaster is ' +a,figsize=(6,5))
        plt.ylabel('No. of reported disasters')
        #plt.xlabel('Year')
        xlab = plt.xlabel("year")
        xlab.set_position((0.5, 0.5))
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
        
    else :
        return render(request,'NatDisVDynamic.html')


def YearCountNatDisV(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        t=int(request.POST.get('txt'))
        print(x)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('natural-disasters-by-type.csv')
        df=df.drop(2,axis=0)
        msg=1
        df1=(df[(df['Entity']==x)])
        df1=(df1[(df1['Year']==t)])
        print("rows",df1.shape)
        if df1.shape[0]==0:
            msg="Not enough data to plot "
            msg=0
            print("no dat to plot")
            return render(request, 'graphic1.html',{'msg':msg})
        else:
            msg=1
            df1=df1.set_index('Year')
            a=df1.iloc[0,0]
            df1.iloc[:20,2].plot.bar(title=' Reported disasters is ' +a,figsize=(6,5))
            plt.ylabel('No. of reported disasters')
            plt.xlabel('Year')
            buf = io.BytesIO()
            plt.margins(0.8)
            df1.iloc[:,2].plot.bar(title=' ' +a,figsize=(6,5))
            # Tweak spacing to prevent clipping of tick-labels
            plt.subplots_adjust(bottom=0.35)
            plt.savefig(buf, format='png',)
    
            fig.savefig('abc.png')
        
            plt.close(fig)
            image = Image.open("abc.png")
            draw = ImageDraw.Draw(image)
        
            image.save(buf, 'PNG')
            content_type="Image/png"
            buffercontent=buf.getvalue()


            graphic = base64.b64encode(buffercontent) 
            return render(request, 'graphic1.html', {'msg':msg,'graphic1': graphic.decode('utf8')})
        
    else :
        return render(request,'YearCountNatDisV.html')
        
    

def TwoDisasYear(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        y=request.POST.get('dt')
        t=int(request.POST.get('txt'))
        print(x)
        print(y)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('natural-disasters-by-type.csv')
        df=df.drop(2,axis=0)
        df1=df[df["Entity"].isin([x,y])]
        df1=(df1[df1["Year"]==t])
        df1=df1.set_index('Entity')
        a=str(df1.iloc[0,1])
        df1.iloc[:,2].plot.bar(title='Reported Disasters in ' +a,figsize=(6,5))
        plt.ylabel('No. of reported disasters')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
        
    else :
        return render(request,'TwoDisasYear.html')


def MinNatDis(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('natural-disasters-by-type.csv')
        df=df.drop(2,axis=0)
        df=(df[df['Year']==x])
        df=df[df['Number of reported natural disasters (reported disasters)']!=0]
        m2=df.iloc[:,3].min()
        df=(df[df['Number of reported natural disasters (reported disasters)']==m2])
        print(df.dtypes)
        df=df.set_index('Entity')
        df=df.iloc[:,2]
        df=pd.DataFrame(df)
        a=df.index[0]
        df.iloc[0,:].plot.bar(rot=360, figsize=(5,5),title=" Minimum disasters reported in "+str(x))
        plt.xlabel(a)
        plt.ylabel('No. of reported disasters')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MinNatDis.html')


def MaxNatDis(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('natural-disasters-by-type.csv')
        df=df.drop(2,axis=0)
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Number of reported natural disasters (reported disasters)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Maximum disasters reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('No. of reported disasters')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MaxNatDis.html')

def Top5NatDis(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('natural-disasters-by-type.csv')
        df=df.drop(2,axis=0)
        df=(df[df['Year']==x])
        df=df.set_index('Entity')
        df=df.sort_values(by='Number of reported natural disasters (reported disasters)',ascending=False)
        df.iloc[0:5,2].plot.bar(title='Top 5 countries caused disasters reported in '+str(x),figsize=(6,5),rot=360)
        plt.ylabel('No. of reported disasters')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
        
    else :
        return render(request,'Top5NatDis.html')

def DeathNatDis(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'DeathNatDis.html',context=my_dict)

def DirDisGdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'DirDisGdp.html',context=my_dict)

def Global(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'Global.html',context=my_dict)

def GlobPreci(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'GlobPreci.html',context=my_dict)



def Map(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method=='POST':
            m=request.POST.get('mag')
            print(m)
            
            df = pd.read_csv('database.csv',engine='python')
            ctype={
                    'Latitude':float,
                    'Longitude':float
                }
            
            df=df.astype(ctype)
            df=df[df.Magnitude>8]
            latitude_list=df.iloc[:,2].values
            longitude_list=df.iloc[:,3].values
            latitude_list[0]
            longitude_list[0]
            print(latitude_list)
            l_list =[latitude_list[0],latitude_list[1],latitude_list[2],latitude_list[3],latitude_list[4]]
            long_list=[longitude_list[0],longitude_list[1],longitude_list[2],longitude_list[3],longitude_list[4]]
            gmap3 = gmplot.GoogleMapPlotter(l_list[0], long_list[0], 5)
            gmap3.heatmap(latitude_list, longitude_list)
            gmap3.scatter(latitude_list, longitude_list, c='r', marker=True)     
            gmap3.draw("template/map12.html")
            
            return render(request,'map12.html')
    else:
            return render(request,'Map.html')


def VolcaMap(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method=='POST':
            m=request.POST.get('mag')
            print(m)
            
            df = pd.read_csv('Volcanic.csv',engine='python')
            latitude_list=df.iloc[:,7].values
            longitude_list=df.iloc[:,8].values
            latitude_list[0]
            longitude_list[0]
            print(latitude_list)
            l_list =[latitude_list[0],latitude_list[1],latitude_list[2],latitude_list[3],latitude_list[4]]
            long_list=[longitude_list[0],longitude_list[1],longitude_list[2],longitude_list[3],longitude_list[4]]
            gmap3 = gmplot.GoogleMapPlotter(l_list[0], long_list[0], 5)
            gmap3.heatmap(latitude_list, longitude_list)
            gmap3.scatter(latitude_list, longitude_list, c='r', marker=True)     
            gmap3.draw("template/map13.html")
            
            return render(request,'map13.html')
    else:
            return render(request,'VolcaMap.html')

def GlobPreciDynamic(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        t=request.POST.get('txt')
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('breastcancer.csv')
        df[[t]].boxplot()
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphic.html', {'graphic': graphic.decode('utf8')})
        
    else :
        return render(request,'GlobPreciDynamic.html')


def place(request):

    my_dict={}
    return render(request,'place.html',context=my_dict)

def subscribe(request):
    if request.method == 'POST':
        
        e=Subscribe()
        e.Email= request.POST.get('ema')
        e.save()
        em=request.POST.get('ema')
        user=Subscribe.objects.filter(Email=em)
        if(len(user)>0):
           # pw=user[0].Pass
            subject="Welcome!"
            message="Thanks for subscribing to our newsletter. You've been added to our list and will hear form us soon. "
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list )  
            us="Thank you for subscribing."
            return render(request,'Contact.html',{'us':us})
        else:
            res="! This email id is not valid"
            return render(request,'Contact.html',{'res':res})
    else:
        return render(request,'contact.html')
        


def Users(request):
    ul = Subscribe.objects.all()
    return render(request,"Users.html",{'ul':ul}) 

def SendNot(request):
    
    if request.method=='POST':
        
        if request.POST.get('txt') and request.POST.get('tarea'):
            Post=Notify()
            Post.Subject= request.POST.get('txt')
            Post.Message= request.POST.get('tarea')
            Post.save()
            subject=request.POST.get('txt')
            message= request.POST.get('tarea')
            email= request.POST.get('email')
            print("email",email)
            em=request.POST.get('email')
            user=Register.objects.all()
            
            for s in user:
                print(s.Email)
                em=s.Email
                
                email_from=settings.EMAIL_HOST_USER
                recipient_list=[em,]
                send_mail(subject,message,email_from,recipient_list )  
                rest="Notification sent. Please Check" 
                print("mail sent")
                return render(request,'NotificationSent.html',{'rest':rest})
            else:
                res="! Not subscribed with this email id."
                return render(request,'SendNot.html',{'res':res})
            
        return render(request,'SendNot.html')
    else:
            return render(request,'SendNot.html')

    #return render(request,"SendNot.html")

def NotificationSent(request):
    my_dict={}
    return render(request,'NotificationSent.html',context=my_dict)

def LoginAdmin(request):
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username , password=password)
        if user:
            
                login(request,user)
                #return HttpResponseRedirect(reverse('index'))
                #return HttpResponse("Login Sucessful ")
                return render(request,'SubsAdmin.html',{})

           
        else:
            print("some one tried to login and failed")
            print("username :{} and password {}".format(username,password))
            return HttpResponse("invalid details Provided ")
    else:
          
        return render(request,'LoginAdmin.html')

def logoutAdmin(request):
    if not request.session.has_key('email'):
        return redirect('/LoginAdmin')
    del request.session['email']
    return redirect('/LoginAdmin')

def Forgot(request):
    if request.method == 'POST':
        email= request.POST.get('email')
        print("email",email)
        em=request.POST.get('email')
        user=Register.objects.filter(Email=em)
        if(len(user)>0):
            pw=user[0].Pass
            subject="Password"
            message="Welcome to . Your Password is "+pw
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em,]
            send_mail(subject,message,email_from,recipient_list )  
            rest="Your Password sent to your respective Email Account. Please Check" 
            return render(request,'Forgot.html',{'rest':rest})
        else:
            res="! This email id is not registered"
            return render(request,'Forgot.html',{'res':res})
    else:
        return render(request,'Forgot.html')     
    

def DynamicVisual(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'DynamicVisual.html',context=my_dict)

def DathDynamic(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'DathDynamic.html',context=my_dict)
    
def DgdpDynamic(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'DgdpDynamic.html',context=my_dict)

def Globalgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'Globalgdp.html',context=my_dict)

def InternalDisDynamic(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    my_dict={}
    return render(request,'InternalDisDynamic.html',context=my_dict)

def DeathCoun(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('deaths-natural-disasters-ihme.csv')
        df1=(df[(df['Entity']==x)])
        df1=df1.set_index('Year')
        a=str(df1.iloc[0,0])
        df1.iloc[:,2].plot.bar(title=' Deaths in ' +a,figsize=(6,5))
        plt.ylabel('Number of deaths')
        plt.xlabel('Year')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicDeath.html', {'graphicDeath': graphic.decode('utf8')})
        
    else :
        return render(request,'DeathCoun.html')

def YearDeath(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        t=int(request.POST.get('txt'))
        print(x)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('deaths-natural-disasters-ihme.csv')
        
        df1=(df[(df['Entity']==x)])
        df1=(df1[(df1['Year']==t)])
        df1=df1.set_index('Year')
        a=df1.iloc[0,0]
        df1.iloc[:20,2].plot.bar(title=' Deaths in ' +a,figsize=(6,5))
        plt.ylabel('Number of deaths')
        plt.xlabel('Year')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicDeath.html', {'graphicDeath': graphic.decode('utf8')})
        
    else :
        return render(request,'YearDeath.html')


def twoCountDeath(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        y=request.POST.get('dt')
        t=int(request.POST.get('txt'))
        print(x)
        print(y)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('deaths-natural-disasters-ihme.csv')
        
        df1=df[df["Entity"].isin([x,y])]
        df1=(df1[df1["Year"]==t])
        df1=df1.set_index('Entity')
        a=str(df1.iloc[0,1])
        df1.iloc[:20,2].plot.bar(title=' Deaths in ' +a,figsize=(6,5))
        plt.ylabel('Number of deaths')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicDeath.html', {'graphicDeath': graphic.decode('utf8')})
        
    else :
        return render(request,'twoCountDeath.html')

def MaxDeath(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('deaths-natural-disasters-ihme.csv')
        df=df.drop(2,axis=0)
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number) (deaths)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Maximum deaths reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Number of deaths')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicDeath.html', {'graphicDeath': graphic.decode('utf8')})
        
    else :
        return render(request,'MaxDeath.html')


def MinDeath(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('deaths-natural-disasters-ihme.csv')
      
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number) (deaths)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Minimum deaths reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Number of deaths')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicDeath.html', {'graphicDeath': graphic.decode('utf8')})
        
    else :
        return render(request,'MinDeath.html')

def Top5Death(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('deaths-natural-disasters-ihme.csv')
       
        df=(df[df['Year']==x])
        df=df.set_index('Entity')
        df=df.sort_values(by='Deaths - Exposure to forces of nature - Sex: Both - Age: All Ages (Number) (deaths)',ascending=False)
        df.iloc[0:5,2].plot.bar(title='Top 5 countries caused deaths reported in '+str(x),figsize=(6,5),rot=360)
        plt.ylabel('Number of deaths')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicDeath.html', {'graphicDeath': graphic.decode('utf8')})
        
    else :
        return render(request,'Top5Death.html')

def DgdpCount(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('direct-disaster-loss-as-a-share-of-gdp.csv')
        df1=(df[(df['Entity']==x)])
        df1=df1.set_index('Year')
        a=str(df1.iloc[0,0])
        df1.iloc[:,2].plot.bar(title=' Loss of Gdp in ' +a,figsize=(6,5))
        plt.ylabel('Percentage')
        plt.xlabel('Year')
        plt.tight_layout()

        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'DgdpGraphic.html', {'DgdpGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'DgdpCount.html')

def YearDgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        t=int(request.POST.get('txt'))
        print(x)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('direct-disaster-loss-as-a-share-of-gdp.csv')
        msg=1
        df1=(df[(df['Entity']==x)])
        df1=(df1[(df1['Year']==t)])
        print("rows",df1.shape)
        if df1.shape[0]==0:
            msg="Not enough data to plot "
            msg=0
            print("no data to plot")
            return render(request, 'DgdpGraphic1.html',{'msg':msg})
        else:
            msg=1
            df1=df1.set_index('Year')
            a=df1.iloc[0,0]
            df1.iloc[:20,2].plot.bar(title=' Loss of Gdp in ' +a,figsize=(6,5))
            plt.ylabel('Percentage')
            plt.xlabel('Year')
            buf = io.BytesIO()
            plt.margins(0.8)
            df1.iloc[:,2].plot.bar(title=' ' +a,figsize=(6,5))
            # Tweak spacing to prevent clipping of tick-labels
            plt.subplots_adjust(bottom=0.35)
            plt.savefig(buf, format='png',bbox_inches='tight')
    
            fig.savefig('abc.png')
        
            plt.close(fig)
            image = Image.open("abc.png")
            draw = ImageDraw.Draw(image)
        
            image.save(buf, 'PNG')
            content_type="Image/png"
            buffercontent=buf.getvalue()


            graphic = base64.b64encode(buffercontent) 
            return render(request, 'DgdpGraphic1.html', {'msg':msg,'DgdpGraphic1': graphic.decode('utf8')})
        
    else :
        return render(request,'YearDgdp.html')
        

def twoCountDgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        y=request.POST.get('dt')
        t=int(request.POST.get('txt'))
        print(x)
        print(y)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('direct-disaster-loss-as-a-share-of-gdp.csv')
        
        df1=df[df["Entity"].isin([x,y])]
        df1=(df1[df1["Year"]==t])
        df1=df1.set_index('Entity')
        a=str(df1.iloc[0,1])
        df1.iloc[:20,2].plot.bar(title=' Loss of Gdp in ' +a,figsize=(6,5))
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'DgdpGraphic.html', {'DgdpGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'twoCountDgdp.html')

def MaxDgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('direct-disaster-loss-as-a-share-of-gdp.csv')
        df=df.drop(2,axis=0)
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['11.5.2 - Direct economic loss attributed to disasters relative to GDP (%) - VC_DSR_LSGP (%)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Maximum GDP loss reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'DgdpGraphic.html', {'DgdpGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MaxDgdp.html')

def MinDgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('direct-disaster-loss-as-a-share-of-gdp.csv')
      
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['11.5.2 - Direct economic loss attributed to disasters relative to GDP (%) - VC_DSR_LSGP (%)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Minimum GDP loss reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'DgdpGraphic.html', {'DgdpGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MinDgdp.html')

def Top5Dgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('direct-disaster-loss-as-a-share-of-gdp.csv')
       
        df=(df[df['Year']==x])
        df=df.set_index('Entity')
        df=df.sort_values(by='11.5.2 - Direct economic loss attributed to disasters relative to GDP (%) - VC_DSR_LSGP (%)',ascending=False)
        df.iloc[0:5,2].plot.bar(title='Top 5 GDP losses reported in '+str(x),figsize=(6,5),rot=360)
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'DgdpGraphic.html', {'DgdpGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'Top5Dgdp.html')


def MaxGlobgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('global-disaster-losses-gdp.csv')
       
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Loss']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Maximum GDP loss reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'GlobGraphic.html', {'GlobGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MaxGlobgdp.html')

def MinGlobgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('global-disaster-losses-gdp.csv')
      
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Loss']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Minimum GDP loss reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'GlobGraphic.html', {'GlobGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MinGlobgdp.html')

def Top5Globgdp(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('global-disaster-losses-gdp.csv')
       
        df=(df[df['Year']==x])
        df=df.set_index('Entity')
        df=df.sort_values(by='Loss',ascending=False)
        df.iloc[0:5,2].plot.bar(title='Top 5 GDP losses reported in '+str(x),figsize=(6,5),rot=360)
        plt.ylabel('Percentage')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'GlobGraphic.html', {'GlobGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'Top5Globgdp.html')

def MaxGlobPreci(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('global-precipitation-anomaly.csv')
       
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Global precipitation anomaly (inches) (inches)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Maximum global precipitation reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Global precipitation anomaly(inches)')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'GlobPreciGraphic.html', {'GlobPreciGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MaxGlobPreci.html')

def MinGlobPreci(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('global-precipitation-anomaly.csv')
      
        df=(df[df['Year']==x])
        m=df.iloc[:,3].min()
        df=(df[df['Global precipitation anomaly (inches) (inches)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Minimum global precipitation reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Global precipitation anomaly(inches)')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'GlobPreciGraphic.html', {'GlobPreciGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'MinGlobPreci.html')

def Top5GlobPreci(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('global-precipitation-anomaly.csv')
       
        df=(df[df['Year']==x])
        df=df.set_index('Entity')
        df=df.sort_values(by='Global precipitation anomaly (inches) (inches)',ascending=False)
        df.iloc[0:5,2].plot.bar(title='Top 5 global precipitations reported in '+str(x),figsize=(6,5),rot=360)
        plt.ylabel('Global precipitation anomaly(inches)')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'GlobPreciGraphic.html', {'GlobPreciGraphic': graphic.decode('utf8')})
        
    else :
        return render(request,'Top5GlobPreci.html')





def InternalCount(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('internally-displaced-persons-from-disasters.csv')
        df1=(df[(df['Entity']==x)])
        df1=df1.set_index('Year')
        a=str(df1.iloc[0,0])
        df1.iloc[:,2].plot.bar(title=' Internally displaced persons in ' +a,figsize=(6,5))
        plt.ylabel('Number of cases')
        plt.xlabel('Year')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicInternal.html', {'graphicInternal': graphic.decode('utf8')})
        
    else :
        return render(request,'InternalCount.html')



def YearInternalDis(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        t=int(request.POST.get('txt'))
        print(x)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('internally-displaced-persons-from-disasters.csv')
        msg=1
        df1=(df[(df['Entity']==x)])
        df1=(df1[(df1['Year']==t)])
        if df1.shape[0]==0:
            msg="Not enough data to plot "
            msg=0
            print("no dat to plot")
            return render(request, 'graphicInternal1.html',{'msg':msg})
        else:
            msg=1
            df1=df1.set_index('Year')
            a=df1.iloc[0,0]
            df1.iloc[:20,2].plot.bar(title=' Internally Displaced person in ' +a,figsize=(6,5))
            plt.ylabel('Number of cases')
            plt.xlabel('Year')
            buf = io.BytesIO()
            plt.margins(0.8)
        # Tweak spacing to prevent clipping of tick-labels
            plt.subplots_adjust(bottom=0.35)
            plt.savefig(buf, format='png',bbox_inches='tight')
    
            fig.savefig('abc.png')
        
            plt.close(fig)
            image = Image.open("abc.png")
            draw = ImageDraw.Draw(image)
        
            image.save(buf, 'PNG')
            content_type="Image/png"
            buffercontent=buf.getvalue()


            graphic = base64.b64encode(buffercontent) 
            return render(request, 'graphicInternal1.html', {'msg':msg,'graphicInternal1': graphic.decode('utf8')})
        
    else :
        return render(request,'YearInternalDis.html')


def twoInternalDis(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=request.POST.get('d')
        y=request.POST.get('dt')
        t=int(request.POST.get('txt'))
        print(x)
        print(y)
        print(t)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('internally-displaced-persons-from-disasters.csv')
        
        df1=df[df["Entity"].isin([x,y])]
        df1=(df1[df1["Year"]==t])
        df1=df1.set_index('Entity')
        a=str(df1.iloc[0,1])
        df1.iloc[:20,2].plot.bar(title=' Internally Displaced person in ' +a,figsize=(6,5))
        plt.ylabel('Number of cases')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicInternal.html', {'graphicInternal': graphic.decode('utf8')})
        
    else :
        return render(request,'twoInternalDis.html')


def MaxInter(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('internally-displaced-persons-from-disasters.csv')
       
        df=(df[df['Year']==x])
        m=df.iloc[:,3].max()
        df=(df[df['Internally displaced persons, new displacement associated with disasters (number of cases) (number of cases)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Maximum displaced persons reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Number of cases')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicInternal.html', {'graphicInternal': graphic.decode('utf8')})
        
    else :
        return render(request,'MaxInter.html')

def MinInter(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('internally-displaced-persons-from-disasters.csv')
      
        df=(df[df['Year']==x])
        m=df.iloc[:,3].min()
        df=(df[df['Internally displaced persons, new displacement associated with disasters (number of cases) (number of cases)']==m])
        df=df.set_index('Entity')
        df.iloc[:,2].plot.bar(title="Minimum displaced persons reported in "+str(x),rot=360,figsize=(6,5))
        plt.ylabel('Number of cases')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicInternal.html', {'graphicInternal': graphic.decode('utf8')})
        
    else :
        return render(request,'MinInter.html')

def Top5Inter(request):
    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        x=int(request.POST.get('txt'))
        print(x)
        fig=plt.figure(figsize=(6, 7), dpi=80,facecolor='w', edgecolor='w')
        matplotlib.rcParams['axes.labelsize'] = 14
        matplotlib.rcParams['xtick.labelsize'] = 8
        matplotlib.rcParams['ytick.labelsize'] = 12
        matplotlib.rcParams['text.color'] = 'k'
        df = pd.read_csv('internally-displaced-persons-from-disasters.csv')
       
        df=(df[df['Year']==x])
        df=df.set_index('Entity')
        df=df.sort_values(by='Internally displaced persons, new displacement associated with disasters (number of cases) (number of cases)',ascending=False)
        df.iloc[0:5,2].plot.bar(title='Top 5 internal displacements reported in '+str(x),figsize=(6,5),rot=360)
        plt.ylabel('Number of cases')
        buf = io.BytesIO()
        plt.margins(0.8)
    # Tweak spacing to prevent clipping of tick-labels
        plt.subplots_adjust(bottom=0.35)
        plt.savefig(buf, format='png',bbox_inches='tight')
   
        fig.savefig('abc.png')
    
        plt.close(fig)
        image = Image.open("abc.png")
        draw = ImageDraw.Draw(image)
    
        image.save(buf, 'PNG')
        content_type="Image/png"
        buffercontent=buf.getvalue()


        graphic = base64.b64encode(buffercontent) 
        return render(request, 'graphicInternal.html', {'graphicInternal': graphic.decode('utf8')})
        
    else :
        return render(request,'Top5Inter.html')




def earthform(request):

    if not request.session.has_key('email'):
        return redirect('/LogIn')
    if request.method == 'POST':
        date= request.POST.get('txt1')
       
        longi= request.POST.get('txt3')
        lati= request.POST.get('txt4')
        print("date",date)
       
        print('longi',longi)
        print('lati',lati)
        data = pd.read_csv("database (1).csv")
        #t="12"
        #lati= "19.246"
       # longi= "145.616"
        data.head()
        data = data[['Date', 'Time', 'Latitude', 'Longitude', 'Depth', 'Magnitude']]
        data.head()
        d=date
        def dateformat(x):
            dt = parse(x)
            return(dt.strftime('%m/%d/%Y'))
        d=dateformat(d)
        print("after format",d)
        s=datetime.datetime.strptime(d, "%m/%d/%Y").timetuple()
        tm=timelibrary.mktime(s)
        pkl_filename="earth_model.pkl"
        with open(pkl_filename, 'rb') as file:
            pickle_model = pickle.load(file)
        reg=pickle_model
        data['Date']=data['Date'].apply(dateformat)
        timestamp = []
        print(data.head(20))
        data=data[14670:]
        for d, t in zip(data['Date'], data['Time']):
            try:
                #ts = datetime.datetime.strptime(d+' '+t, '%m/%d/%Y %H:%M:%S')
                #print(ts.timetuple())
                #t = datetime(ts.timetuple())
                s=datetime.datetime.strptime(d, "%m/%d/%Y").timetuple()
                timestamp.append(timelibrary.mktime(s))
            except ValueError:
                # print('ValueError')
                timestamp.append('ValueError')
        timeStamp = pd.Series(timestamp)
        data['Timestamp'] = timeStamp.values
        final_data = data.drop(['Date', 'Time'], axis=1)
        ##final_data = final_data[final_data.Timestamp != 'ValueError']
        final_data.dtypes
        X = final_data[['Timestamp', 'Latitude', 'Longitude']]
        y = final_data[['Magnitude', 'Depth']]
        print(X.shape,"X")
        print(y.shape,"y")
        X.iloc[8741,0]=tm
        X.iloc[8741,1]=lati
        X.iloc[8741,2]=longi

        y=reg.predict(X)

        print(y[8741])
        r=y[8741]
        return render(request,'earthquakePredResult.html',{'y':r})
    else:         
        return render(request,'earthform.html')

