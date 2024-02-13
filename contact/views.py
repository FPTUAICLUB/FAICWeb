from django.shortcuts import render, redirect
from .models import Contact
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get("name")
        email = request.POST.get("email")
        messages = request.POST.get("messages")
        contact.name = name
        contact.email = email
        contact.messages = messages
        contact.save()
        return render(request, "contact/response.html")
    return render(request, "contact/index.html")
