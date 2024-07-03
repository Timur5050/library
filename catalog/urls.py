from django.urls import path

from catalog.views import (
    index,
    LiteraryFormatListView,
    BooksListView,
    AuthorsListView,
    BookDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path("literary-formats/", LiteraryFormatListView.as_view(), name="literary-format-list"),
    path("books/", BooksListView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("authors/", AuthorsListView.as_view(), name="author-list"),
]
app_name = "catalog"
