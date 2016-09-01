from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from .form import PostForm
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
def post_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10)  # Show 10 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        'title' : 'List',
        'object_list': queryset,
        'page_request_var':page_request_var
    }

    return render(request, 'post_list.html', context)


def listing(request):
    contact_list = Contacts.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'contacts': contacts})


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