from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    text1 = "Helllo world"
    text2 = "Hello Bebish"
    return render(request, "./index.html",{
        "text1": text1,
        "text2": text2,
    })