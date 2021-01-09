from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm, LoginForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from article.models import Article
from .models import Info

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password= form.cleaned_data.get("password")
        first_name= form.cleaned_data.get("name")
        last_name= form.cleaned_data.get("surname")
        email= form.cleaned_data.get("email")
        birthday= form.cleaned_data.get("date")
        newUser=User(username = username, first_name=first_name, last_name=last_name,email=email)
        newUser.set_password(password)
        newinfo=Info(username=newUser,birthday=birthday)
        newUser.save()
        newinfo.save()
        
        
        messages.success(request,"başarıyla giriş yaptınız")
        return redirect("index")
    else:
        context={
        "form":form
        }

        return render(request,"register.html",context)

def loginUser(request):
    form=LoginForm(request.POST or None)

    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username, password=password)
        if user is None:
            messages.info(request,"böyle bir kullanıcı bulunmamaktadır")
            return render(request,"login.html",context)
        else:
            messages.success(request,"başarıyla giriş yaptınız")
            login(request,user)
            return redirect("index")
    return render(request,"login.html",context)
@login_required(login_url="user:login")
def logoutUser(request):
    logout(request)
    messages.success(request,"başarıyla çıkış yapıldı")
    return redirect("index")
@login_required
def profile(request,id):
    user=get_object_or_404(User,id=id)
    if request.user==user:
        articles=Article.objects.filter(author=request.user)
        info=Info.objects.filter(username=request.user).first()
        form=ProfileForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            user_img=form.cleaned_data.get("user_img")
            newimg=Info.objects.filter(username=request.user).first()
            newimg.user_img=user_img
            newimg.save()
            return redirect("http://localhost:8000/user/"+str(request.user.id))
        

        return render(request,"profile.html",{"user":user,"articles":articles,"info":info,"form":form})
    else:
        articles=Article.objects.filter(author=user)
        info=Info.objects.filter(username=user).first()
        form=ProfileForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            user_img=form.cleaned_data.get("user_img")
            newimg=Info.objects.filter(username=request.user).first()
            newimg.user_img=user_img
            newimg.save()
            return redirect("http://localhost:8000/user/"+str(request.user.id))
        

        return render(request,"profile.html",{"user":user,"articles":articles,"info":info,"form":form})

