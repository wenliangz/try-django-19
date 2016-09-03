from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect,Http404
from .models import Post
from .form import PostForm
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from urllib.parse import quote_plus
from django.utils import timezone
from django.db.models import Q

# Create your views here.
def post_list(request):
    today = timezone.now().date()
    queryset_list = Post.objects.active()  # .order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()

    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        ).distinct()
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

def post_detail(request,slug=None):
    instance= get_object_or_404(Post,slug=slug)
    share_sting =quote_plus(instance.content)
    context = {
            'title' : 'title',
            'instance': instance,
            'share_string':share_sting
        }
    return render(request, 'post_detail.html', context)

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None) # pass the request.POST object for validation, add 'or None' to prevent from showing validation all the time
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,'Post successfully created!')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post_form.html', context)

def post_update(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None,request.FILES or None,instance=instance)
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

def post_delete(request,slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request, 'Successfully Deleted!')
    return redirect('posts:list')