from django.shortcuts import render
#from .models import Job
def home(request):
    #jobs=Job.objects
    return render(request, 'jobs/jobshome.html' )#, {'jobs':jobs})

def about(request):
    return render(request,'jobs/jobsabout.html')    