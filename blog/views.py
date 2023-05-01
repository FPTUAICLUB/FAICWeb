from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Article, Profile, Tag


def index(request):
    # feature articles on the home page
    featured = Article.articlemanager.filter(featured=True)[0:3]

    context = {"articles": featured}

    return render(request, "blog/index.html", context)


def article(request, article):
    article = get_object_or_404(Article, slug=article, status="published")

    context = {"article": article}

    return render(request, "blog/article.html", context)


def articles(request):
    # get query from request
    query = request.GET.get("query")
    # print(query)
    # Set query to '' if None
    if query == None:
        query = ""

    # articles = Article.articlemanager.all()
    # search for query in headline, sub headline, body
    articles = Article.articlemanager.filter(
        Q(headline__icontains=query)
        | Q(sub_headline__icontains=query)
        | Q(body__icontains=query)
    )

    tags = Tag.objects.all()

    context = {
        "articles": articles,
        "tags": tags,
    }

    return render(request, "blog/articles.html", context)
