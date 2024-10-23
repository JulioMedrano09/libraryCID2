from django.shortcuts import render, redirect
from unicodedata import name
from pymysql import NULL
from .models  import  Book



def index(request, letter = NULL):
    if letter != NULL:
        books = Book.objects.filter(title__istartswith=letter)
    else:   
        books = Book.objects.filter(title__contains= request.GET.get('search', ''))
    context = {
        'books': books 
    }
    return render(request, 'book/index.html', context)

def view(request, id ):
    book = Book.objects.get(id=id)
    context = {
        'book': book
    }
    return render(request, 'book/detail.html', context)
