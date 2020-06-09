from django.shortcuts import render, HttpResponse
from article.models import Article, Author


def homepage(request):
    articles = Article.objects.all()
    wind = Author.objects.get(id=1)
    
    return render(request, "article/homepage.html", 
    {
        "articles": articles,
        "wind":wind
        
    })

# Create your views here.
