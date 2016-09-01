from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .form import PostForm
from django.contrib import messages

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
            'title' : 'title',
            'instance': instance
        }
    return render(request, 'post_detail.html', context)

def post_create(request):
    form = PostForm(request.POST or None) # pass the request.POST object for validation, add 'or None' to prevent from showing validation all the time
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,'Post successfully created!')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_update(request,id=None):
    instance = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post Saved!', extra_tags='some tag')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title':instance.title,
        'form': form,
        'instance':instance
    }
    return render(request, 'post_form.html', context)

def post_delete(request,id=None):
    instance = get_object_or_404(Post,id=id)
    instance.delete()
    messages.success(request, 'Successfully Deleted!')
    return redirect('posts:list')