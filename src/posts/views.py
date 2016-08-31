from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
from .form import PostForm

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


def post_detail(request,id=None):
    instance= get_object_or_404(Post,id=id)
    context = {
            'title' : 'Detail',
            'instance': instance
        }
    return render(request, 'post_detail.html', context)

def post_create(request):
    form = PostForm(request.POST or None) # pass the request.POST object for validation, add 'or None' to prevent from showing validation all the time
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form,
    }

    return render(request, 'post_create.html', context)

def post_delete(request):
    return HttpResponse('<h1>delete</h1>')

def post_update(request):
    return HttpResponse('<h1>update</h1>')