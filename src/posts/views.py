from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
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
    instance= get_object_or_404(Post,id=3)
    if request.user.is_authenticated():
        context = {
            'title' : 'My User Detail',
            'instance': instance
        }
    else:
        context = {
            'title' : 'Detail',
            'instance': instance
        }
    return render(request, 'post_detail.html', context)

def post_create(request):
    return HttpResponse('<h1>create</h1')

def post_delete(request):
    return HttpResponse('<h1>delete</h1')

def post_update(request):
    return HttpResponse('<h1>update</h1')