from django.shortcuts import render, redirect
from .forms import UserFileForm, FileModelForm
from .models import FileModel
from .ocr_engine import get_text
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.forms import UserChangeForm
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os
#from googletrans import Translator

def download_pdf(request):
   # some code
   file_data = request.POST["txtareaField"]
   
   if request.POST.get("txt"):
       response = HttpResponse(file_data, content_type='application/text charset=utf-8')
       response['Content-Disposition'] = 'attachment; filename="text.txt"'
   if request.POST.get("pdf"):
       response = HttpResponse(file_data, content_type='application/pdf')
       response['Content-Disposition'] = 'attachment; filename=%s' % 'text.pdf'
   if request.POST.get("docs"):
       response = HttpResponse(file_data, content_type='application/docs')
       response['Content-Disposition'] = 'attachment; filename="text.docs"'

   return response

def homepage(request):
    bool = "false"
    if request.user.is_authenticated:
        bool="true"
    
    context = {'form': UserFileForm(),'bool':bool}
    if request.method == 'POST':
        user_input = UserFileForm(request.POST, request.FILES)
        if user_input.is_valid():
            fileobj = request.FILES['userfile']
            lang = user_input.cleaned_data['lang']
            is_image = fileobj.name.endswith(('jpg', 'png', 'jpeg', 'tiff'))
            if is_image:
                multi = False
            else:
                multi = True
            text = get_text(fileobj, lang, multi)
            context['text'] = text
            return render(request, 'ocr/index.html', context)
        else:
           context['form_error'] = 'Error! File can not be converted for recognition'
           return render(request, 'ocr/index.html', context)

    
    
    return render(request, 'ocr/index.html', context)

# handel user login reuest

def userLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            return redirect("homepage")
            messages.info(request, 'You are logged in succesffully!')
        else:
             messages.info(request, 'Username or password is invalid, Please check it once.!')
             return render(request, 'ocr/error404.html')

    else:
        return render(request, 'ocr/error404.html')


def userLogout(request):
    logout(request)
    return redirect('homepage')


def userSignup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input

        if (pass1 != pass2):
            messages.info(request, 'Your passsword is not matching')
            return redirect('homepage')

        # chekc username is unique or not and Create new user
        try:
            user= User.objects.get(username=username)
            messages.info(request, 'Your username is not unique. try another one')
            return redirect('homepage') 
        except User.DoesNotExist:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            login(request, myuser)
            messages.info(request, 'Welcome to Django-ocr app! You have created your account successfully')
            return redirect('homepage')      
    else:
        return render(request, 'ocr/error404.html')

def ContactUs(request):
    return render(request,'ocr/contactus.html')