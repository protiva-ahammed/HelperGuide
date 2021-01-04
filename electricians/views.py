from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Electrician
from django.utils import timezone

def eeelist(request):
    e = Electrician.objects
    return render(request, 'electricians/eeelist.html',{'e': e})

@login_required
def electricianreg(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['name'] and request.POST['experience'] and request.POST['esalary'] and request.POST['contract'] and request.POST['address'] and request.POST['skill'] and request.POST['url'] and request.FILES['image']:
            e = Electrician()
            e.title = request.POST['title']
            e.name = request.POST['name']
            e.experience= request.POST['experience']
            e.esalary = request.POST['esalary']
            e.contract = request.POST['contract']
            e.address = request.POST['address']
            e.skill = request.POST['skill']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                e.url=request.POST['url']

            else:
                e.url="http://" + request.POST['url']
            #e.cv = request.FILES['cv']
            e.image = request.FILES['image']
            e.pub_date=timezone.datetime.now()
            e.seeker=request.user
            e.save()
            return redirect('/electricians/' + str(e.id))




        else:
            return render(request,'eletricians/regform.html',{'error':'All Fields are required'})



    else:
        return render(request,'electricians/regform.html')





def detailjobe(request,e_id):
    e=get_object_or_404(Electrician, pk=e_id)
    return render(request,'electricians/detail.html', {'e':e} )


@login_required(login_url="/accounts/signup")
def eupvote(request, e_id):
    if request.method == 'POST':
        e = get_object_or_404(Electrician, pk=e_id)
        e.votes_total += 1
        e.save()
        return redirect('/electricians/' + str(e.id))