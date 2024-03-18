from django.shortcuts import render
def homePage(request):
    return render(request,"index.html")
def loginPage(request):
    return render(request,"login1.html")
def registrationPage(request):
    return render(request,"register.html")