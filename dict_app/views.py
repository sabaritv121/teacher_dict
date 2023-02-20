from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import *


# Create your views here.
def home(request):
    return render(request,"home.html")

def base(request):
    return render(request,"djangify/Modified_files/index.html")



    


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('add')
            # elif user.is_importer:
            #     return redirect('cm')
            # elif user.is_user:
            #     return redirect('user_home')
        else:
                messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')

#teacher add

def teacher_add(request):
    form = TeacherAddForm()
    if request.method == 'POST':
        form = TeacherAddForm(request.POST,request.FILES)
        

        if form.is_valid():
            form.save()
            return redirect('base')

    return render(request,'register.html',{'form':form})


#view details

def view(request):
    data=Teacher.objects.all()
    return render(request,'view.html',{"data":data})    