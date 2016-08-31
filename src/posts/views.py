from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    queryset = Post.objects.all()
    if request.user.is_authenticated():
        context = {
            'title' : 'My User list',
            'object_list': queryset
        }
    else:
        context = {
            'title' : 'List',
            'object_list': queryset
        }
    return render(request, 'index.html', context)


def post_detail(request):
    return HttpResponse('<h1>detail</h1')

def post_create(request):
    return HttpResponse('<h1>create</h1')

def post_delete(request):
    return HttpResponse('<h1>delete</h1')

def post_update(request):
    return HttpResponse('<h1>update</h1')