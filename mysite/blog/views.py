from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Post
from. forms import PostForm
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        
    
    context = {
        "form": form,
        
        }
    return render (request,"blog/post_form.html",context)

def post_update(request, id=None):

    return render (request,"blog/post_edit.html",context)
def post_delete(request):
    return HttpResponse("<h1>Delete </h1>")


#ignore for now..
def post_detail(request):
    return HttpResponse("<h1>Detail</h1>")


def post_list(request):
    return HttpResponse("<h1> List </h1>")



