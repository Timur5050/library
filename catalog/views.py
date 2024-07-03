from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book, Author, LiteraryFormat


def index(request: HttpRequest) -> HttpResponse:
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_literary_formats = LiteraryFormat.objects.count()
    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_literary_formats': num_literary_formats
    }

    return render(request, "catalog/index.html", context=context)


class LiteraryFormatListView(ListView):
    model = LiteraryFormat
    template_name = "catalog/literary_format_list.html"
    context_object_name = "literary_format_list"
    #queryset = LiteraryFormat.objects.filter(name__endswith="y")


class BooksListView(ListView):
    model = Book
    queryset = Book.objects.select_related("format")
    paginate_by = 1


class AuthorsListView(ListView):
    model = Author


class BookDetailView(DetailView):
    model = Book

# def book_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
#     book = Book.objects.get(id=pk)
#     context = {
#         'book': book,
#     }
#
#     return render(request, "catalog/book_detail.html", context=context)

# def literary_format_list_view(request: HttpRequest) -> HttpResponse:
#     literary_format_list = LiteraryFormat.objects.all()
#     context = {
#         "literary_format_list": literary_format_list
#     }
#
#     return render(request, "catalog/literary_format_list.html", context=context)
