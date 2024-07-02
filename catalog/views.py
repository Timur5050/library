import datetime
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<html>"
                        "<h1>welcome to library</h1>"
                        "</html>")
