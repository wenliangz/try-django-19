from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request,'index.html',{})
def post_detail(request):
    return HttpResponse('<h1>detail</h1')

def post_create(request):
    return HttpResponse('<h1>create</h1')

def post_delete(request):
    return HttpResponse('<h1>delete</h1')

def post_update(request):
    return HttpResponse('<h1>update</h1')