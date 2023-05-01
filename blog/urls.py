from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("articles/", views.articles, name="articles"),
    path("<slug:article>/", views.article, name="article"),
]
