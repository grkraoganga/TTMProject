from django.core.mail import send_mail
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from .models import Admin, Register,Packages


#def adminhome(request):
#    return render(request,"adminhome.html")



def ttmhome(request):
    return render(request,"ttmhome.html")

def checkadminlogin(request):
    if request.method == "POST":
        name = request.POST["uname"]
        pwdd = request.POST["pwd"]
        #flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
        flag=Register.objects.filter(username=name,password=pwdd).values()
        if flag:    #flag is not empty
            if name=="venkat":   #venkat is admin
                messages.info(request,"This is admin TTM page")
                return render(request,"adminhome.html")
        if flag:
            messages.info(request, "This is User's TTM page")
            return render(request,"ttmhome.html")
        else:
            messages.info(request, "Your credentials are not correct")
            return render(request,"loginfail.html")
def checkregistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        addr = request.POST["addr"]
        email = request.POST["email"]
        phno = request.POST["phno"]
        uname = request.POST["uname"]
        pwd = request.POST["pwd"]
        cpwd = request.POST["cpwd"]
        if pwd == cpwd:
            if Register.objects.filter(username=uname).exists():
                messages.info(request, "username existing...")
                return render(request,"register.html")
            elif Register.objects.filter(email=email).exists():
                messages.info(request, "email existing...")
                return render(request, "register.html")
            else:
                user = Register.objects.create(name=name,address=addr,email=email,phno=phno,username=uname,password=pwd)
                user.save()
                messages.info(request, "user created...")
                return render(request, "login.html")
        else:
            messages.info(request, "password is not matching...")
            return render(request,"register.html")
def checkpackages(request):
    if request.method == "POST":
        tcode = request.POST["tourcode"]
        tname = request.POST["tourname"]
        tpack = request.POST["tourpackage"]
        tdesc = request.POST["desc"]
        pack = Packages.objects.create(tourcode=tcode, tourname=tname, tourpackage=tpack, desc=tdesc)
        pack.save()
        messages.info(request,"Data inserted suceessfully")
        return render(request,"package.html")
    else:
        return render(request, "package.html")

def viewplaces(request):
    data = Packages.objects.all() # get all objects of Packages class
    return render(request,"viewplaces.html",{"placesdata":data})
def checkChangePassword(request):
    if request.method == "POST":
        uname = request.POST["uname"]
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Register.objects.filter(username=uname, password=opwd).values()
        if flag:
            Register.objects.filter(username=uname, password=opwd).update(password=npwd)
            messages.info(request, "Password Updated")
            return render(request, "index.html")
        else:
            messages.info(request,"Password Updated")
            return render(request, "index.html")
    else:
        return render(request, "changepassword.html")
def logout(request):
    messages.info(request,"Logout")
    return render(request,"index.html")
def mail(request):
    return render(request,"sendmail.html")
def sendmail(request):
    if request.method == "POST":
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(subject,message,'grkraoganga@gmail.com',['grkraoganga@gmail.com'],fail_silently=False)
        return HttpResponse("Mailsent Successfully")
    else:
        return render(request,'sendmail.html')