import json
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import Author, Book


authorsList = ['leo_tolstoy', 'alexandre_dumas']
authors_and_books = [
    {'title': 'War and Peace', 'author': 'leo_tolstoy'},
    {'title': 'Anna Karenina', 'author': 'leo_tolstoy'},
    {'title': 'Resurrection', 'author': 'leo_tolstoy'},
    {'title': 'The Three Musketeer', 'author': 'alexandre_dumas'},
    {'title': 'The Count of Monte Cristo', 'author': 'alexandre_dumas'}
]


def index(req):
    authors = Author.objects.all()
    books = Book.objects.all()
    # print('Author List is : \n')
    # for a in authors:
    #     print(a.name)
    # print('authors: ', authors, '\n', 'books : ', books)
    return render(req, 'index.html', context={'authorsList': authors, 'bookList': books})


def add_author(req):
    tempList = []
    for author in authorsList:
        print('author : ', author)
        tempList.append(Author(name=author))
        # Author.objects.create(name=author)
    print('authorList : ',  tempList)
    res = Author.objects.bulk_create(tempList)
    print('res: ', res)
    return HttpResponseRedirect(redirect_to='/')
    # return HttpResponse('Hello World !!!')


def add_book(req):
    print('add book here')
    try:
        for ele in authors_and_books:
            print(ele['title'], ele['author'])
            authors = Author.objects.filter(name=ele['author'])
            if len(authors) > 0:
                author = authors[0]
                print(author.id)
                books = Book.objects.create(
                    title=ele['title'], author_id=author.id)
            else:
                print('Authors not found')
    except Exception as e:
        print(e)
    return HttpResponseRedirect(redirect_to='/')


def book_and_author(req):
    books = Book.objects.all()
    if books:
        for book in books:
            # print(f'{book.title} {book.author_id}')
            author = Author.objects.get(pk=book.author_id)
            # print(author.name)
            print(f"'{book.title}'. {author.name}")
    else:
        print('books nort found')
    return HttpResponse('look at the python console')
    # return HttpResponseRedirect(redirect_to='/')


def author_and_books(req):
    authors = Author.objects.all()
    if authors: 
        for author in authors:
            # print(author.id,author.name)
            print(author.name, end=":")
            books = Book.objects.filter(author_id=author.id)
            for book in books:
                print(book.title, end=",")
            print("")
    return HttpResponse('look at the python console')

def author_and_books_count(req):
    authors = Author.objects.all()
    if authors: 
        for author in authors:
            # print(author.id,author.name)
            print(author.name, end=":")
            books = Book.objects.filter(author_id=author.id)
            # for book in books:
            print(len(books), end="\n")
    return HttpResponse('look at the python console')
