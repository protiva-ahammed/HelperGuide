from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Createjob
from django.utils import timezone

def createjoblist(request):
    createjob = Createjob.objects
    return render(request, 'createjobs/createjoblist.html',{'createjob':createjob})

@login_required
def create(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['duration'] and request.POST['salary'] and request.POST['contract'] and request.POST['address'] and request.POST['description'] and request.POST['url'] and request.FILES['icon']:
            createjob = Createjob()
            createjob.title = request.POST['title']
            createjob.duration = request.POST['duration']
            createjob.salary = request.POST['salary']
            createjob.contract = request.POST['contract']
            createjob.address = request.POST['address']
            createjob.description = request.POST['description']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                createjob.url=request.POST['url']

            else:
                createjob.url="http://" + request.POST['url']
            createjob.icon = request.FILES['icon']
            createjob.pub_date=timezone.datetime.now()
            createjob.hunter=request.user
            createjob.save()
            return redirect('/createjobs/' + str(createjob.id))




        else:
            return render(request,'createjobs/create.html',{'error':'All Fields are required'})



    else:
        return render(request,'createjobs/create.html')




@login_required(login_url="/accounts/login")
def detailjob(request,createjob_id):
    createjob=get_object_or_404(Createjob,pk=createjob_id)
    return render(request,'createjobs/detail.html',{'createjob':createjob})


@login_required(login_url="/accounts/login")
def upvote(request, createjob_id):
    if request.method == 'POST':
        createjob = get_object_or_404(Createjob, pk=createjob_id)
        createjob.votes_total += 1
        createjob.save()
        return redirect('/createjobs/' + str(createjob.id))