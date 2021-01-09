from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import addArticle
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.models import Info
# Create your views here.
def articles(request):
    keyword=request.GET.get("keyword")
    if keyword: 
        articles=Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()

    return render(request,"articles.html",{"articles":articles})
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    return render(request,"dashboard.html",{"articles":articles})
@login_required(login_url="user:login")
def addarticle(request):
    form=addArticle(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"makale başarıyla eklendi")
        return redirect("index")
    context={
         "form":form
    }
    return render(request,"addarticle.html",context)
def detail(request,id):
    article=get_object_or_404(Article,id=id)
    comments=article.comments.all()
    img=Info.objects.all()
    print(img)
    return render(request,"detail.html",{"article":article,"comments":comments,"img":img})
@login_required(login_url="user:login")
def update(request,id):
    article=get_object_or_404(Article,id=id)
    form=addArticle(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"makale başarıyla güncellendi")
        return redirect("article:dashboard")
    context={
         "form":form
    }
    return render(request,"update.html",context)
@login_required(login_url="user:login")
def delete(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"makale başarıyla silindi")
    return redirect("article:dashboard")
def comment(request,id):
    comment=get_object_or_404(Article,id=id)
    if request.method=="POST":
        comment.user=request.user
        comment.comment=request.POST.get("comment")
        newcomment=Comment(user=comment.user, comment=comment.comment)

        newcomment.article=comment
        newcomment.save()

    return redirect(reverse("article:detail",kwargs={"id":id}))






