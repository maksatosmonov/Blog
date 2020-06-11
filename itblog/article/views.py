from django.shortcuts import render, HttpResponse
from article.models import Article, Author
from django.contrib.auth.models import User
from .forms import ArticleForm, AuthorForm


def homepage(request):
    articles = Article.objects.filter(active=True)
    wind = Author.objects.get(id=1)
    
    return render(request, "article/homepage.html", 
    {"articles":articles})

def article(request, id):
    if request.method =="POST":
        article = Article.objects.get(id=id)
        article.active = False
        article.save()
        return redirect(homepage) 

    article = Article.objects.get(id=id)
    return render(request, "article/article.html", {"article": article})


def add_article(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get("title")
        article.text = request.POST.get("text")
        author_id = request.POST.get("author")
        author = Author.objects.get(id=author_id)
        article.author = author
        article.save()
        return render(request, "article/success.html")

    form = ArticleForm()
    return render(request, "article/add_article.html", {"form":form})

def authors(request):
    context = {}
    context["authors_all"] = Author.objects.all()
    return render(request, "article/authors.html", context)

def add_author(request):
    if request.method == "POST":
        author = Author()
        author.name = request.POST.get("name")
        author.save()
        return render(request, "article/success.html")

    form = AuthorForm()
    return render(request, "article/add_author.html", {"form":form})


def users(request):
    context = {}
    context["user_all"] = User.objects.all()
    return render(request, "article/users.html", context)



# Create your views here.
