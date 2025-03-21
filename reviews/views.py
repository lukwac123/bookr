from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def index(request):
    return render(request, "base.html")


def book_search(request):
    search_text = request.GET.get("search", "")
    return render(request, "search-results.html", {"search_text": search_text})


def welcome_view(request):
    message = f"<html><h1>Witaj w witrynie Bookr!</h1><p>{Book.objects.count()} książek i stale dodajemy nowe!</p></html>"
    return HttpResponse(message)
