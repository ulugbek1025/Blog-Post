from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

# Create your views here.

def register(request):

    form=RegisterForm(request.POST or None)

    if form.is_valid():

            # Create a new user object but avoid saving it yet
            newuser = form.save(commit=False)
            # Set the chosen password
            newuser.set_password(
            form.cleaned_data['password'])
            # Save the User object
            newuser.save()

            login(request,newuser, backend='django.contrib.auth.backends.ModelBackend')
            messages.info(request,'You have successfully registered...')
            return redirect("index")
    context = {
            "form" : form
            }
    return render(request,'user/register.html',context)



def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"user/login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect("index")
    return render(request,"user/login.html",context)

def logoutuser(request):
    logout(request)
    messages.success(request,'You have successfully  Logout')
    return redirect('index')
