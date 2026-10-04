from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    date = datetime.now()
    #return render(request, "index.html", context={"prenom":"Bruno"})
    return render(request, "DocBlog/index.html", context={"date":date})