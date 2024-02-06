from django.shortcuts import render
from app1.models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')
def adminsignup(request):
    if (request.method == "POST"):
        u = request.POST['u'] #or we can use request.get[]
        p = request.POST['p']
        cp = request.POST['cp']
        fname = request.POST['f']
        lname = request.POST['l']
        e = request.POST['e']
        pl = request.POST['pl']
        n = request.POST['n']

        if (p == cp):
            user = CustomUser.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=e,
                                                  place=pl, phone=n)
            user.is_admin=True
            user.save()
            return home(request)
    return render(request,'adminsignup.html')
def studentsignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        fname = request.POST['f']
        lname = request.POST['l']
        e = request.POST['e']
        pl = request.POST['pl']
        n = request.POST['n']

        if (p == cp):
            user = CustomUser.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=e,
                                                  place=pl, phone=n)
            user.is_student=True
            user.save()
            return home(request)
    return render(request,'studentsignup.html')
def teachersignup(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        fname = request.POST['f']
        lname = request.POST['l']
        e = request.POST['e']
        pl = request.POST['pl']
        n = request.POST['n']

        if (p == cp):
            user = CustomUser.objects.create_user(username=u, password=p, first_name=fname, last_name=lname, email=e,
                                                  place=pl, phone=n)
            user.is_teacher=True
            user.save()
            return home(request)
    return render(request,'teachersignup.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.is_admin==True:
            login(request,user)
            return adminhome(request)
        elif user and user.is_student==True:
            login(request,user)
            return studenthome(request)
        if user and user.is_teacher==True:
            login(request,user)
            return teacherhome(request)
        else:
            return HttpResponse("Invalid credentials")

    return render(request,'login.html')
def adminhome(request):
    return render(request,'adminhome.html')
def studenthome(request):
    return render(request,'studenthome.html')
def teacherhome(request):
    return render(request,'teacherhome.html')

def user_logout(request):
    logout(request)
    return user_login(request)
