from django.shortcuts import render
from application.models import Post
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    message = "Список постов:\n\n\n"
    for post in Post.objects.all():
        message += str(post.title) + '\n' + str(post.content) + '\n' + str(post.published)
    return HttpResponse(message, content_type="text/plain; charset=utf-8")



