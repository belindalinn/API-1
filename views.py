from django.shortcuts import render

from django.db import IntegrityError  # Import IntegrityError
from django.http import JsonResponse  # Import JsonResponse
from .models import Book  # Import the Book model
from django.views.decorators.csrf import csrf_exempt  # Import csrf_exempt decorator
from django.forms.models import model_to_dict  # Import model_to_dict

@csrf_exempt
def books(request):
    if request.method == 'GET':
        books = Book.objects.all().values()
        return JsonResponse({'books': list(books)})
    elif request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')

        book = (title == title, author==author, price==price)

        try:
            book.save()
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
        return JsonResponse(model_to_dict(books), status=201)
