from django.shortcuts import render, get_object_or_404
from . import views
from django.contrib.auth.decorators import login_required
from . models import Showpost

def allposts(request):
    showposts=Showpost.objects
    return render(request,'showposts/showpostshome.html' , {'showposts':showposts})
@login_required(login_url="/accounts/login")
def detail(request,showpost_id):
    showpost=get_object_or_404(Showpost, pk=showpost_id)
    return render(request,'showposts/detail_post.html',{'showpost':showpost})